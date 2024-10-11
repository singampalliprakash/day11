num=int(input("enter the number:"))
if num>1:
    for i in range(2,(num//2)+1):
        if (num%i)==0:
            print("it is not a prime number")
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")