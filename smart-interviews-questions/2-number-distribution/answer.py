"""
❯ python3 smart-interviews-questions/2-number-distribution/answer.py
10
120 0 -9 89 68 -982 91 -54 -12 -139
1 4 5
"""

def main():
    n = input()
    arr = [int(i) for i in input().split()]

    zero, positive, negative = counter(arr)

    print(f"{zero} {positive} {negative}")

def counter(arr):
    zero_n = posi_n = nega_n = 0

    for i in arr:
        if i > 0:
            posi_n += 1
        elif i < 0:
            nega_n += 1
        else:
            zero_n += 1
    
    return zero_n, posi_n, nega_n

if __name__ == "__main__":
    main()