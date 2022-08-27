print('''
===== ORDER =====
===== INPUT =====
  1.HinhThang.
  2.HinhChuNhat
  3.HinhVuong
  4.HinhBinhHanh
  5.HinhTamGiac
  6.HinhThoi
''')
def HinhThang(DayLon,DayBe,ChieuCao):
    print(f"Dien tich hinh thang la {((DayLon+DayBe) * ChieuCao)/2}.")
    return ""
def HinhChuNhat(ChieuDai,ChieuRong):
    print(f"Dien tich hinh chu nhat la {ChieuDai * ChieuRong}.")
    print(f"Chu vi hinh chu nhat la {(ChieuDai + ChieuRong)*2}.")
    return ""
def HinhVuong(ChieuRong):
    print(f"Dien tich cua hinh vuong la {ChieuRong**2}.")
    print(f"Chu vi hinh vuong la {ChieuRong * 4}.")
    return ""
def HinhBinhHanh(CanhDay,ChieuCao):
    print(f"Dien tich cua hinh binh hanh la {CanhDay * ChieuCao}.")
    return ""
def HinhTamGiac(CanhDay,ChieuCao):
    print(f"Dien tich hinh tam giac la {(CanhDay * ChieuCao)/2}")
    return ""
def HinhThoi(DuongCheo1,DuongCheo2):
    print(f"Dien tich hinh thoi la {(DuongCheo1 * DuongCheo2)/2}")
    return ""
choice = int(input("Chon hinh trong 6 hinh tren: "))
if choice == 1:
    a = float(input("Nhap day lon: "))
    b = float(input("Nhap day be: "))
    c = float(input("Nhap chieu cao: "))
    print(HinhThang(a,b,c))
elif choice == 2:
    d = float(input("Nhap chieu cao: "))
    e = float(input("Nhap chieu rong: "))
    print(HinhChuNhat(d,e))
elif choice == 3:
    f = float(input("Nhap chieu rong: "))
    print(HinhVuong(f))
elif choice == 4:
    g = float(input("Nhap canh day: "))
    h = float(input("Nhap chieu cao: "))
    print(HinhBinhHanh(g,h))
elif choice == 5:
    i = float(input("Nhap canh day: "))
    j = float(input("Nhap chieu cao: "))
    print(HinhTamGiac(i,j))
elif choice == 6:
    k = float(input("Nhap duong cheo 1: "))
    l = float(input("Nhap duong cheo 2: "))
    print(HinhThoi(k,l))        
