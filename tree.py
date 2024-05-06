from lib.utils import measure_time
import time
import random



class Node:
    def __init__(self, data, parent = None):
        self.val = data
        self.left = None
        self.right = None
        self.parent = parent
        self.size = 1
        self.max = data


    def __repr__(self) -> str:
        return f"Node({self.val} -> p{self.parent and self.parent.val or None} - {self.left}, {self.right})"



def insert_tree(root, val, parent = None):
    if not root:
        return Node(val, parent)
    
    if val < root.val:
        root.left = insert_tree(root.left, val, root)
    else:
        root.right = insert_tree(root.right, val, root)

    root.size += 1
    root.max = max(root.left and root.left.max or float('-inf'), root.right and root.right.max or float('-inf'))

    return root


def delete_tree(node, root):
    if not node or not root:
        return root
    
    if node.left:
        prev = subtree_find_prev(node)
        node.val, prev.val = prev.val, node.val
        return delete_tree(prev, root)
    elif node.right:
        next = subtree_find_next(node)
        node.val, next.val = next.val, node.val
        return delete_tree(next, root)
    else:
        if node.parent:
            if node.parent.left == node:
                node.parent.left = None
            else:
                assert node.parent.right == node
                node.parent.right = None

            while node.parent:
                node.parent.size -= 1
                node.max = max(node.left and node.left.max or float('-inf'), node.right and node.right.max or float('-inf'), node.val)
                node = node.parent
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
    
    print(prefix + ("└── " if is_left else "┌── ") + str(node.val) + '(' + str(node.size) + 'm' + str(node.max))

    if node.left:
        print_tree_visual_aux(node.left, prefix + ("    " if is_left else "│   "), True)


def get_by_index(root, i):
    if not root:
        return None

    mid = 0
    if root.left:
        mid = root.left.size

    if i == mid:
        return root
    elif i < mid:
        return get_by_index(root.left, i)
    else:
        assert i > mid
        return get_by_index(root.right, i - mid - 1)
        


# Test
arr = [12, 11, 13, 5, 6, 7]
root = arr2tree(arr)
print(inorder(root))
print(root)
print_tree_visual_aux(root, "", True)

delete_tree(root.left, root)

print_tree_visual_aux(root, "", True)



c = subtree_find_first(root)
while c:
    print(c.val)
    c = subtree_find_next(c)

c = subtree_find_last(root)
while c:
    print(c.val)
    c = subtree_find_prev(c)


print([get_by_index(root, i).val for i in range(root.size)])

# Execution time: 0.000997781753540039 seconds


arr = random.sample(range(1, 10000000), 100000)
