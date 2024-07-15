"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Đếm xem số k xuất hiện trong list bao nhiêu lần
"""

numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]
k = 10


def countNumber(num, k):
    if k not in num:
        return False
    for i in num:
        if i == k:
            return num.count(i)


print(countNumber(numbers, k))
