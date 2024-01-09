def main():
    size = int(input("Enter the size of the one-dimensional array: "))
    arr = [int(input(f"Element {i + 1}: ")) for i in range(size)]

    print("The entered one-dimensional array is:")
    print(arr)

if __name__ == "__main__":
    main()
