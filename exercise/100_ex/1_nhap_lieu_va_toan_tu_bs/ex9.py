"""
    Nhập vào số nguyên a, kiểm tra xem a có phải là số chính
    phương hay không, nếu có thì in ra True, ngược lại in ra False
"""

a = int(input("Nhập vào a: "))
cana = a**0.5
print(cana == round(cana))

