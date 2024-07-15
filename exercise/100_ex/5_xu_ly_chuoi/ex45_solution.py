"""
    Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên
    cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó

VD:

Nhập: 3, 12, 15
Tổng: 30
"""

string = str(input("Nhập vào string: "))
# cắt bỏ dấu ","
stringSplit = string.split(",")
# partInt
a = int(stringSplit[0])
b = int(stringSplit[1])
c = int(stringSplit[2])
# tính tổng
tong = a + b + c
print(tong)