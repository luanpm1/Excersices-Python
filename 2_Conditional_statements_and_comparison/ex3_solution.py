"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên tương ứng
    với số đơn vị điện sử dụng của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền điện cho gia đình đó,
    với quy tắc sau:
    Số đơn vị điện                     Giá
    100 đơn vị đầu                  Miễn phí
    100 đơn vị tiếp theo            5$/đơn vị
    Các đơn vị sau đó               10$/đơn vị
"""
e = int(input("Enter electric unit: "))
if e <= 100:
    e = e
elif e <= 200 and  e > 100:
    e *= 5
elif e > 200:
    e *= 10
print("Total electric bill:", e, "$")



