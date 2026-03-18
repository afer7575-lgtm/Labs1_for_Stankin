from typing import List
from decor_time import decor_timer

@decor_timer
def first_el(arr: List): # O(1)
    return arr[0]

@decor_timer
def binary_search(arr, target):# O(log(n))
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Элемент найден
        elif arr[mid] < target:
            low = mid + 1  # Ищем в правой половине
        else:
            high = mid - 1  # Ищем в левой половине
    return -1  # Элемент не найден

@decor_timer
def linear_search(arr: List, search_el): # 0(n)
    for i in range(len(arr)):
        if arr[i] == search_el:
            return i
    return -1

@decor_timer
def find_min(arr: List):# O(n)
    min = arr[0]
    for el in arr[1:]:
        if el < min: min = el
    return el

@decor_timer
def buble_sort(arr:List):# O(n^2)
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not(swap):
            break
    return arr
