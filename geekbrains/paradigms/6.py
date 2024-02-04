def binary_search(arr, target):
    """
    This function takes a sorted array arr and a target value and returns the index
    of the target in the array, or -1 if the target is not present.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test the function
test_array = [1, 3, 4, 6, 7, 8, 10, 13, 14]
test_target = 4

# Call the binary_search function
index_result = binary_search(test_array, test_target)
print(index_result)