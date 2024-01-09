def main():
    rows = int(input("Enter the number of rows: "))
    
    jagged_array = []
    for i in range(rows):
        row_size = int(input(f"Enter the number of columns for row {i + 1}: "))
        row = [int(input(f"Element {j + 1}: ")) for j in range(row_size)]
        jagged_array.append(row)

    print("The entered jagged array is:")
    for row in jagged_array:
        print(row)

if __name__ == "__main__":
    main()
