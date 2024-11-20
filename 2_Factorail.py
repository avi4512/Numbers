def Factorial(n):

    res = 1
    if n < 0:
        print("Factorial Not exist for the Negative Numbers...!")
        return
    if n == 0:
        print(f"Factorial of {n} is 1")
        return
    for i in range(1,n+1):
        res = res * i
    print(f"Factorial of {n} is {res}")

Factorial(7)



