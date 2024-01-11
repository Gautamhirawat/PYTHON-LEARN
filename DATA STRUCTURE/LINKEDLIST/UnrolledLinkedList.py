class UnrolledLinkedList:
    class Node:
        def __init__(self, capacity):
            self.capacity = capacity
            self.size = 0
            self.elements = [None] * capacity
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = self.Node(3)  # Adjust the capacity as needed
            self.head.elements[0] = data
            self.head.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            if current.size < current.capacity:
                current.elements[current.size] = data
                current.size += 1
            else:
                new_node = self.Node(3)  # Adjust the capacity as needed
                new_node.elements[0] = data
                new_node.size += 1
                current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            for i in range(current.size):
                print(current.elements[i], end=" ")
            current = current.next
        print()


# Example usage:
unrolled_list = UnrolledLinkedList()
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    unrolled_list.insert(data)

print("The unrolled linked list is:")
unrolled_list.display()
