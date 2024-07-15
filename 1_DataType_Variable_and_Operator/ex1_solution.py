"""
    Yêu cầu người dùng nhập vào bán kính của hình tròn.
    Tính và hiển thị ra màn hình chu vi và diện tích của
    hình tròn tương ứng
"""
from math import pi


r = float(input("Enter the radius of the circle: "))
# Calculate circumference
c = 2 * pi * r
# Calculate area
a = pi * r**2
print("Circumference:", c)
print("Area:", a)
print("hello")



