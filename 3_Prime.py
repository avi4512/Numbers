def prime(n):

    if n <= 1:
        print(f"{n} Not A Prime Number")
        return
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} Not A Prime Number")
            return

    print(f"{n} Prime Number")
n = int(input("Enter the Number:"))
prime(n)

