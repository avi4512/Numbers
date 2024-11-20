#n = 1729
#1.Sum of Digits = (1 + 7 + 2 + 9 = 19)
#2.Reverse sum of digits (91)
#3. Multiply the Sumo f digits and Reverse sum of digits (19 * 91) = 1729


def reverse(n):
    res = 0
    while n:
        dig = n % 10
        res = (res * 10) + dig
        n = n // 10
    return res
#1.Sum of Digits
def Magical_number(n):

    sum_digits = 0
    safe = n
    while safe:
        digit = safe % 10
        sum_digits = sum_digits + digit
        safe = safe // 10
    

    #2.reverse the getting result
    rev_n = reverse(sum_digits)
    
    #3.multiply the reverse num and sum of digits
    res = rev_n * sum_digits

    if res == n:
        print(f"{n} Magical Number")
    else:
        print(f'{n} Not Magical Number')

Magical_number(1729)















