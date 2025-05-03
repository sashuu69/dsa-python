"""
~/Development/github.com/sashuu69/dsa-python main* 13s                                                                                      04:01:18 PM
❯ python3 smart-interviews-questions/8-first-and-last/main.py
10
1 3 5 7 9 11 3 13 15 3
3
1 9
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    target = int(input())

    first_occurance, last_occurance = finder(arr, target)

    print(f"{first_occurance} {last_occurance}")

def finder(arr, target):
    first = last = 0

    for i in range(0, len(arr)):
        if arr[i] == target:
            first = i
            break
    
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == target:
            last = i
            break
    
    return first, last


if __name__ == "__main__":
    main()
