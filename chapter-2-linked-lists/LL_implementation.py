# Implement a Linked List from scratch with an add, remove, & print method. Should contain self.data & self.next.



class LLNode(object):
    " Node in a linked list. "

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_next(self, next_node):
        self.next = next_node


class LinkedList(object):
    " Self-implemented linked-list class. "

    def __init__(self, head=None):
        " Head parameter must be LLNode object. "
        self.head = head
        self.tail = None

    def insert_at_head(self, node_data):
        " Inserts node at beginning of list. Please note that it passes node data and not a node itself. "
        new_node = LLNode(node_data)
        new_node.set_next(self.head)
        # if new_node.next == None:
        #     self.tail = new_node
        self.head = new_node

    def add(self, node_data):
        if self.head == None:
            new_node = LLNode(node_data)
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new_node = LLNode(node_data)
            current.next = new_node
        return

    def remove(self, node_data):
        current = self.head
        while current.data != node_data:
            previous = current
            current = current.next
        if current is None:
            raise ValueError("Data not found.")
        previous.set_next(current.next)


    def search(self, data):
        current = self.head
        while current.data is not data:
            current = current.next
        if current is None:
            raise ValueError("Data not found.")
        return current

    def _print(self):
        current = self.head
        while current != None:
            print current.data
            current = current.next


# starter list for testing
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)

def remove_k_from_list(l, k): # works
    head = l 
    while head.data == k:
        head = l.next
    node = head
    while node.next is not None:
        if node.next.data == k:
            node.next = node.next.next
            node = node.next
        else:
            node = node.next
            
    return head

