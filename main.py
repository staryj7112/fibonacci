def sum_even_fibonacci(n):
    a, b, total = 3, 4, 0
    while a <= n:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

print(sum_even_fibonacci(7000000))