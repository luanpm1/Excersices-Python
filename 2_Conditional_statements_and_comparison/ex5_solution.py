"""
    Yêu cầu người dùng nhập vào 3 số nguyên dương
    1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
    2. Nếu có thì kiểm tra tiếp xem đây là tam giác cân, tam giác đều,
    tam giác vuông hay tam giác thường
    3. Kiểm tra tiếp xem tam giác có góc tù hay không?
    4. Tính diện tích của tam giác
"""
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a + b > c and a + c > b and b + c > a:
    print("is a triangle")
    if a == b == c:
        print("equilateral triangle") # tam giac deu
    elif a == b or a == c or b == c:
        print("isosceles triangle") # tam giac can
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("right triangle") # tam giac vuong
    else: print("regular triangle") # tam giac thuong
    p = (a + b +c)/2
    area = math.sqrt(p*(p - a)*(p -b)*(p -c))
    print("Area triangle:", area, "unit")
else:print("Exception")