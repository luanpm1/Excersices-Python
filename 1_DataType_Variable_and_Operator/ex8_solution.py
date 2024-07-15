"""
    Yêu cầu người dùng nhập vào 2 số bất kỳ.
    Viết chương trình để đổi giá trị 2 số đó với nhau theo 2 cách
"""
a = input("Enter the first value: ")
b = input("Enter the second value: ")
print("Original values: a =", a, ", b=", b)
# making 1 (use temporary variables to exchange the values of a and b )
store = a
a = b
b = store
print("Number after swap with making 1: a =", a, ", b=", b)

