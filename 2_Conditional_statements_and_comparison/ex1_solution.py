"""
    Nhập vào 2 số:
    - 1 số đại diện cho 1 năm
    - 1 số đại diện cho 1 tháng trong năm đó
    In ra màn hình số ngày của tháng đó
    Chú ý: Năm nhuận là năm thỏa mãn 1 trong 2 điều kiện sau:
    - Năm đó chia hết cho 4 nhưng không chia hết cho 100
    - Năm đó chia hết cho 400
"""
year = int(input("Enter year number: "))
month = int(input("Enter month number: "))

isLeapYear = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month == 2 and isLeapYear:
    print(29)
else:
    print("Số ngày của tháng {} năm {} là:".format(month, year), daysOfMonth[month - 1])
