def fabo(m):
    if m==0 or m==1:
        return 1
    elif m<0:
        print("invalid number")

    else:
        return fabo(m-1) + fabo(m-2)

m = int(input("enter the value of m?"))
print(fabo(m))