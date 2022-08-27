import random
import string
kboard = int(input("Nhap chieu dai cua mat khau can tao:"))
total = string.hexdigits
lenght = kboard
password = "".join(random.sample(total,kboard))
print(password)

