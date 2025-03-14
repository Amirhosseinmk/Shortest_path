def bubbleSort(arr,key = lambda x:x):
    for i in range(0,len(arr) - 1):
        j = i + 1
        for j in range(j,len(arr)):
            if key(arr[j]) < key(arr[i]):
                arr[j],arr[i] = arr[i],arr[j]
    return arr
    




