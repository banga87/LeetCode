"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

def tribonacci(n: int) -> int:
    arr = [0] * (n + 1)
    
    if n == 0:
        return n
    if n <= 2:
        return 1

    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    
    for i in range(3, n + 1):
        arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1]

    return arr[-1]

print(tribonacci(25))