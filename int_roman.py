num = int(input("Enter the number:"))
l = ["I","IV", "V", "IX","X","XL","L", "XC", "C", "CD", "D", "CM", "M"]
m = [1,4,5,9,10,40, 50, 90,100, 400, 500, 900, 1000]
i =12
while(num):
    quo = num // m[i]
    num = num % m[i]
    while(quo):
        print(l[i],end="")
        quo -= 1
    i -= 1