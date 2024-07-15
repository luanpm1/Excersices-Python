"""
    Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao
    nhiêu ký tự in hoa, bao nhiêu ký tự in thường,
    bao nhiêu ký tự số
"""

string = str(input("Nhập vào string: "))
# khởi tạo biến đếm
inHoa = 0
inThuong = 0
so = 0
# loop
for char in string:
    if char.isupper():
        inHoa += 1
    elif char.islower():
        inThuong += 1
    elif char.isdigit():
        so += 1
print(inHoa,inThuong,so)
