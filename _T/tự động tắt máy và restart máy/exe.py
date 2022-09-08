import os
commandln = input("Input your command ('r' để khởi động lại máy/ 's' để tắt máy) ")
timewait = int(input("Nhập thời gian chờ "))
if commandln == 'r':
    os.system("shutdown -t 0 -r -f {timewait}")
elif commandln == 's':
    os.system("shutdown -s -t {timewait}")
else:
    print("Không hợp lí! ")
stopcommandln = input("Bạn có muốn dừng không? (y/n) ")
if stopcommandln == 'y':
    os.system("shutdown -a")
elif stopcommandln == 'n':
    print("Đã bỏ qua stopcommandln.")
else:
    print("")


