""" 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node. 

EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

"""
from LL_implementation import LLNode, LinkedList

def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next
    return 


if __name__ == "__main__":
    ll = LinkedList()
    ll.add('a')
    ll.add('b')
    ll.add('c')
    ll.add('d')
    ll.add('e')
    ll.add('f')

    node_c = ll.search('c')
    delete_middle_node(node_c)

