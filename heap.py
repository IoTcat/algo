from lib.utils import measure_time
import time
import random
import heapq





def heap_findMax(arr):
    return len(arr) > 0 and arr[0] or None


def heap_parentI(i):
    return (i-1)>>1

def heap_childLeftI(i):
    return (i<<1)+1

def heap_childRight(i):
    return (i<<1)+2

def heap_heapifyUp(arr, i):
    if i <= 0:
        return
    parentI = heap_parentI(i)
    if arr[parentI] < arr[i]:
        arr[parentI], arr[i] = arr[i], arr[parentI]
        heap_heapifyUp(arr, parentI)

def heap_insert(arr, v):
    arr.append(v)
    heap_heapifyUp(arr, len(arr)-1)


def heap_heapifyDown(arr, i, l = None):

    if not l:
        l = len(arr)


    if i > l - 1:
        return

    childLeftI = heap_childLeftI(i)
    childRightI = childLeftI + 1

    if not childLeftI < l:
        return 
    
    if not childRightI < l:
        if arr[childLeftI] > arr[i]:
            arr[childLeftI], arr[i] = arr[i], arr[childLeftI]
        return
    
    if arr[childLeftI] > arr[childRightI]:
        if arr[childLeftI] > arr[i]:
            arr[childLeftI], arr[i] = arr[i], arr[childLeftI]
            heap_heapifyDown(arr, childLeftI, l)

    else:
        if arr[childRightI] > arr[i]:
            arr[childRightI], arr[i] = arr[i], arr[childRightI]
            heap_heapifyDown(arr, childRightI, l)



def heap_pop(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    res = arr.pop()
    heap_heapifyDown(arr, 0)
    return res


def heap_build(arr):
    for i in range(len(arr)-1, -1, -1):
        heap_heapifyDown(arr, i)

    return arr


def heap_sort(arr):
    for i in range(len(arr)):
        heap_heapifyUp(arr, i)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_heapifyDown(arr, 0, i)




def heap_draw_tree_with_proper_spacing(arr):
    n = len(arr)
    h = 0
    while (1 << h) < n:
        h += 1
    h -= 1

    for i in range(h+1):
        print(' ' * (2 ** (h-i) - 1), end = '')
        for j in range(2 ** i):
            idx = 2 ** i + j - 1
            if idx < n:
                print(arr[idx], end = ' ' * (2 ** (h-i+1) - 1))
        print()

# Test
arr = [random.randint(1, 20) for _ in range(10)]

print(arr)
heap_sort(arr)
print(arr)

arr = [random.randint(1, 20) for _ in range(10)]

heap_draw_tree_with_proper_spacing(arr)

heap = []

# for a in arr:
#     heap_insert(heap, a)
heap = heap_build(arr)

heap_draw_tree_with_proper_spacing(heap)

print(heap_findMax(heap))

print(heap_pop(heap))

heap_draw_tree_with_proper_spacing(heap)