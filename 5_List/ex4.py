"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận cùng kích thước,
    kết quả trả về là ma trận tích của chúng
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    mat2 = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]
    Output:
        array = [
        [58,  64],
        [139, 154],
    ]

"""


def multiply_matrices(mat1, mat2):
    # Kiêm tra kích thướt hai ma trận
    if len(mat1) != len(mat2):
        return None
        exit()
    # result

