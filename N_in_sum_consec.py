'''
Express N in number of consecutive numbers
eg 10 -> 1 2 3 4
100 ->18 19 20 21 22 or 9 10 11 12 13 14 15 16 
it is an ap
a+ (a+1) + (a+2) +......+(a+n) = N
last - first                        a+n+a
------------ * n = N ========>      ----- * n = N =====> (2an + n^2)/2 = N
     2                                  2
 we need to find a 
 the formula becomes
 (2N +n - n^2) /2n --->numerator should be positive -->thats the while loop
'''

N = 100
count =0
n = 2 # sequence should have atlease 2 numbers
while (2 * N + n - (n**2) > 0):
    a = (2 * N + n -(n**2)) / (2 *n)
    if(a - int(a) == 0): #no decimal point
        count = count+1
    n += 1
print(count)
