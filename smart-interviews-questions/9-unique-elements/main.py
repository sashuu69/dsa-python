"""
❯ python3 smart-interviews-questions/9-unique-elements/main.py
7
5 4 10 9 21 4 10
5 9 21
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(" ".join(str(i) for i in unique(arr)))

def unique(arr):
    temp_dict = {}
    temp_list = []

    for i in arr:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

    for i in temp_dict:
        if temp_dict[i] == 1:
            temp_list.append(i)

    return temp_list

if __name__ == "__main__":
    main()
