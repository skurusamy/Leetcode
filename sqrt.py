num = int(input("Enter the number: "))
if num == 1 :
    print("1")
else:
    start = 1
    end = num
    while start < end:
        mid = (start + end) //2
        if mid * mid == num:
            ans = mid
            break
        elif mid * mid < num:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)
