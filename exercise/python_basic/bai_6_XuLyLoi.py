"""
    Nhập từ bàn phím 2 số a và b là các giá trị kiểu số nguyên
    Tính c=a/b
        Nếu c hợp lệ thì in c
        Nếu b = 0 thi in ra 'Lỗi chia cho 0'
"""

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))

c = a / b
if b == 0:
    print("Lỗi chia cho 0")
else:
    print(c)

lst = [3 ** x for x in range(9)]
