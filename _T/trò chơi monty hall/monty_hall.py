#import thư viện.
import random
import time
#nhập tên.
name = input("Nhập tên của bạn: ")
#welcome.
welcome = "*Chào mừng đến trò chơi Monty Hall."
wel_1 = "*Sau đây có 3 cửa hãy chọn 1 cửa có con xe và hai cửa còn lại hai con dê"
print(welcome)
print(wel_1)
r = "===================="
#biến in ra kết quả.
result = "Kết quả là..."
#list cửa
doorlst = [1,2,3]
#random ra cửa.
doorrandom = random.choice(doorlst)
#vòng lặp m.
m = True
#==code.
while m:
    choice = int(input("*Lựa chọn của bạn là: "))
    doorchoice = f"Cửa của bạn là {choice}"
    print(doorchoice)
    choice_1 = input("*Bạn có chắc chắn không? (y/n)")
    if choice_1 == 'y':
        if choice > 0 and choice < 4:
            if choice == doorrandom:
                #biến money
                money = 1000
                money_1 = 0
                print(r)

                print(result)
                time.sleep(2)
                print("Bạn đã thắng! Xin chúc mừng !!!")
                print(r)
                money_1 += 200
                print(f"Nhận thêm {money_1}$.")
                print(f"***Tài khoản ngân hàng của {name}: {money + money_1}$.")
            else:
                print(result)
                time.sleep(2)
                print(f"Bạn đã bị sai, cánh cửa chính xác là {doorrandom}.")
                print("*Phá sản.")
                break
        else:
            print("Xin khởi động lại.")
            break
    if choice_1 == 'n':
        choice_2 = int(input("*Xin nhập lại cửa: "))
        if choice_2 > 0 and choice_2 < 4:
            if choice_2 == doorrandom:
                #biến money
                money = 1000
                money_1 = 200
                print(r)

                print(result)
                time.sleep(2)
                print("Bạn đã thắng! Xin chúc mừng")
                print(r)
                money_1 += 200
                print(f"Nhận thêm {money_1}$.")
                print(f"***Tài khoản ngân hàng của {name}: {money + money_1}$.")
            else:
                print(result)
                time.sleep(2)
                print(f"Bạn đã bị sai, cánh cửa chính xác là {doorrandom}.")
                print("*Phá sản.")
                break
        else:
            print("Xin khởi động lại.")
            break

