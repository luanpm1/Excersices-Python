"""
    Giải và biện luận phương trình ax^2 + bx + c = 0
"""

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))

if a != 0:
    delta = b * b - 4 * (a * c)
    print(delta)
    if delta > 0:
        print("x1:", (-b + delta * 0.5) / 2 * a)
        print("x2:", ((-b - delta * 0.5) / 2 * a))
    elif delta == 0:
        print("Phương trình có ngiệm kép x1 = x2:", -b / 2 * a)
    else:
        print("Phương trình vô ngiệm")
else:print("Không là phương trình bậc hai")