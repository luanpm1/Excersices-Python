"""
    Nhập vào số nguyên dương a, kiểm tra xem a có phải là
    số nguyên tố hay không
"""
from math import *
a = float(input("Nhập vào a: "))
# duyệt qua các số từ 2 đến căn n, nếu n chia hết cho bất
# kì số nào thì không phải số nguyên tố
# khai căn = 0.5
for i in range(2,sqrt(a)):
    if a % i == 0:
        print("'a' không phải là số nguyên tố")
    else: print("'a' là số nguyên tố")