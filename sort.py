import random
import time
import sys
# from memory_profiler import profile
sys.setrecursionlimit(15000000) 

# @profile
def select_sort(arr):
    left = 0
    right = len(arr)

    while left < right:
        max_i = left
        for i in range(left + 1, right):
            if arr[i] > arr[max_i]:
                max_i = i
        
        arr[max_i], arr[right - 1] = arr[right - 1], arr[max_i]
        right -= 1

    return arr

def select_sort_r(arr, n = None):
    if not n:
        n = len(arr)
    
    if n <= 1:
        return
    
    max_i = 0
    for i in range(n):
        if arr[i] > arr[max_i]:
            max_i = i
    
    arr[n-1], arr[max_i] = arr[max_i], arr[n-1]

    select_sort_r(arr, n-1)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    ans = []
    left_p = 0
    right_p = 0

    while left_p < len(left) or right_p < len(right):
        if not left_p < len(left):
            ans.append(right[right_p])
            right_p += 1
            continue
        if not right_p < len(right):
            ans.append(left[left_p])
            left_p += 1
            continue

        if left[left_p] < right[right_p]:
            ans.append(left[left_p])
            left_p += 1
        else:
            ans.append(right[right_p])
            right_p += 1


    return ans



def merge_sort_r(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort_r(arr[:mid])
    right = merge_sort_r(arr[mid:])

    ans = []

    left_pos = 0
    right_pos = 0

    while left_pos < len(left) and right_pos < len(right):
        if left[left_pos] < right[right_pos]:
            ans.append(left[left_pos])
            left_pos += 1
        else:
            ans.append(right[right_pos])
            right_pos += 1

    while left_pos < len(left):
        ans.append(left[left_pos])
        left_pos += 1

    while right_pos < len(right):
        ans.append(right[right_pos])
        right_pos += 1

    return ans


def insert_sort(arr, i = 0):
    if i == len(arr):
        return
    
    for j in range(i):
        if arr[j] > arr[i]:
            arr[j], arr[j+1:i+1] = arr[i], arr[j:i]
            continue

    insert_sort(arr, i+1)


def bubble_sort(arr, i = 0):
    if i == len(arr) - 1:
        return

    for j in range(len(arr)-1, i, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

    bubble_sort(arr, i+1)


def ram_sort(arr):
    ram = []
    for n in arr:
        while len(ram) <= n:
            ram.append(None)
        ram[n] = n

    ans = []

    for n in ram:
        if n:
            ans.append(n)

    return ans




def radix_sort(arr):

    for i in range(len(arr)):
        arr[i] = (arr[i]%len(arr), arr[i]//len(arr))

    ram = [[] for _ in range(len(arr))]

    # sort my reminder
    for i in range(len(arr)):
        ram[arr[i][0]].append(arr[i])

    ans = []
    for n in ram:
        if n:
            ans.extend(n)


    ram = [[] for _ in range(len(arr))]

    # sort by divider
    for i in range(len(ans)):
        ram[ans[i][1]].append(ans[i])

    ans = []

    for n in ram:
        if n:
            ans.extend(n)

    for i in range(len(ans)):
        ans[i] = ans[i][1] * len(arr) + ans[i][0]

    return ans


def quick_sort(arr, start = None, end = None):
    if not start:
        start = 0
    if not end:
        end = len(arr)

    if end - start <= 1:
        return

    l = start
    r = end - 2
    p = end - 1


    while True:
        
        while l < p and arr[l] <= arr[p]:
            l += 1

        while r > l and arr[r] > arr[p]:
            r -= 1

        if l == p:
            break

        if l == r:
            arr[l], arr[p] = arr[p], arr[l]
            break

        arr[l], arr[r] = arr[r], arr[l]

        
    quick_sort(arr, start, l)
    quick_sort(arr, l+1, end)

    



def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    return result



# Generate a random list of numbers
numbers = random.sample(range(1, 100), 10)

# Print the unsorted list
print("Unsorted list:", numbers)

quick_sort(numbers)

# Print the sorted list
print("Sorted list:", numbers)


# Generate a random list of numbers
numbers = random.sample(range(1, 100000000), 10000)

# Sort the list
# numbers.sort()
# select_sort_r(numbers)
# numbers = merge_sort(numbers)

measure_time(select_sort_r, numbers)
measure_time(select_sort, numbers)
numbers = measure_time(merge_sort_r, numbers)
measure_time(insert_sort, numbers)
measure_time(bubble_sort, numbers)
measure_time(ram_sort, numbers)
measure_time(radix_sort, numbers)
measure_time(quick_sort, numbers)