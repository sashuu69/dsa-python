"""
~/Development/github.com/sashuu69/dsa-python main*                                                                                          01:57:18 PM
❯ python3 smart-interviews-questions/11-print-array-a-using-b/main.py
5
100 200 400 800 1000
6
4 2 0 6 10 0
1000 400 100 -1 -1 100
"""

INVALID_INDEX = -1

def main():
    n = int(input())
    arr1 = [int(i) for i in input().split()]
    m = int(input())
    arr2 = [int(i) for i in input().split()]
    
    print(" ".join(str(i) for i in printer(arr1, arr2)))

def printer(arr1, arr2):
    result = []

    for num in arr2:
        if num < len(arr1):
            result.append(arr1[num])
        else:
            result.append(INVALID_INDEX)
    
    return result


if __name__ == "__main__":
    main()
