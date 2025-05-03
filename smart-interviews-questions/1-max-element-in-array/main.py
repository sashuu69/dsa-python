"""
❯ python3 smart-interviews-questions/1-max-element-in-array/answer.py
5
-2 -19 8 15 4
15
"""
def main():
    n = input()
    arr = [int(i) for i in input().split()]

    print(max(arr))

def highest(arr) -> int:
    max = 0

    for i in arr:
        if max < i:
            max = i
    
    return max

if __name__ == "__main__":
    main()
