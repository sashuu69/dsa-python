"""
~/Development/github.com/sashuu69/dsa-python main* 7s                                                                                       03:53:37 PM
❯ python3 smart-interviews-questions/14-longest-contiguous-1s/main.py
10
1 0 0 1 0 1 1 1 1 0
4
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(longest(arr))

def longest(arr):
    maxx = prev = count = 0
    for i in arr:
        if prev == 0 and i == 1:
            count = 1
        elif i == 1:
            count += 1
        
        if maxx < count:
            maxx = count
        
        prev = i
        
    return maxx

if __name__ == "__main__":
    main()
