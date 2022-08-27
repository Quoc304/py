f_num = ["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
ff_num = ["Mười","Mười Một","Mười Hai","Mười Ba","Mười Bốn","Mười Năm","Mười Sáu","Mười Bảy","Mười Tám","Mười Chín"]
m_num = ["Chục","Trăm","Nghìn","Triệu","Tỉ"]
number = int(input("Input: "))
out = 'Ouput:'
if number < 10:
    j = -1
    for i in range(0,10):
        j+=1
        if number == i:
            print(out + f_num[j])
if number < 20 and number > 9:
    j = -1
    for i in range(10,20):
        j+=1
        if number == i:
            print(out + ff_num[j])
if number < 30 and number > 19:
    j = -1
    sem = " Mươi "
    for i in range(20,30):
        if number == 20:
            print(out + f_num[2] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[2] + sem + f_num[j])
if number < 40 and number > 29:
    j = -1
    sem = " Mươi "
    for i in range(30,40):
        if number == 30:
            print(out + f_num[3] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[3] + sem + f_num[j])
if number < 50 and number > 39:
    j = -1
    sem = " Mươi "
    for i in range(40,50):
        if number == 40:
            print(out + f_num[4] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[4] + sem + f_num[j])
if number < 60 and number > 49:
    j = -1
    sem = " Mươi "
    for i in range(50,60):
        if number == 50:
            print(out + f_num[5] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[5] + sem + f_num[j])
if number < 70 and number > 59:
    j = -1
    sem = " Mươi "
    for i in range(60,70):
        if number == 60:
            print(out + f_num[6] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[6] + sem + f_num[j])
if number < 80 and number > 69:
    j = -1
    sem = " Mươi "
    for i in range(70,80):
        if number == 70:
            print(out + f_num[7] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[7] + sem + f_num[j])
if number < 90 and number > 79:
    j = -1
    sem = " Mươi "
    for i in range(80,90):
        if number == 80:
            print(out + f_num[8] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[8] + sem + f_num[j])
if number < 100 and number > 89:
    j = -1
    sem = " Mươi "
    for i in range(90,100):
        if number == 90:
            print(out + f_num[9] + sem)
            break
        j+=1
        if number == i:
            print(out + f_num[9] + sem + f_num[j])
