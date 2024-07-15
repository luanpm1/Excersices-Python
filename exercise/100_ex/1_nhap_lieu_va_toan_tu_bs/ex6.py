"""
    Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng
    KHÔNG nằm trong khoảngtừ 20 - 70 thì in ra True, ngược
    lại in ra False
"""

a = int(input("Nhập vào a: "))
print(a % 5 == 0 and not (20 <= a <= 70))
