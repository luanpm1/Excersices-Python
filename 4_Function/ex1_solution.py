"""
    Viết hàm tính và trả về khoảng cách giữa 2 điểm:
    - A(xa, ya, za)
    - B(xb, yb, zb)
    trong không gian 3 chiều
"""

from math import sqrt


def calculate_distance(a, b):
    distance = 0
    for i, j in zip(a, b):
        distance += (i - j) ** 2
    distance = sqrt(distance)
    return distance


a_coord = (1, 3, 6)
b_coord = (2, -1, -3)
print("Distance between 2 points is:", calculate_distance(a_coord, b_coord))
