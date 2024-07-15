"""
    Nhập vào số thực a, kiểm tra xem a có phải là số nguyên
    hay không, nếu có thì in ra True, ngược lại in ra False
"""

a = float(input("Nhập vào a: "))
# dùng hàm round để làm tròn
b = round(a)
print(a == b)