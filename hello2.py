"""def hello(to):
    print("hello, ",to)



name = input()
hello(name)"""
def main():
    x = int(input())
    print(f"{x} cube is",sq(x))

def sq(n):
    return pow(n,3)
main()