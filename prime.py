n = int(input("Enter any num"))
if n<2:
    print("not a prime")
else:
    for i in range (2,n):
        if (n%i==0):
            print("not a prime")
            break
    else:
        print("num is prime")

    