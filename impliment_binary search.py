def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # If target is not present in array
    return -1

while True:
    # Initialize an empty array
    arr = []

    # Take user input for the sorted array elements one by one
    while True:
        element = input("Enter the next element of the sorted array (or 'done' to finish): ")
        if element.lower() == 'done':
            break
        arr.append(int(element))

    # Take user input for the target element
    target = int(input("Enter the element to search for: "))

    # Perform binary search
    result = binary_search(arr, target)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

    # Ask if the user wants to search again
    choice = input("Do you want to search again? (1/2): ")
    if choice.lower() != '1':
        break
