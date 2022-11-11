def mergeSort(arr):
    if len(arr) > 1:

        # mid is the point where the array is divided into two subarrays
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        # Sort the two halves
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # Until we reach either end of either left or right, pick larger among
        # elements left and right and place them in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # When we run out of elements in either left or right,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

array = [6, 5, 12, 9, 1]
print(mergeSort(array)) 