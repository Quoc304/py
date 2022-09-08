from math import *
#biến a,b
#####a = int(input("Nhập số a: "))
#####b = int(input("Nhập số b: "))
#####p = int(input("Nhập số mũ: "))
#công thức tổ hợp
def Combination(k,n):
    C = (factorial(n))/(factorial(k)*factorial(n-k))
    return int(C)
#công thức chính hợp
def Permutation(k,n):
    A = (factorial(n))/(factorial(n-k))
    return int(A)
#công thức hoán vị
def Conversion(n):
    P = factorial(n)
    return int(P)
#công thức nhị thức Newton dạng (a+b)^n
def BinomialNewton(a,b,n):
    Sum = 0
    Sum_Result = 0
    k = 0
    for i in range(k,n+1):
        Sum += i
    i = n
    j = 0
    while k < n+1:    
        binomial = Combination(k,n) * (a ** (i)) * (b ** (j))
        Sum_Result += binomial
        k+=1
        i-=1
        j+=1
    return int(Sum_Result)
###print(BinomialNewton(a,b,p))
