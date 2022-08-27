from fractions import Fraction

a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))

if a == 0:
    if b == 0:
        print("Vo so nghiem.")
    else:
        print("Vo nghiem.")

else:
    print(f"Nghiem cua x la {Fraction(-b/a)}")
