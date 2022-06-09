def binary_search(number_to_find, sorted_values):
    sorted_values.sort()
    low = 0
    high = len(sorted_values)-1
    
    def do_recursive_search(find_me, arr, low, high):
        if low > high:
            return -1
        
        middle = (low + high) // 2
        print(middle)
        if find_me == arr[middle]:
            return middle
        if find_me < arr[middle]:
            return do_recursive_search(find_me, arr, low, middle-1)
        if find_me > arr[middle]:
            return do_recursive_search(find_me, arr, middle+1, high)
            
    return do_recursive_search(number_to_find, sorted_values, low, high)