"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên bất kì
    Lấy ra chữ số hàng đơn vị theo 2 cách khác nhau
    rồi in ra màn hình
"""
# making 1
n1 = int(input("Enter a number: "))
unitRow1 = n1 % 10
print("The units digit with making 1 is:", unitRow1)
# making 2
n2 = int(input("Enter a number: "))
part_n = str(n2)
unitRow2 = int(part_n[-1])
print("The units digit with making 2 is:", unitRow2)
print("Next step")

