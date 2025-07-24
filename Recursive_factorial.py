def factorial(num, memo={}):
    if num<=1:
        return 1
    if num in memo:
        return memo[num]
    memo[num] = num * factorial(num-1,memo)
    return memo[num]
n=int(input())
result = factorial(n)
print(factorial(n))
