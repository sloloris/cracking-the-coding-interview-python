""" 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. 
EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""
from LL_implementation import LLNode, LinkedList

# Can you assume both numbers have the same number of digits?

def sum_lists(ll1,ll2):
    node1 = ll1.head
    node2 = ll2.head
    list_sum = 0
    digit = 0.1
    while node1:
        digit *= 10
        list_sum += (node1.data + node2.data) * digit
        node1 = node1.next
        node2 = node2.next
    while list_sum > 0:
        remainder = list_sum % digit
        




if __name__ == "__main__":
    print "nothing yet"