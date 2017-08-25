# In-Order Traversal - visit (here, print) the (1) left branch, (2) current node, (3) right branch. This visits the nodes of a BST in ascending order.

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print node.data
        in_order_traversal(node.right)


# Pre-Order Traversal - visit the (1) current node, (2) child nodes (probably left to right)

def pre_order_traversal(node):
    if node:
        print node.data
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


# Post-Order Traversal - visit the current node after its child nodes. The root is always the last node visited

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print node.data