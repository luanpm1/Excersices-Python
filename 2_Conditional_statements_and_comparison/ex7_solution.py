"""
    Yêu cầu người dùng nhập vào 2 số, trong đó:
    - Số thứ nhất là bán kính của 1 hình tròn
    - Số thứ hai là diện tích của 1 hình vuông
    Hãy tính và so sánh xem, trong 2 hình trên,
    hình nào có chu vi lớn hơn
"""

r = int(input("Enter a number: "))
a = int(input("Enter a number: "))

from math import *

# Calculate the circumference of the circle
circumCircle = 2 * pi * r
# Calculate the side of a square from the area
sideSquare = sqrt(a)
# Calculate the perimeter of the square
periSquare = 4 * sideSquare
# result
print(circumCircle > periSquare)
