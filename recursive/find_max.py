def max_num(arr):
    if len(arr) <= 1:
        return arr[0]
    examinated_num = arr.pop()
    returned_num = max_num(arr)
    if examinated_num >= returned_num:
        return examinated_num
    else: 
        return returned_num

print(max_num([5,8,2, 9, 10]))
