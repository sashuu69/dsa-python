"""
❯ python3 smart-interviews-questions/5-mean-median-mode/main.py
8
1 2 3 4 5 5 6 6
4.0 4.5 5
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    mean, median, mode = calc_mean(arr, n), calc_median(arr), calc_mode(arr)
    
    print(f"{mean} {median} {mode}")

def calc_mean(arr, n):
    summ = 0
    for num in arr:
        summ += num
    
    return summ / n

def calc_median(arr):
    middle = len(arr) // 2

    if len(arr) % 2 == 1:
        return arr[middle]
    else:
        return (arr[middle - 1] + arr[middle]) / 2

def calc_mode(arr):
    temp_dict = {}

    for i in arr:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    
    max = 0
    for i in temp_dict:
        if temp_dict[i] > max:
            max = temp_dict[i]
    
    temp_list = []
    for i in temp_dict:
        if temp_dict[i] == max:
            temp_list.append(i)
    
    return temp_list[0]


if __name__ == "__main__":
    main()