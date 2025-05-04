"""
~/Development/github.com/sashuu69/dsa-python main*                                                                                          02:29:21 PM
❯ python3 smart-interviews-questions/12-gauntlets/main.py
6
4 1 7 4 1 4
2
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(gauntlet_counter(arr))
    
def gauntlet_counter(arr):
    temp_dict = {}
    count = 0

    for i in arr:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

    for i in temp_dict:
        count += temp_dict[i] // 2

    return count

if __name__ == "__main__":
    main()
