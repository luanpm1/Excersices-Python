"""
    Cho list bao gồm các số bất kì
    Đếm xem số lần xuất hiện của mỗi số trong list đó
"""

numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]
result = {}

for i in numbers:
    if i not in result.keys():
        result[i] = 1
    else:
        result[i] += 1

for key, value in result.items():
    print("Number", key, "appears", value, "times")
