"""
    Viết hàm nhận 3 số đầu vào, và trả về số lớn nất trong 3 số
    (Không dùng hàm max())
"""


def get_max(a, b, c):
    if a != b != c:
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c
    else:
        return "Exception"


print(get_max(1, 3, 4))
# print(get_max(1, 3, 3))