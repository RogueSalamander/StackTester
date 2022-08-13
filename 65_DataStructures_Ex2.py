'''
Use a stack to create a new list with the items 
in the following list reversed: [1, 2, 3, 4, 5]. 
'''


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
numList = [1, 2, 3, 4, 5]
revStack = []
for c in numList:
    stack.push(c)

print(stack.items)

#How to go through each item on a stack?
for i in numList:
    revStack.append(stack.pop())


print(revStack)