class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        current = self.head
        if current.data == key:
            if not current.next:
                self.head = None
                return
            else:
                nxt = current.next
                current.next = None
                nxt.prev = None
                self.head = nxt
                return

        while current:
            if current.data == key:
                if not current.next:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    return
                else:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    return
            current = current.next
        print("Element not exist in the list")

    def insert_after(self, key, data):

        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                if not current.next:
                    current.next = new_node
                    new_node.prev = current
                    return
                else:
                    nxt = current.next
                    current.next = new_node
                    new_node.prev = current
                    new_node.next = nxt
                    nxt.prev = new_node
                    return
            current = current.next










if __name__ == '__main__':
    dlList = DoublyLinkedList()
    dlList.append(1)
    dlList.append(2)
    dlList.append(4)
    dlList.append(5)
    dlList.insert_after(5, 6)

    dlList.print_list()
