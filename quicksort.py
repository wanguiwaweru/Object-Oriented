def quickSort(arr):
    if len(arr) < 2:
        return arr

    smaller, same, greater = [], [], []

    # Select pivot
    pivot = arr[-1]

    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            same.append(i)
        elif i > pivot:
            greater.append(i)

    return quickSort(smaller) + same + quickSort(greater)

print(quickSort([8,7,1,1,0,9,2]))

from random import randint
def quickSort(arr):
    if len(arr) < 2:
        return arr

    smaller, same, greater = [], [], []

    # Select pivot
    pivot = arr[randint(0, len(arr) - 1)]

    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            same.append(i)
        elif i > pivot:
            greater.append(i)

    return quickSort(smaller) + same + quickSort(greater)

print(quickSort([8,7,1,1,0,9,2]))