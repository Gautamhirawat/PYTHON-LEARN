class TwoStacks:
    def __init__(self, capacity):
        self.stack = [0] * capacity
        self.top1 = -1
        self.top2 = capacity

    def push1(self, item):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack[self.top1] = item
        else:
            print("Stack 1 Overflow")

    def push2(self, item):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stack[self.top2] = item
        else:
            print("Stack 2 Overflow")

    def pop1(self):
        if self.top1 >= 0:
            item = self.stack[self.top1]
            self.top1 -= 1
            return item
        else:
            print("Stack 1 Underflow")
            return -1

    def pop2(self):
        if self.top2 < len(self.stack):
            item = self.stack[self.top2]
            self.top2 += 1
            return item
        else:
            print("Stack 2 Underflow")
            return -1

if __name__ == "__main__":
    capacity = int(input("Enter the capacity of the stacks: "))
    stack = TwoStacks(capacity)

    elements1 = input("Enter elements for stack 1 (space-separated): ").split()
    for element in elements1:
        stack.push1(int(element))

    elements2 = input("Enter elements for stack 2 (space-separated): ").split()
    for element in elements2:
        stack.push2(int(element))

    print("Popped elements from stack 1:")
    while True:
        popped = stack.pop1()
        if popped == -1:
            break
        print(popped)

    print("Popped elements from stack 2:")
    while True:
        popped = stack.pop2()
        if popped == -1:
            break
        print(popped)
