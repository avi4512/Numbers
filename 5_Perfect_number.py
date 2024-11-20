# n = 6  (1 + 2 + 3 = 6)

def Perfect(n):
    res = 0
    for i in range(1,n):
        if n % i == 0:
            res = res + i
    if res == n:
        print(f"{n} Perfect Number")
    else:
        print(f"{n} Not Perfect Number")


Perfect(28)
