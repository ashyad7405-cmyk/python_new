def main():
    n = int(input())
    print_row(n)
    

def print_row(width):
    print("?" * width)

    

main()
def main():
    print_square(3)
# for each row in square
def print_square(size):
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end='')
        print()

main()