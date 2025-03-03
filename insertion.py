#Problem:
#Given an unsorted array of integers, sort the array in ascending order using the insertion sort algorithm.
def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]
        j = i - 1

        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place key at its correct position

    return arr

# Example usage
arr = [9, 5, 1, 4, 3]
sorted_arr = insertion_sort(arr)
print("Sorted Array:", sorted_arr)


