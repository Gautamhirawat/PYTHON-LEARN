class DynamicStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack Underflow")
            return -1

if __name__ == "__main__":
    stack = DynamicStack()

    elements = input("Enter elements to push (space-separated): ").split()
    for element in elements:
        stack.push(int(element))

    print("Popped elements:")
    while True:
        popped = stack.pop()
        if popped == -1:
            break
        print(popped)
