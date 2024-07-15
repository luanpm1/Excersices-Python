"""
    Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c

    Nếu d là số trong khoảng từ 100 - 200 thì in ra True,
    ngược lại in ra False
"""

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))
d = (a + b)**c
print(d)
print(100 <= d <= 200)
