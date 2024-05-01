from lib.utils import measure_time
import time
import random



class Node:
    def __init__(self, data, parent = None):
        self.val = data
        self.left = None
        self.right = None
        self.parent = parent


    def __repr__(self) -> str:
        return f"Node({self.val} -> p{self.parent and self.parent.val or None} - {self.left}, {self.right})"



def insert_tree(root, val, parent = None):
    if not root:
        return Node(val, parent)
    
    if val < root.val:
        root.left = insert_tree(root.left, val, root)
    else:
        root.right = insert_tree(root.right, val, root)

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



def subtree_find_next(n):

    if n.right:
        cur = n.right
        while cur.left:
            cur = cur.left
        return cur
    
    if n.parent:
        prev = n
        cur = n.parent
        while cur and cur.right == prev:
            prev = cur
            cur = cur.parent

        if cur:
            return cur
        
    return None


def subtree_find_prev(n):
    if n.left:
        cur = n.left
        while cur.right:
            cur = cur.right

        return cur
    
    if n.parent:
        cur = n.parent
        prev = n
        while cur and cur.left == prev:
            prev = cur
            cur = cur.parent

        if cur:
            return cur
        
    return None
        
    


def subtree_find_first(n):

    if not n:
        return None

    while n.left:
        n = n.left

    return n
    
def subtree_find_last(n):

    if not n:
        return None
    
    while n.right:
        n = n.right

    return n

def print_tree_visual_aux(node, prefix, is_left):
    if not node:
        print("Empty tree")
        return

    if node.right:
        print_tree_visual_aux(node.right, prefix + ("│   " if is_left else "    "), False)
    
    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    if node.left:
        print_tree_visual_aux(node.left, prefix + ("    " if is_left else "│   "), True)



# Test
arr = [12, 11, 13, 5, 6, 7]
root = arr2tree(arr)
print(inorder(root))
print(root)
print_tree_visual_aux(root, "", True)

c = subtree_find_first(root)
while c:
    print(c.val)
    c = subtree_find_next(c)

c = subtree_find_last(root)
while c:
    print(c.val)
    c = subtree_find_prev(c)


# Execution time: 0.000997781753540039 seconds


arr = random.sample(range(1, 10000000), 100000)
