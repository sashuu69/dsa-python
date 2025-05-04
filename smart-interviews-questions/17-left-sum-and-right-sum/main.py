"""
~/Development/github.com/sashuu69/dsa-python main* 10s                                                                                      11:04:45 PM
❯ python3 smart-interviews-questions/17-left-sum-and-right-sum/main.py
3
6 7 7
14 1 13
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(" ".join(str(i) for i in left_sum_right_sum(arr)))

def left_sum_right_sum(arr):
    temp_list = []

    for index in range(0, len(arr)):
        left_sum = right_sum = 0

        for i in arr[:index]:
            left_sum += i

        for i in arr[(index + 1):]:
            right_sum += i

        temp_list.append(abs(left_sum - right_sum))

    return temp_list 

if __name__ == "__main__":
    main()
