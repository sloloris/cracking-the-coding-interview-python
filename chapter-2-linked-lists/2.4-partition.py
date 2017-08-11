""" 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x. The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions. 
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 with partition x=5
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from LL_implementation import LLNode, LinkedList

def partition(ll, x):
    partitioned = LinkedList()
    current = ll.head
    while current.next:
        if current.data >= x:
            partitioned.add(current.data)
        else:
            partitioned.insert_at_head(current.data)
        current = current.next
    if current.data >= x:
        partitioned.add(current.data)
    else:
        partitioned.insert_at_head(current.data)
    return partitioned




if __name__ == "__main__":
    ll = LinkedList()
    ll.add(3)
    ll.add(5)
    ll.add(8)
    ll.add(5)
    ll.add(10)
    ll.add(2)
    ll.add(1)

    new_ll = partition(ll, 5)
    new_ll._print() #remember that x itself can be anywhere in the second half of the output ll

