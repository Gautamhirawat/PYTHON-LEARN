def main():
    size = int(input("Enter the size of the dynamic array: "))
    dynamic_array = [int(input(f"Element {i + 1}: ")) for i in range(size)]

    print("The entered dynamic array is:")
    print(dynamic_array)

if __name__ == "__main__":
    main()
