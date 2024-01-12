class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            item = self.top.data
            self.top = self.top.next
            return item
        else:
            print("Stack Underflow")
            return -1

if __name__ == "__main__":
    stack = LinkedStack()

    elements = input("Enter elements to push (space-separated): ").split()
    for element in elements:
        stack.push(int(element))

    print("Popped elements:")
    while True:
        popped = stack.pop()
        if popped == -1:
            break
        print(popped)
