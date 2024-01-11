import random

class SkipList:
    class Node:
        def __init__(self, data, level):
            self.data = data
            self.forward = [None] * (level + 1)

    def __init__(self, max_level):
        self.max_level = max_level
        self.header = self.Node(None, max_level)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, data):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].data < data:
                current = current.forward[i]
            update[i] = current

        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level

        new_node = self.Node(data, level)

        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def display(self):
        for i in range(self.level + 1):
            node = self.header.forward[i]
            print(f"Level {i}: ", end="")
            while node:
                print(node.data, end=" ")
                node = node.forward[i]
            print()


# Example usage:
skip_list = SkipList(max_level=4)
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    skip_list.insert(data)

print("The skip list is:")
skip_list.display()
