def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

array=[3,2,4,1]
partition(array, 0, 3)
print(array)

        
