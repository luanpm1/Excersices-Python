"""
    Yêu cầu người dùng nhập vào lượng nước tiêu thụ của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền nước cho gia đình đó,
    với quy tắc sau:
    Lượng nước (lít)                    Giá mỗi 1000 lít
    0-8000                                  5$
    8001-22000                              6$
    22001-30000                             7$
    30001+                                  10$
"""
unit = float(input("Enter a water unit: "))
if unit >= 0 and unit <= 8000:
    unit *= 5
elif unit >= 8001 and unit <= 22000:
    unit *= 6
elif unit >= 22001 and unit <= 30000:
    unit *= 7
elif unit >= 30001:
    unit *=10
    print("Total water bill:", unit, "$")
else:print("Exception")
