def selection(arr):

    for i in range(len(arr)):
        #set index of minimum as i
        mini = i
        # check if adjacent element is smaller than current min
        # update index of minimum if it is smaller
        for j in range(i+1,len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        
        arr[i], arr[mini] = arr[mini], arr[i]

    return arr

print(selection([3,5,1,8,0,7]))