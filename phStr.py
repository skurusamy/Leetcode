def letterCombination(result,digit,current,index,hash):
    if index == len(digit):
        result.append(current)
        return
    letter = hash[int(digit[index])]
    for i in range(len(letter)):
         letterCombination(result,digit,current+letter[i],index+1,hash)

digit = input("Enter number: ")
result =[]
hash = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

if digit is None or len(digit) == 0:
    print("Invalid")
letterCombination(result,digit,"",0,hash)
print(result)