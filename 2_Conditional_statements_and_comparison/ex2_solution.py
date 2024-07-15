"""
    Yêu cầu người dùng nhập vào 3 số a, b, c
    Tìm nghiệm của phương trình bậc 2
    ax^2 + bx + c = 0
"""
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
delta = b**2 - 4*a*c
if (delta > 0):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("x1:", x1 , "x2:", x2)
elif (delta ==0):
    x = -b / (2*a)
    print("x:", x)
else: print("meaningless equation")