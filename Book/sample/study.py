import time
import csv
import itertools
from RnDTestLib.TestLib import Test_lib, Test_const, Test_algo_lib, Test_tune_lib, Test_config_lib
import numpy as np
from RnDTestLib.TestLib import Test_algo_lib
from RnDTestLib.IOInterface.IOInterface import IOInterface
import os
import glob

#define DUT
dut_0 = REF # 4 VOAs
dut_1 = DUT # 2 VOAs

#define Power Suplies
#PS_DUT_0 = PS_EUI
#PS_DUT_1 = PS_DUT

#define TempControl Oven
# TC= TC1

#create test class instance
myTest = Test_algo_lib.HRT_Class(True)

try:
    myio_dut_0 = IOInterface(dut_0, 'I2C', 0xA0, 0x0)
    myio_dut_1 = IOInterface(dut_1, 'I2C', 0xA0, 0x0)
except Exception as e:
    raise Exception('Cannot read EUI board! - %s' + str(e))




#=====================Helper Functions Start=====================#
def setatt(targetAtt, ATT):
    current_att = -round(ATT.ReadAttenuation(), 2)
    if targetAtt < 0:
        print ('Target att %s dBm is too high, will use minimum attenuation instead' % (targetAtt))
        ATT.SetMinAttenuation()
    else:
        ATT.SetAttenuation(targetAtt)
    current_att = -round(ATT.ReadAttenuation(),2)
    print ('Attenuation set to %s dB' % (current_att))
    return current_att


def readBERonBoardED(Lanelist, EDlist, gating = 6):
    BER_list = []
    BitError_list = []
    TotalBit_list = []
    IsSync_list = []
    #start bert
    print ('==========================================================================')
    for iter, ED in enumerate(EDlist):
        ED.Stop()
    time.sleep(0.1)
    for iter, ED in enumerate(EDlist):
        ED.Start()
    time.sleep(gating)
    for iter, ED in enumerate(EDlist):
        BitError_list.append(ED.ErrorCount())
        TotalBit_list.append(ED.BitCount())
        BER_list.append(ED.BER())
        IsSync_list.append(ED.IsEDInSync)
        ED.Stop()
        print ('Lane %s BER is %s, error count is %s, total bit is %s, sync %s'%(Lanelist[iter], BER_list[iter], BitError_list[iter], TotalBit_list[iter], IsSync_list[iter]))
    print ('==========================================================================')
    return BER_list, BitError_list, TotalBit_list, IsSync_list

def get_tx_los_lol_MSA(DUTM):
    myTest.SetPassword(DUTM)
    pageNumber = 0x11

    memAddress = 136   # TX LOS
    myTest.msa_byte_read(DUTM, pageNumber, memAddress)
    time.sleep(0.1)
    Raw_txLOS = myTest.msa_byte_read(DUTM, pageNumber, memAddress)

    memAddress = 137   # TX LOL
    myTest.msa_byte_read(DUTM, pageNumber, memAddress)
    time.sleep(0.1)
    Raw_txLOL = myTest.msa_byte_read(DUTM, pageNumber, memAddress)

    txlos_list = []
    txlol_list = []
    for lane in range(8):
        txlos_list.append(bool(Raw_txLOS & (1<<lane))*1)
        txlol_list.append(bool(Raw_txLOL & (1<<lane))*1)

    return txlos_list, txlol_list

def get_rx_los_lol_MSA(DUTM):
    myTest.SetPassword(DUTM)
    pageNumber = 0x11

    memAddress = 147   # RX LOS
    myTest.msa_byte_read(DUTM, pageNumber, memAddress)
    time.sleep(0.1)
    Raw_rxLOS = myTest.msa_byte_read(DUTM, pageNumber, memAddress)

    memAddress = 148   # RX LOL
    myTest.msa_byte_read(DUTM, pageNumber, memAddress)
    time.sleep(0.1)
    Raw_rxLOL = myTest.msa_byte_read(DUTM, pageNumber, memAddress)

    rxlos_list = []
    rxlol_list = []
    for lane in range(8):
        rxlos_list.append(bool(Raw_rxLOS & (1<<lane))*1)
        rxlol_list.append(bool(Raw_rxLOL & (1<<lane))*1)

    return rxlos_list, rxlol_list

def enter_eng_mode_2x200():
    myTest.DUTreset(DUT)
    print 'wait 20s'
    time.sleep(20)
    table=129
    offset = 0
    data=0x7CE0
    myTest.HCI_write_byte(myio_dut_1, table, offset, [data])
    time.sleep(0.1)
    readback =myTest.HCI_read_byte(myio_dut_1, table, offset)
    print '====================='
    print hex(readback)

def get_Vea_2x200(lanelist,DUTM=DUT):
    EA_BIAS_DAC_READ_list=[]
    Vea_V_list=[]
    for lane in lanelist:
        EA_BIAS_DAC_READ,Vea_V=EA_BIAS_DAC_read(lane,DUTM)
        EA_BIAS_DAC_READ_list.append(EA_BIAS_DAC_READ)
        Vea_V_list.append(Vea_V)
    return EA_BIAS_DAC_READ_list,Vea_V_list

def write_vea_eng_mode_2x200(lane,Vea_V_tgt,DUTM=DUT):
    lane = int(lane)
    if lane not in range(1, 9):
        raise Exception('lane not in 1-8')
    lane -= 1

    table=129
    offset = 0
    readback = myTest.HCI_read_byte(myio_dut_1,table,offset)

    if readback != 0x7CE0:
        raise Exception('Not under engineering mode')
    else:
        print 'Module under engineering mode'
    Vea_V_tgt_DAC = float(Vea_V_tgt)/(-5)*4096
    Vea_V_tgt_DAC_roundup = int(round(Vea_V_tgt_DAC))


    table = 173
    base = 80
    addr = base+lane*2
    data = Vea_V_tgt_DAC_roundup
    myTest.HCI_write_byte(myio_dut_1,table,addr, [data])
    time.sleep(0.1)
    EA_BIAS_DAC_READ,Vea_V = EA_BIAS_DAC_read(lane+1)
    return EA_BIAS_DAC_READ,Vea_V


def prompt_message(message):
    message = str(message)
    Test_lib.ShowInfo(message)


def EA_BIAS_DAC_read(lane,DUTM=DUT):
    lane = int(lane)
    if lane not in range(1, 9):
        raise Exception('lane not in 1-8')
    lane -= 1
    myTest.SetPassword(DUTM)
    table = 173
    base = 112

    addr =base+lane*2

    temp1 = myTest.HCI_read_byte(myio_dut_1, table, addr)
    EA_BIAS_DAC_READ = temp1>>4

    Vea_V = float(EA_BIAS_DAC_READ)/4096*(-5)
    return EA_BIAS_DAC_READ,Vea_V


# def TDECQ_result_overshoot_debug(DCA, OCH_scpi, TDECQ_fn_scpi, tdecq_max=False):
#     chscpi = OCH_scpi
#     fnscpi = TDECQ_fn_scpi
#     DCA.Write(':MEAS:EYE:APOW:SOUR', chscpi)
#     avp = float(DCA.GPIBQuery(':MEAS:EYE:APOW?'))
#     DCA.Write(':MEAS:EYE:TTIM:SOUR', fnscpi)
#     t_transition_ps = float(DCA.GPIBQuery(':MEAS:EYE:TTIM?'))/1e-12
#     DCA.Write(':MEAS:EYE:NMAR:SOUR', fnscpi)
#     nmar_uW = float(DCA.GPIBQuery(':MEAS:EYE:NMAR?'))/1e-6
#     DCA.Write(':MEAS:EYE:PAM:LIN:SOUR', fnscpi)
#     DCA.GPIBWrite(':MEAS:EYE:PAM:LIN:DEF RLMA120')
#     rlm = float(DCA.GPIBQuery(':MEAS:EYE:PAM:LIN?'))
#     DCA.Write(':MEAS:EYE:OER:SOUR', fnscpi)
#     DCA.GPIBWrite(':MEAS:EYE:OER:UNIT DEC')
#     oER = float(DCA.GPIBQuery(':MEAS:EYE:OER?'))
#     DCA.Write(':MEAS:EYE:CEQ:SOUR', fnscpi)
#     ceq = DCA.GPIBQuery(':MEAS:EYE:CEQ?')
#     DCA.Write(':MEAS:EYE:TDEQ:SOUR', fnscpi)
#
#
#     tdecq = float(DCA.GPIBQuery(':MEAS:EYE:TDEQ?'))
#     if tdecq_max:
#         tdecq = float(DCA.GPIBQuery(':MEAS:EYE:TDEQ:MAX?'))
#
#     try:
#         DCA.Write(':MEAS:EYE:VEOP:SOUR', fnscpi)
#         veo = float(DCA.GPIBQuery(':MEAS:EYE:VEOP?'))
#     except:
#         veo = 'na'
#
#     over_under_hitratio_list = [1e-4,1e-3,1e-2]
#
#     undershoot_list=[]
#     overshoot_list=[]
#     for over_under_hitratio in over_under_hitratio_list:
#         try:
#             DCA.Write(':MEAS:EYE:PAM:UND:SOUR', chscpi)
#             DCA.Write(':MEAS:EYE:PAM:UND:THR', str(over_under_hitratio))
#             undershoot_list.append(float(DCA.GPIBQuery(':MEAS:EYE:PAM:UND?')))
#             DCA.Write(':MEAS:EYE:PAM:OVER:SOUR', chscpi)
#             DCA.Write(':MEAS:EYE:PAM:OVER:THR', str(over_under_hitratio))
#             overshoot_list.append(float(DCA.GPIBQuery(':MEAS:EYE:PAM:OVER?')))
#         except:
#             undershoot_list.append('na')
#             overshoot_list.append('na')
#     undershoot_1e4,undershoot_1e3,undershoot_1e2=undershoot_list
#     overshoot_1e4,overshoot_1e3,overshoot_1e2=overshoot_list
#     return avp,t_transition_ps,nmar_uW,rlm,oER,ceq,tdecq,veo,undershoot_1e4,undershoot_1e3,undershoot_1e2,overshoot_1e4,overshoot_1e3,overshoot_1e2



#=====================Helper Functions End=====================#

#######################################################################
myTest.SetPassword(dut_0)
myTest.SetPassword(dut_1)

fwRevDUT_0 = ''
fwRevDUT_1 = ''
fwver_offsetlist = [16, 18, 20, 22, 24]
table = 255

for offset in fwver_offsetlist:
    try:
        fwRevDUT_0 += '%0x-' % (myTest.HCI_read_byte(myio_dut_0, table, offset))
    except:
        fwRevDUT_0 = 'NA'
    try:
        fwRevDUT_1 += '%0x-' % (myTest.HCI_read_byte(myio_dut_1, table, offset))
    except:
        fwRevDUT_1 = 'NA'
#debug
#fwRevDUT_1 = 'NA'

fwRevDUT_0 = fwRevDUT_0[:-1].ToUpper()
fwRevDUT_1 = fwRevDUT_1[:-1].ToUpper()

DUT_0_SN = 'NA'
DUT_1_SN = 'NA'
DUT_0_SN = myTest.getQSFPDD_SN(dut_0)
DUT_1_SN = myTest.getQSFPDD_SN(dut_1)
#debug
#DUT_1_SN = 'NA'

print ('DUT 0 SN: %s' % (DUT_0_SN))
print ('DUT 0 FW Rev: %s' % (fwRevDUT_0))
print ('DUT 1 SN: %s' % (DUT_1_SN))
print ('DUT 1 FW Rev: %s' % (fwRevDUT_1))

#######################################################################




ATT_list = [ATT1, ATT2]

#==============set by power scan step, start, stop, overload level, offset starts==============#
att_start = 0
att_stop = 10.1
att_step = 1
#att_overload_list = [4.5, 4.5, 4.5, 4.5]
#offset_list = [-0.41,-0.63,-0.24,-1.1]

att_step = -abs(att_step)*int(att_start>att_stop)+abs(att_step)*int(att_start<att_stop)
targetAtt_list = np.arange(att_start,att_stop,att_step).tolist()

list_lane = [1,2,3,4,5,6,7,8]
#EDlist_lane = [ED1, ED2, ED3, ED4, ED5, ED6, ED7, ED8]
EDlist_lane = [ED21, ED22, ED23, ED24, ED25, ED26, ED27, ED28]
gating = 5

# er_list = [3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5]
Vea_offset_list = [0,-0.2,-0.175,-0.15,-0.125,-0.1,-0.075,-0.05,-0.025,0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2]
#Vea_offset_list = [0,-0.2,-0.175]

Note = 'Vea_scan'

columns = {}

path = r'Y:\Engineering\40G\100G-Development\FTCD4715(2x200G_CGR4+_OSFP)\measurements\Vea_scan\TP2\result\valid'
extension = 'csv'
os.chdir(path)
csvfile_list = glob.glob('*.{}'.format(extension))
print(csvfile_list)

filename = ''

for csvfile in csvfile_list:
    if (DUT_1_SN in csvfile):
        filename = r'%s\%s'%(path,csvfile)

print filename

if filename == '':
    raise Exception('Wrong module inserted!!!')

#filename = r'Y:\Engineering\40G\100G-Development\FTCD4715(2x200G_CGR4+_OSFP)\measurements\Vea_scan\TP2\result\valid\Result_X67AK7Q_01-05-2022-19-35-50.csv' #TP2 data filepath


with open(filename) as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items(): # go over each column name and value
#                print '(k, v) = ', (k, v)
            try:
                columns[k].append(v) # append the value into the appropriate list
            except KeyError:
                columns[k] = [v]

er_list = columns['OuterER']
print er_list

def runtest():
    PS_DUT.SetOutput(1, 3.3, 15)
    ATT1.OpenShutter(1)
    ATT2.OpenShutter(1)
    ATT1.SetAttenuation(0.5)
    ATT2.SetAttenuation(0.5)
    print '====================BEGIN====================='
    
    PGlist_TEC = [PG1, PG2, PG3, PG4, PG5, PG6, PG7, PG8]
    #PGlist_TEC = [PG21, PG22, PG23, PG24, PG25, PG26, PG27, PG28]

    datarate_list = [25,50,100]
    baudrate_list = [25,56,100]

    #choose from 25,50,100
    datarate2set_die0 = 50
    datarate2set_die1 = 50
    pattern2set = DataPattern.PRBS31
    #pattern2set = DataPattern.PRBS9_5
    #pattern2set = DataPattern.PRBS15
    #pattern2set = DataPattern.SSPRQ
    pgrate2set_die0 = baudrate_list[datarate_list.index(datarate2set_die0)]
    pgrate2set_die1 = baudrate_list[datarate_list.index(datarate2set_die1)]
    PGlist_TEC[0].PGInitialize()

    PGlist_TEC[0].PGSetRate(pgrate2set_die0)
    PGlist_TEC[4].PGSetRate(pgrate2set_die1)

    for PGn in PGlist_TEC:
        PGn.PGSetPattern(pattern2set)
        PGn.EnablePattern(1)
    
    
    #PGlist_TEC = [PG1, PG2, PG3, PG4, PG5, PG6, PG7, PG8]
    PGlist_TEC = [PG21, PG22, PG23, PG24, PG25, PG26, PG27, PG28]

    datarate_list = [25,50,100]
    baudrate_list = [25,56,100]

    #choose from 25,50,100
    datarate2set_die0 = 50
    datarate2set_die1 = 50
    pattern2set = DataPattern.PRBS31
    #pattern2set = DataPattern.PRBS9_5
    #pattern2set = DataPattern.PRBS15
    #pattern2set = DataPattern.SSPRQ
    pgrate2set_die0 = baudrate_list[datarate_list.index(datarate2set_die0)]
    pgrate2set_die1 = baudrate_list[datarate_list.index(datarate2set_die1)]
    PGlist_TEC[0].PGInitialize()

    PGlist_TEC[0].PGSetRate(pgrate2set_die0)
    PGlist_TEC[4].PGSetRate(pgrate2set_die1)

    for PGn in PGlist_TEC:
        PGn.PGSetPattern(pattern2set)
        PGn.EnablePattern(1)
    
    
    TC1.SetTemperature(41)
    time.sleep(500)
    
    myTest.SetPassword(dut_0)
    myTest.SetPassword(dut_1)

    csvfolder = r'\\sny-netapp-02\Department\Engineering\40G\100G-Development\FTCD4715(2x200G_CGR4+_OSFP)\measurements\Vea_scan\BER'

    #Create Data File for Waterfall Data
    timestamp = myTest.timestr()
    csvname = 'Result_%s_%s_%s' % (DUT_0_SN, DUT_1_SN, timestamp)
    csvname_wf = r'%s\%s.csv'%(csvfolder, csvname)
    csvheader_common = ['DUTSN', 'FW_Revision', 'Note']

    csvheader_data = ['Lane', 'Atteunuation','Vea_offset', 'outerER', 'outerOMA','TEMP_TEC', 'MSA Temperature', 'MSA Vcc', 'LASER_TEMP_1', 'LASER_TEMP_2', 'Tx_Bias', 'Tx_Pwr', 'RxPower_MSA', 'RxLOS', 'RxLOL', 'TxLOS', 'TxLOL','EA_BIAS_DAC', 'Vea_V', 'RAW_BER', 'BER', 'BitError', 'TotalBit', 'IsSync']

    csvheader = csvheader_common + csvheader_data
    with open(csvname_wf, 'wb') as csv_file:
        headers = csvheader
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
    csv_file.close()

    er_idx = 0
    
    for vea_idx, Vea_offset in enumerate(Vea_offset_list):
        er_list_tgt = er_list[vea_idx*8:vea_idx*8+8]
        initial_flag = (Vea_offset == 0)
        if initial_flag:
            enter_eng_mode_2x200()
            EA_BIAS_DAC_READ_list_0,Vea_V_list_0=get_Vea_2x200(list_lane)

        for row_idx, lane in enumerate(list_lane):
            Vea_V_0 = Vea_V_list_0[row_idx]
            Vea_V_tgt = Vea_V_0 + Vea_offset
            EA_BIAS_DAC_READ,Vea_V=write_vea_eng_mode_2x200(lane, Vea_V_tgt)
        
        
        for targetAtt in targetAtt_list:
            for ind, ATT in enumerate(ATT_list):
                # ATT.SetAttenuation(targetatt)
                att_read = setatt(targetAtt, ATT)
                time.sleep(0.1)
                ATT.OpenShutter(1)
                time.sleep(0.1)
            
            print ('Reading BER at %s dB, %s V' % (targetAtt, Vea_offset))
            BER_list, BitError_list, TotalBit_list, IsSync_list = readBERonBoardED(list_lane, EDlist_lane, gating)

            print '---------------------------------------'
            print 'BER_list = ', BER_list
            print 'BitError_list = ', BitError_list
            print 'TotalBit_list = ', TotalBit_list
            print 'IsSync_list = ', IsSync_list
            print '---------------------------------------'

            txlos_list, txlol_list = get_tx_los_lol_MSA(dut_0)
            rxlos_list, rxlol_list = get_rx_los_lol_MSA(dut_0)

#            currentatt = ATT_list[rowidx].ReadAttenuation()
            # currentpwr = offsetlist[rowidx]-targetatt
            # currentpwr = targetpow


            msa_temp = myTest.TEMP_MSA(dut_0)
            vcc = myTest.VCC_MSA(dut_0)
            try:
                laser_temp1, laser_temp2 = myTest.TEC_TEMP_MSA(dut_0)
            except:
                laser_temp1, laser_temp2 = 'NA', 'NA'

            #er_idx = 0
            for row_idx, lane in enumerate(list_lane):
                try:
                    rx_pwr = myTest.RX_PWR_MSA(lane, dut_0)
                except:
                    rx_pwr = 'NA'

                try:
                   oER = float(er_list_tgt[row_idx])
                   # secq = secq_list[rowidx]
                   oOMA = Test_algo_lib.pwr_to_oma(rx_pwr, oER)
                except:
                   oER = 'NA'
                   # secq = 'NA'
                   oOMA = 'NA'
                #er_idx = er_idx +1
                TxBias = myTest.bias_MSA(list_lane[row_idx], dut_0)
                TxPwr = myTest.TX_PWR_MSA(list_lane[row_idx], dut_0)

                EA_BIAS_DAC_READ,Vea_V=EA_BIAS_DAC_read(lane,DUT)

                if lane < 5:
                    currentatt = ATT_list[0].ReadAttenuation()
                else:
                    currentatt = ATT_list[1].ReadAttenuation()
                
                rxlol = rxlol_list[row_idx]
                isSync = IsSync_list[row_idx]
                bitCount = TotalBit_list[row_idx]
                rawber = BER_list[row_idx]
                errCount = BitError_list[row_idx]
                
                if (rxlol) or (not isSync) or (bitCount <= 0):
                    ber = 0.5
                elif (not rxlol) and (isSync) and (bitCount > 0) and (errCount == 0):
                    ber = 1e-12
                else:
                    ber = rawber

                csvdata_data = [lane, currentatt, Vea_offset, oER, oOMA, str(TC1.GetTemperature()), msa_temp, vcc, laser_temp1, laser_temp2, TxBias, TxPwr, rx_pwr, rxlos_list[row_idx], rxlol, txlos_list[row_idx], txlol_list[row_idx], EA_BIAS_DAC_READ, Vea_V, rawber, ber, errCount, bitCount, isSync]


                csvdata_common = [DUT_1_SN, fwRevDUT_1, Note]
                csvdata = csvdata_common + csvdata_data
                with open(csvname_wf, 'ab') as f:
                    writer = csv.writer(f)
                    writer.writerow(csvdata)
                f.close()

                er_idx = er_idx +1

if __name__ == '__main__':
    runtest()
    prompt_message('Test Done!')
#    1