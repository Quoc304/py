from socket import *
import time
stt = time.time()
if __name__ == "__main__":
        target = input("Nhập tên host name: ")
        t_IP = gethostbyname(target)
        print("Bắt đầu scan ở địa chỉ: ", t_IP)
        for i in range(50,500):
            s = socket(AF_INET, SOCK_STREAM)
            connect = s.connect_ex((t_IP, i))
            if connect == 0:
                print(f"Port {i}: OPEN")
            s.close()
print('Thời gian đã mất: {time.time() - stt}')
