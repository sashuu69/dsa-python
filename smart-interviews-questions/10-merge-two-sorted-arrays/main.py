"""
❯ python3 smart-interviews-questions/10-merge-two-sorted-arrays/main.py
7
1 1 5 8 10 12 15
5
-1 2 4 5 7
-1 1 1 2 4 5 5 7 8 10 12 15
"""

def main():
    m = int(input())
    arr1 = [int(i) for i in input().split()]
    n = int(input())
    arr2 = [int(i) for i in input().split()]
    
    arr = arr1 + arr2

    print(" ".join(str(i) for i in merge_sort(arr)))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2

    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    result = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])

    return result

if __name__ == "__main__":
    main()