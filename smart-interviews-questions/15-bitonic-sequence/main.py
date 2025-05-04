"""
~/Development/github.com/sashuu69/dsa-python main* 8s                                                                                       05:02:30 PM
❯ python3 smart-interviews-questions/15-bitonic-sequence/main.py
4
0 3 2 1
true
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print("true" if is_bitonic(arr) else "false")

def is_bitonic(arr):
    arr_len = len(arr)

    if arr_len < 3:
        return False
    
    i = 1

    while i < arr_len and arr[i] > arr[i - 1]:
        i += 1
    
    if i == 1 or i == arr_len:
        return False
    
    while i < arr_len and arr[i] < arr[i - 1]:
        i += 1

    return i == arr_len


if __name__ == "__main__":
    main()
