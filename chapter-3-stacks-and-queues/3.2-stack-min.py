""" 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time. """

# You would want to implement your Stack from a custom LinkedList class where each Node has a next_min property and the LinkedList has a min property so that, when a node that is the minimum is pushed from the stack, it would update the stack min. Take into account how you deal with doubles.

