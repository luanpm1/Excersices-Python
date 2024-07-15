"""
    Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c
    có cấu thành độ dài của 1 tam giác được không
"""

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))
if a + b > c and a + c > b and b + c > a:
    print(True)
else: print(False)