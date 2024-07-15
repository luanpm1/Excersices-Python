"""
    Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu
    nhập lại cho đến khi người dùng nhập đúng số dương

    Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng
    quy tắc”
"""

a = int(input("Nhập vào a: "))
while a < 0:
    a = int(input("Bạn nhập sai nguyên tắc, vui lòng nhập lại số dương: "))
print("Bạn nhập đúng quy tắc")
