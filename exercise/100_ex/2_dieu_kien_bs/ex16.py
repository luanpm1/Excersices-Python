"""
    Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác,
    kiểm tra xem đó là tam giác gì (tam giác đều, tam giác
    vuông cân, tam giác vuông, tam giác cân hay tam giác thường)
"""

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif (a == b or a == c or b == c):
        if (a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2):
            print("Tam giác vuông cân")
        else:
            print("Tam giác cân")
    elif (a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2):
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Không thể tạo thành 1 tam giác")
