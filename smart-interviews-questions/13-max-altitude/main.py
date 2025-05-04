"""
~/Development/github.com/sashuu69/dsa-python main*                                                                                          02:29:38 PM
❯ python3 smart-interviews-questions/13-max-altitude/main.py
5
-5 1 5 0 -7
1
"""

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(max_altitude(arr))

def max_altitude(arr):
    alt = maxx = arr[0]

    for i in arr[1:]:
        alt += i

        if maxx < alt:
            maxx = alt
    
    return maxx

if __name__ == "__main__":
    main()
