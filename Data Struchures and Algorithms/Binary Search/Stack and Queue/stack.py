class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def push(self, data):
        new_item = Node(data)
        if self.is_empty():
            self.head = new_item
        else:
            new_item.next = self.head
            self.head = new_item
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next





if __name__ == '__main__':
    MyStack = Stack()

    MyStack.push(11)
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)

    # Display stack elements
    MyStack.print_stack()

    # Print top element of stack
    print("\nTop element is ", MyStack.peek())

    # Delete top elements of stack
    MyStack.pop()
    MyStack.pop()

    # Display stack elements
    MyStack.print_stack()

    # Print top element of stack
    print("\nTop element is ", MyStack.peek())
