def getNthFibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return getNthFibonacci(n-1) + getNthFibonacci(n-2)

def getNthFibonacciMemoized(n, memo = {0:0,1:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = getNthFibonacciMemoized(n-1,memo)+getNthFibonacciMemoized(n-2,memo)
    return memo[n]


print(getNthFibonacciMemoized(8))