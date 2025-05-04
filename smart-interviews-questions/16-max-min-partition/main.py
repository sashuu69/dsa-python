"""
~/Development/github.com/sashuu69/dsa-python main                                                                                           05:04:50 PM
❯ python3 smart-interviews-questions/16-max-min-partition/main.py
6
7 1 14 16 30 4
2
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    new_arr = quick_sort(arr)

    print(min_max(new_arr))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left_arr = [i for i in arr[1:] if i < pivot]
    mid_arr = [i for i in arr if i == pivot]
    right_arr = [i for i in arr[1:] if i > pivot]

    return left_arr + mid_arr + right_arr

def min_max(arr):
    minn = arr[-1]
    i = 1

    while i < len(arr):
        temp = arr[i] - arr[i - 1]

        if temp < minn:
            minn = temp

        i += 1
    
    return minn


if __name__ == "__main__":
    main()
