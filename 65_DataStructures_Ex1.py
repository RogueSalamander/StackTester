'''
Reverse the string "yesterday" using a stack and 
print it. 
You should use a class called Stack. 
You need to define a push and pop method in your 
class. 
'''


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
for c in "yesterday":
    stack.push(c)

reversed_string = ""
for i in range(len(stack.items)):
    reversed_string += stack.pop(i)

print(reversed_string)