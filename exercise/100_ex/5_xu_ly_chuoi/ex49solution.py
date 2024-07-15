"""
    Nhập vào một chuỗi, hãy tách toàn bộ con số trong
    chuỗi ra rồi tính tổng của chúng

VD:

Nhập chuỗi: abd45ecf47wde3s1
Tổng: 45 + 47 + 3 + 1 = 96
"""

string = input("Nhập vào string: ")
chuoiTam = ""
tong = 0
for i in string:
    if i.isdigit():
        chuoiTam += i
    else:
        if chuoiTam != "":
            tong += int(chuoiTam)
            chuoiTam = ""
if chuoiTam != "":
    tong += int(chuoiTam)
print(tong)