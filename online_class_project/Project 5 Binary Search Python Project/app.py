def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
print("Binary Search Project")
sorted_list = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
target = int(input("Enter the number to search for: "))

# Process
result = binary_search(sorted_list, target)

# Output
if result != -1:
    print(f"Number {target} found at index {result}")
else:
    print(f"Number {target} not found in the list")
