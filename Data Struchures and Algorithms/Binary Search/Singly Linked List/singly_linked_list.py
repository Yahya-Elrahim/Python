
# ----------- linked list ------------------
# Linked list  is an linear data structure , in which the elements are not stored at
# contiguous memory location.The element in a linked list are linked using pointers.
# Linked list consists a nodes and each node contains a value and apointer that refrence to the next node
# ----------- Application of Linked list ---------------
# 1. Tree
# 2. Graph
# 3. Stack
# 4. Queue
# 5. LRU/MRU
# 6. Hash table
# 7. non-binary trees
# e.t.c

# Linked list types
# 1. Signly linked list
# 2. Doubly linked list
# 3. Circular linked list

# A header node is a special node that is found at the beginning of the list. A list that contains this type of node,
# is called the header-linked list.
# Types of Header Linked List
#
# 1- Grounded Header Linked List : It is a list whose last node contains the NULL pointer.
# 2- Circular Header Linked List :  A list in which last node points back to the header node is called circular linked list

# ----------Implementation of Signly linked list ---------------------


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Big of notation is O(n)
    def print_list(self, head):
        current_node = head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # To get the length of linked list with while loop
    # Big of notation is O(n)
    def len(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    # To get the length of linked list using recursive function
    # Big of notation is O(n)
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    # Big of notation is O(n)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        # Big of notation is O(1)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Big of notation is O(n)
    def insert_after_node(self, previous_node, data):
        if self.head is None:
            print("Linked list is empty")
            return
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == previous_node:
                new_node.next = current_node.next
                current_node.next = new_node
                break
            current_node = current_node.next
        else:
            print("Previous node not exist in linked list")

    def swap(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def delete(self, data):

        previous = None
        current = self.head
        while current and current.data != data:
            previous = current
            current = current.next
        if not current:
            print("Data not exist in list")
            return
        # Key is th list header
        if not previous:
            self.head = current.next
            return
        else:
            previous.next = current.next
    def delete_at(self, position):
        current = self.head
        if position == 0:
            self.head = current.next
            return
        previous = None
        count = 1
        while current and count != position:
            previous = current
            current = current.next
            count += 1
        if current is None:
            print("Key not founded")
            return
        previous.next = current.next

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def merge(self, l2):

        p = self.head
        q = l2.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head







if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(1)
    l_list.append(5)
    l_list.append(7)
    l_list.append(9)
    l_list.append(10)

    l_list_2 = LinkedList()
    l_list_2.append(2)
    l_list_2.append(3)
    l_list_2.append(4)
    l_list_2.append(6)
    l_list_2.append(8)
    l_list.print_list(l_list.merge(l_list_2))


