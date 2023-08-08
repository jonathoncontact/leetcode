def fib(n: int) -> int:
    #base case 
    if n == 0:
        return 0
    if n == 1:
        return 1

    #recursive case
    return fib(n-1) + fib(n-2)

result = fib(32)
print(result)