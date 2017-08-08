""" 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed? """

from LL_implementation import LLNode, LinkedList

def remove_dups(ll):
    visited = set()
    visited.add(ll.head.data)
    node = ll.head
    while node.next:
        if node.next.data in visited:
            node.next = node.next.next
            continue
        else:
            visited.add(node.next.data)
            if node.next:
                node = node.next
            else:
                break
    return ll


if __name__ == "__main__":
    test_ll = LinkedList()
    test_ll.add(5)
    test_ll.add(6)
    test_ll.add(8)
    test_ll.add(3)
    test_ll.add(6)
    test_ll.add(3)
    test_ll.add(2)
    test_ll_2 = LinkedList()
    test_ll_2.add(1)
    new_test_ll = remove_dups(test_ll)
    new_test_ll_2 = remove_dups(test_ll_2)