"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên lớn hơn 1
    1. Kiểm tra xem đó có phải là số nguyên tố hay không
    2. In ra màn hình tất cả các số nguyên tố nhỏ hơn hoặc bằng n
"""
from math import sqrt

n = int(input("Enter a number: "))
# First task
for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        print(n, "is a composite number")
        exit(0)
print(n, "is a prime number")

# Second task
for i in range(2, n + 1):
    if i == 2:
        print(i, "is a prime number")
        continue
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i, "is a prime number")
