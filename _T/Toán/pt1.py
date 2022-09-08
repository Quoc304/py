from fractions import Fraction

def Pt1(a,b):
    
    if a == 0:
        if b == 0:
            print("Vo so nghiem.")
        else:
            print("Vo nghiem.")
            return ""
    else:
        print(f"Nghiem cua x la {Fraction(-b/a)}")
        return ""
