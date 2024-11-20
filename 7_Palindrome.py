# n = 121
# reverse n = 121
# n == reverse n

def reverse(n):
    res = 0
    while n:
        dig = n % 10
        res = (res * 10) + dig
        n = n // 10
    return res

def Palindrome(n):
    safe = n
    res = reverse(n)
    if safe == res:
        print(f"{n} Palindrome")
    else:
        print(f'{n} Not Palindrome')

Palindrome(121)


