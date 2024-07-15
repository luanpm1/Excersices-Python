"""
    Nhập vào số nguyên dương a, đếm số ước của a
"""

a = int(input("Nhập vào a: "))
# tạo biến đếm
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        # nếu thõa biến đếm tăng 1
        count += 1
print(count)
