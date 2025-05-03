"""
❯ python3 smart-interviews-questions/4-odd-and-even-sum/main.py
5
4 6 9 2 5
14 12
"""

def main():
    n = input()
    arr = [int(i) for i in input().split()]

    odd_sum, even_sum = aggregator(arr)

    print(f"{odd_sum} {even_sum}")

def aggregator(arr):
    odd_sum = even_sum = 0

    for i in arr:
        if i % 2 == 1:
            odd_sum += i
        else:
            even_sum += i

    return odd_sum, even_sum


if __name__ == "__main__":
    main()
