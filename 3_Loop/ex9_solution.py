"""
    Cho 1 mảng gồm các số tùy ý
    Kiểm tra xem mảng đó có phải mảng đơn điệu hay không.
    Định nghĩa mảng đơn điệu: mảng đơn điệu là mảng
    không tăng hoặc không giảm
"""
# array = [1, 3, 3, 4, 6, 7, 7]
# array = [5, 3, 2, 2, 1]
array = [2, 3, 2, 1]
# array = [1, 2, 3, 4]
# Tăng dần
increasing = True
# Giảm dần
decreasing = True

for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
        increasing = False
    if array[i] < array[i + 1]:
        decreasing = False

print(increasing or decreasing)
