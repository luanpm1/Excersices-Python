"""
    Nhập vào số nguyên dương a và b, in toàn bộ ước chung
    của a và b
"""

a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
# duyệt qua các số từ 1 đến min a
for i in range(1, min(a, b) + 1):
    # nếu thõa điều kiện ước chung thì in ra
    if a % i == 0 and b % i == 0:
        print(i)
