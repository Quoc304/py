def Help_SDHT():
    print("**  Help")
    print('**  1/ (a + b)2 = a2 + 2ab + b2 = (a - b)2 + 4ab')
    print('**  2/ (a - b)2 = a2 - 2ab + b2 = (a + b)2 - 4ab')
    print("**  3/ (a + b)3 = a3 + 3a2b + 3ab2 + b3")
    print("**  4/ (a - b)3 = a3 - 3a2b + 3ab2 - b3")
    print("**  5/ a2 – b2 = (a – b)(a + b)")
    print("**  6/ a3 + b3 = ( a + b )( a2 - ab + b2 ) = a3 + b3 = (a+b)3 - 3ab( a + b)")
    print("**  7/ a3 - b3 = ( a - b )( a2 + ab + b2 )")
def Calculator_SHDT(x,y,z,t,i):
    '''
    x = int(input("**  Nhập x: "))
    y = int(input("**  Nhập y: "))
    z = int(input("**  Nhập z: "))
    t = int(input("**  Nhập dạng hằng đẳng thức: "))
    i = int(input("** Nhập dạng hệ quả: "))
    '''
    print("==  7 HĐT  ==")
    if t == 1:
        print(f'**  (a + b)2 = a2 + 2ab + b2 = (a - b)2 + 4ab = {(x+y) ** 2}')
    if t == 2:
        print(f'**  (a - b)2 = a2 - 2ab + b2 = (a + b)2 - 4ab = {(x-y) ** 2}')
    if t == 3:
        print(f'**  (a + b)3 = a3 + 3a2b + 3ab2 + b3 = {(x + y) ** 3}')
    if t == 4:
        print(f'**  (a - b)3 = a3 - 3a2b + 3ab2 - b3 = {(x - y) ** 3}')
    if t == 5:
        print(f'**  a2 – b2 = (a – b)(a + b) = {x ** 2 - y ** 2}')
    if t == 6:
        print(f'**  a3 + b3 = ( a + b )( a2 - ab + b2 ) = a3 + b3 = (a+b)3 - 3ab( a + b) = {x ** 3 + y ** 3}')
    if t == 7:
        print(f'**  a3 - b3 = ( a - b )( a2 + ab + b2 ) = {x ** 3 - y ** 3}')
    if t == 0:
        print("==  Hệ Qủa  ==")
        if i == 1:
            print(f"**  a2 + b2 = (a+b)2 - 2ab = {x ** 2 + y ** 2}")
        if i == 2:
            print(f"** (a + b + c)2 = a2 + b2 + c2 + 2( ab + bc + ca ) = {(x + y + z) ** 2}")
        if i == 3:
            print(f"** (a + b + c)3 = a3 + b3 + c3 + 3( a + b )( b + c )( c + a ) = {(x + y + z) ** 3}")
    return "" 

