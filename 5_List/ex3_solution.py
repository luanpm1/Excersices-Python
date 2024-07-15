"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận,
    kết quả trả về là ma trận tổng của chúng. Nếu phép
    cộng không thực hiện được thì trả về giá trị 0
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    mat2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    Output:
        array = [4, 5, 1, 2, 3]

"""


def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return 0
    result = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat1)):
            temp.append(mat1[i][j] + mat2[i][j])
        result.append(temp)
    return result


mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
mat2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
]
print(add_matrices(mat1,mat2))
