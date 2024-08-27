# Define the function to find the unique element in a sorted array
def find_unique_element(A, low, high):
    # Check if the search space is empty
    if low > high:
        return -1  # Not found, return -1

    # Calculate the middle index of the search space
    mid = (low + high) // 2

    # Check if the middle element is the unique element
    print('check ==> mid:',mid,'value =',A[mid])
    if A[mid] != A[mid - 1] and A[mid] != A[mid + 1]:
        return A[mid]  # Unique element found, return it

    # Check if the middle element is at an even index
    if mid % 2 == 0:  # Check even-indexed half
        # Check if the next element is the same as the middle element
        print(mid,"(even)",(low,high),'A[',mid,']=',A[mid],'A[',mid+1,']=',A[mid + 1])
        if A[mid] == A[mid + 1]:
            # If so, the unique element must be to the right of the next element
            print("even+2=",(mid+2,high))
            return find_unique_element(A, mid + 2, high)
        else:
            # Otherwise, the unique element must be to the left of the middle element
            print("even-2=",(low,mid - 2))
            return find_unique_element(A, low, mid - 2)
    else:  # Check odd-indexed half
        # Check if the previous element is the same as the middle element
        print(mid,"(odd)",(low,high),'A[',mid,']=',A[mid],'A[',mid-1,']=',A[mid- 1])
        if A[mid] == A[mid - 1]:
            # If so, the unique element must be to the right of the middle element
            print("odd+1=",(mid+1,high))
            return find_unique_element(A, mid + 1, high)
        else:
            # Otherwise, the unique element must be to the left of the middle element
            print("odd-1=",(low,mid-1))
            return find_unique_element(A, low, mid - 1)

# Test code, arr is odd(7) n, search is 0 to even(6) 
arr = [2, 2, 5, 8, 8, 10, 10]  # Example array with a unique element 5
#unique_element = find_unique_element(arr, 0, len(arr) - 1)  # Call the function to find the unique element
#print("Unique element:", unique_element)  # Output should be 5
# Test code, arr is odd(9) n, search is 0 to even(8) 
arr = [2, 2, 4, 4, 8, 8,9, 10, 10]  # Example array with a unique element 9
#unique_element = find_unique_element(arr, 0, len(arr) - 1)  # Call the function to find the unique element
#print("Unique element:", unique_element)
# Test code, arr is odd(9) n, search is 0 to even(8) 
arr = [1,2, 2, 4, 4, 8, 8, 10, 10]  # Example array with a unique element 9
print(arr)
unique_element = find_unique_element(arr, 0, len(arr) - 1)  # Call the function to find the unique element
print("Unique element:", unique_element)
