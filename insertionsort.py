def insertion(arr):
    #loop from first to last element
    for i in range(1,len(arr)):
        
        #initialize key as current element
        key = arr[i]
        #initialize variable that points to the left of key
        j = i-1
        #check if key is less than arr[j] and move arr[j] one position up if it is greater than key
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def insertionDecreasing(arr):

    for i in range(1,len(arr)):        
        key = arr[i]
        j = i-1

        while j >=0 and key > arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion([9,5,1,2,4,7]))
print(insertionDecreasing([9,77,5,6,1,2]))
