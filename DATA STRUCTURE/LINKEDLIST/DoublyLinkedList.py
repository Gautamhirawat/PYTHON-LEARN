class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
doubly_list = DoublyLinkedList()
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    doubly_list.insert(data)

print("The doubly linked list is:")
doubly_list.display()
