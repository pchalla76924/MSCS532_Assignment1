def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr


n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

sorted_arr = insertion_sort_desc(arr)

print("Sorted array in decreasing order:", sorted_arr)