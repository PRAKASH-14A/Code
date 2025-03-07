def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):  # Always iterates fully, even if sorted
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap elements
    return arr

arr = [5, 2, 9, 1, 5, 6]
print("Unsorted:", arr)
print("Sorted:", bubble_sort(arr))  # O(n^2) complexity
