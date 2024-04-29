from lib.utils import measure_time
import time
import random



class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node({self.val} -> {self.left}, {self.right})"



def insert_tree(root, val):
    if not root:
        return Node(val)
    
    if val < root.val:
        root.left = insert_tree(root.left, val)
    else:
        root.right = insert_tree(root.right, val)

    return root


def arr2tree(arr):
    root = None
    for n in arr:
        root = insert_tree(root, n)

    return root

def inorder(root):
    if not root:
        return []
    
    return inorder(root.left) + [root.val] + inorder(root.right)




# Test
arr = [12, 11, 13, 5, 6, 7]
root = arr2tree(arr)
print(inorder(root))
# Execution time: 0.000997781753540039 seconds


arr = random.sample(range(1, 10000000), 100000)
