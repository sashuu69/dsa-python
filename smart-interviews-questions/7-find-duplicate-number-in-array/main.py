"""
~/Development/github.com/sashuu69/dsa-python main*                                                                                          02:36:16 PM
❯ python3 smart-interviews-questions/7-find-duplicate-number-in-array/main.py
6
5 4 10 9 21 10
10
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(find_duplicate_number(arr))

def find_duplicate_number(arr):
    temp_arr = [0 for _ in range(0, 110)]

    for num in arr:
        temp_arr[num] += 1
    
    for i in range(0, len(temp_arr)):
        if temp_arr[i] > 1:
            return i


if __name__ == "__main__":
    main()
