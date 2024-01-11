class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
singly_list = SinglyLinkedList()
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    singly_list.insert(data)

print("The singly linked list is:")
singly_list.display()
