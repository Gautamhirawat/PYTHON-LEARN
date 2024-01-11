class SelfAdjustingList:
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

    def move_to_front(self, key):
        prev = None
        current = self.head
        while current is not None and current.data != key:
            prev = current
            current = current.next

        if current is not None:
            if prev is not None:
                prev.next = current.next
                current.next = self.head
                self.head = current

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
self_adjusting_list = SelfAdjustingList()
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    self_adjusting_list.insert(data)

key_to_move = int(input("Enter the key to move to the front: "))
self_adjusting_list.move_to_front(key_to_move)

print("The self-adjusting list is:")
self_adjusting_list.display()
