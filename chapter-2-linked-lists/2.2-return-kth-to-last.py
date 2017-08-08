""" 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. """

from LL_implementation import LLNode, LinkedList

def kth_to_last(ll, k):
    count = 0
    current = ll.head
    k_from_curr = None
    while current.next:
        if count == k:
            k_from_curr = ll.head
        count += 1
        current = current.next
        if k_from_curr != None:
            k_from_curr = k_from_curr.next
    return k_from_curr


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)
    ll.add(9)
    ll.add(10)

    kth_el = kth_to_last(ll, 7)
    print kth_el.data