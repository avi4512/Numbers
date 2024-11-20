def Amstrong(n):
    str_n = str(n)
    c = len(str_n)
    res = 0
    for i in str_n:
        res = res + pow(int(i),c)
    if res == n:
        print("It is a Armstrong Number...")
    else:
        print("It is NOt a Armstrong number....")


Amstrong(371)

