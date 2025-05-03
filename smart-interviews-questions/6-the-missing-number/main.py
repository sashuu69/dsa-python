"""
~/Development/github.com/sashuu69/dsa-python main* 16s                                                                                      02:35:55 PM
❯ python3 smart-interviews-questions/6-the-missing-number/main.py
12 15 9 1 71 77 81 29 70 19 11 83 56 2 57 53 68 99 82 100 22 10 51 40 34 98 80 38 39 89 94 4 26 64 45 8 90 24 93 33 21 7 49 88 5 28 55 67 65 50 32 58 6 37 46 42 20 44 41 3 78 76 73 16 31 85 91 54 60 47 97 43 84 17 35 69 13 30 61 79 72 48 23 66 52 27 62 87 63 18 75 96 14 86 95 74 25 59 36
92
"""

def main():
    arr = [int(i) for i in input().split()]
    
    print(find_missing_number(arr))

def find_missing_number(arr):
    temp_arr = [0 for i in range(0, 101)]

    for index in range(0, len(temp_arr)):
        if index in arr:
            temp_arr[index] = 1

    for index in range(1, len(temp_arr)):
        if temp_arr[index] == 0:
            return index

if __name__ == "__main__":
    main()
