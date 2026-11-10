def square(n):
    return n * n


def divide(x, y):
    return round(x / y, 2)


def main():
    x = float(input())
    y = float(input())
    z = divide(x, y)
    print(f"{z:.2f}")


if __name__ == "__main__":
    main()
