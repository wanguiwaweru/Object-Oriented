def bubbleSort(arr):

    for i in range(len(arr)):

        #compare every two items in the array
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def optimizedBubble(arr):
    
    for i in range(len(arr)):
        isSorted = True
        for j in range(len(arr)-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                isSorted = False
        if isSorted:
            break
    return arr


print(bubbleSort([2,77,1,8,9]))
print(optimizedBubble([2,77,1,8,9]))
