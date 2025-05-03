"""
❯ python3 smart-interviews-questions/3-reverse-array/main.py
5
2 19 8 15 4
4 15 8 19 2
"""
def main():
    n = input()
    arr = [int(i) for i in input().split()]

    reverse_array(arr)

    print(" ".join(str(i) for i in arr))

def reverse_array(arr, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(arr) - 1
    
    if start_index >= end_index:
        return

    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]

    reverse_array(arr, start_index + 1, end_index - 1)


if __name__ == "__main__":
    main()
