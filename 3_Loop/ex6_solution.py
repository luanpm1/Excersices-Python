"""
    Yêu cầu người dùng nhập vào 1 số dạng nhị phân (e.g. 1001)
    In ra giá trị dạng thập phân tương ứng của số đó
"""
n = input("Enter a binary number: ")
print(type(n))
numeric = int(n, 2)
print("Value numeric of bainery", n, "is", numeric)
