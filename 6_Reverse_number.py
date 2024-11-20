def reverse(n):
    res = 0
    while n:
        dig = n % 10
        res = (res * 10) + dig
        n = n // 10
    return res
print(reverse(12345))

