"""
    Đếm số chẵn, lẻ, âm, dương trong dãy sau
"""
numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]

for i in numbers:
    if i % 2 == 0:
        print("even number:", i)
    else:
        print("odd number:", i)
    if i < 0:
        print("negative:", i)
    else:
        print("positive:", i)
