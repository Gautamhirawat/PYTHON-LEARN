def main():
    size = int(input("Enter the size of the sparse array: "))
    sparse_array = [int(input(f"Element {i + 1}: ")) for i in range(size)]

    nonzero_elements = {i: value for i, value in enumerate(sparse_array) if value != 0}

    print("The entered sparse array is:")
    print({k: nonzero_elements.get(k, 0) for k in range(size)})

if __name__ == "__main__":
    main()
