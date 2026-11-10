def hello(name="world"):
    name = name.strip() if isinstance(name, str) else ""
    if not name:
        name = "world"
    return f"hello, {name}"


def main():
    name = input("what's ur name?").strip()
    print(hello(name))


if __name__ == "__main__":
    main()

  