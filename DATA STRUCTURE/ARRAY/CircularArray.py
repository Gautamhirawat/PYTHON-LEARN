def main():
    size = int(input("Enter the size of the circular array: "))
    circular_array = [int(input(f"Element {i + 1}: ")) for i in range(size)]

    print("The entered circular array is:")
    start_index = int(input("Enter the start index for circular display: "))
    
    for i in range(size):
        index = (start_index + i) % size
        print(circular_array[index], end=" ")

if __name__ == "__main__":
    main()
