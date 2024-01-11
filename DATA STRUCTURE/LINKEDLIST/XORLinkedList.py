class XORLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.xor_next_prev = 0

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = self.Node(data)
        new_node.xor_next_prev = 0

        if self.head is None:
            self.head = new_node
        else:
            current_addr = 0
            prev_addr = 0

            current = self.head
            prev = None

            while current is not None:
                next_addr = prev_addr ^ current.xor_next_prev

                if next_addr == 0:
                    new_node.xor_next_prev = current_addr
                    current.xor_next_prev ^= (0 if prev is None else prev_addr ^ id(new_node))
                    break

                prev = current
                prev_addr = current_addr
                current_addr = next_addr
                current = self.get_object(current_addr)

    def display(self):
        current_addr = 0
        prev_addr = 0

        current = self.head
        prev = None

        while current is not None:
            print(current.data, end=" ")

            next_addr = prev_addr ^ current.xor_next_prev

            if next_addr == 0:
                break

            prev = current
            prev_addr = current_addr
            current_addr = next_addr
            current = self.get_object(current_addr)
        print()

    # Dummy method for get_object (replace with actual method to get object based on memory address)
    @staticmethod
    def get_object(address):
        return None


# Example usage:
xor_list = XORLinkedList()
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    xor_list.insert(data)

print("The XOR linked list is:")
xor_list.display()
