def subset(ip,output,ans):
    if len(ip) == 0:
        #ans.append(output)
        print(output)
        return
    op1 = output
    op2 = output.join(ip[0])
    ip = ip[1:]
    subset(ip,op1,ans)
    subset(ip,op2,ans)
    

out =""
ans=[]
print(subset("ab",out,ans))
print(out)