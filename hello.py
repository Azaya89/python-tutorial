def main():
    """Main function"""

    name = get_name()
    return f"Hello, {name}. You are welcome to this class."

def get_name():
    name = input("What is your name? ").title().strip()
    return name

if __name__ == "__main__":
    print(main())
