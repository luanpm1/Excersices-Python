"""
    Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c
    theo thứ tự tăng dần rồi in ra lại
"""

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print(a,b,c)