def fib(n):
    result = [1, 1]
    while n>2:
        result.append(result.pop(0) + result[0])
        n -=1
    return result[1]

