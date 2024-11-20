#n = 12
#1.square of n = 12 * 12 ==> 144
#2.Reverse of given n ===> 21
#3.Square of Reverse number ==> 21 * 21 == 441
#4.Reverse the Square reverse number ==> 144
# if step1 == Step4 


def reverse(n):
    res = 0
    while n:
        dig = n % 10
        res = (res * 10) + dig
        n = n // 10
    return res

def ADAM_number(n):

    sqr_n = n * n
    rev_n = reverse(n)
    sqr_rev = rev_n * rev_n
    rev_sqr = reverse(sqr_rev)

    if sqr_n == rev_sqr:
        print(f'{n} ADAM number')
    else:
        print(f'{n} Not ADAM Number')
ADAM_number(12)


















