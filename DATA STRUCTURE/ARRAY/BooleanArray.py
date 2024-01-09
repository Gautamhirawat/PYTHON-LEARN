def main():
    size = int(input("Enter the size of the boolean array: "))
    bool_array = [bool(int(input(f"Element {i + 1} (0 for False, 1 for True): "))) for i in range(size)]

    print("The entered boolean array is:")
    print(bool_array)

if __name__ == "__main__":
    main()
