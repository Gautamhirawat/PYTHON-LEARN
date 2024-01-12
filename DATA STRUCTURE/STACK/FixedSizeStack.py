class FixedSizeStack:
    def __init__(self, capacity):
        self.stack = [0] * capacity
        self.top = -1

    def push(self, item):
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top >= 0:
            item = self.stack[self.top]
            self.top -= 1
            return item
        else:
            print("Stack Underflow")
            return -1

if __name__ == "__main__":
    capacity = int(input("Enter the capacity of the stack: "))
    stack = FixedSizeStack(capacity)

    elements = input("Enter elements to push (space-separated): ").split()
    for element in elements:
        stack.push(int(element))

    print("Popped elements:")
    while True:
        popped = stack.pop()
        if popped == -1:
            break
        print(popped)
