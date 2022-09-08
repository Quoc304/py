import math
from fractions import Fraction

def Pt2(a,b,c):
    while True:
        if a == 0 and b == 0:
            print("Mot trong so a, b phai khac khong.")
            a = float(input("Nhap so a: "))
            b = float(input("Nhap so b: "))        
        else:
            delta = b**2 - 4 * a * c

            if delta < 0:
                print("Phuong trinh vo nghiem.")
                return ""
            elif delta == 0:
                print(f"x1 va x2 co nghiem kep la x1 = x2 = {-b / (2 * a)}.")
                return ""
            else:
                print("x1 va x2 co hai nghiem rieng biet lan luot la:")
                print(f"Nghiem cua a la {Fraction((-b + math.sqrt(delta))/(2*a))}")
                print(f"Nghiem cua b la {Fraction((-b - math.sqrt(delta))/(2*a))}")
                return ""

