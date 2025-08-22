#An element is a leader if it is greater than all elements to its right.
# leaders_in_array.py

def find_leaders(arr):
    """
    Function to find leader elements in an array.
    Leaders are elements greater than all elements to their right.
    """
    n = len(arr)
    leaders = []

    # Start with the rightmost element, it's always a leader
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    # Traverse array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Leaders were collected in reverse order
    leaders.reverse()
    return leaders


# Example usage
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print("Array:", arr)
    print("Leaders:", find_leaders(arr))

