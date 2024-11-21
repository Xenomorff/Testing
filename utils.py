async def get_fib(n: int) -> int:
    '''возвращает n-e число из последовательности Фибоначчи'''
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a