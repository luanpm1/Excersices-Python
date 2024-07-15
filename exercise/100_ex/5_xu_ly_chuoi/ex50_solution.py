"""
    Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là
    một chuỗi mật khẩu mạnh hay không (một chuỗi mật
    khẩu mạnh cần có ít nhất 1 ký tự đặc biệt, 1 ký
    tự in hoa, 1 con số, 1 chữ thường và độ dài phải
    lớn hơn 6)
"""

string = input("Nhập vào string: ")
ktDoDai = len(string) > 6
ktDacBiet = ktInHoa = ktInThuong = ktSo = False
for i in string:
    if i.isdigit():
        ktSo = True
    elif i.isupper():
        ktInHoa = True
    elif i.islower():
        ktInThuong = True
    else:
        ktDacBiet = True
if ktDoDai and ktSo and ktDacBiet and ktInThuong and ktInHoa:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")
