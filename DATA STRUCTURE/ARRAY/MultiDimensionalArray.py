def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    
    matrix = [[int(input(f"Element at position [{i}][{j}]: ")) for j in range(columns)] for i in range(rows)]

    print("The entered multi-dimensional array is:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
