def find_smallest(arr):
    smallest_num = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_idx = i
    return smallest_idx

def selection_sort(arr):
    sorted_arr = []
    copied_arr = list(arr)
    for num in range(len(copied_arr)):
        smallest_idx = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_idx))
    return sorted_arr

print(selection_sort([5,2,3,1,0]))
