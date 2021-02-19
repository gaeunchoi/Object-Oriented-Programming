# Stack

# Stack class
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        # Write code here!
        self.data.append(x)

    def pop(self):
        # Write code here!
        tmp = self.data.pop(-1)
        print("popping -> pop value: " + str(tmp))

    def empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)


if __name__=="__main__":
    stack = Stack()

    stack.push(1)
    print("After pushing 1:  " + str(stack))

    stack.push(2)
    print("After pushing 2:  " + str(stack))

    stack.push(50)
    print("After pushing 50:  " + str(stack))

    stack.pop()
    print("After popping:  " + str(stack))

    stack.push(5)
    print("After pushing 5:  " + str(stack))
