def main():
  x = int(input("what's x?"))

  if x%2==0:
    print("even")
  else:
    print("odd")

def even(n):
    if n%2==0:#can replace line 10,11,12,13 by return True if n%2==0 else return False or just write return n%2==0
        return True
    else:
        return False

main()