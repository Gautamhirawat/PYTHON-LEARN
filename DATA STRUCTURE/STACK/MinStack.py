class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()
            return item
        else:
            print("Stack Underflow")
            return -1

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print("MinStack is empty")
            return -1

if __name__ == "__main__":
    stack = MinStack()

    elements = input("Enter elements to push (space-separated): ").split()
    for element in elements:
        stack.push(int(element))

    print("Popped elements:")
    while True:
        popped = stack.pop()
        if popped == -1:
            break
        print(popped)

    print("Minimum element:", stack.get_min())
