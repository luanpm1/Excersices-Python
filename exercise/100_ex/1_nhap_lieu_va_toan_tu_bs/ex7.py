"""
    Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết
    cho 2 thì in ra True,ngược lại in ra False
"""

a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
print(a and b % 2 == 0)