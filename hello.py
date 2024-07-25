def main():
    """Main function that runs the file."""

    name = get_name()
    return f"Hello, {name}. You are welcome to this class."

def get_name():
    name = input("What is your name? ").title().strip()
    return name

if __name__ == "__main__":
    print(main())

# git init, status, add, commit (-m or -am), log, log --oneline, revert, reset (--soft, --hard), rm --cached, restore
