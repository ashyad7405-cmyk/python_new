def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

numbers = [10, 40, 30, 20, 50]
print(linear_search(numbers, 20))  # Output: 2
