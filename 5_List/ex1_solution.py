"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Trả về kết quả là 1 list, trong đó các phần tử bị dịch
    sang trái k đơn vị
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 2
    Output:
        array = [3, 4, 5, 1, 2]
"""


def shift_array(array, k):
    length = len(array)
    k %= length  # k khong vuot chieu dai cua danh sach
    return array[k:] + array[:k]


arr = [1, 2, 3, 4, 5]
k = 2
result = shift_array(arr, k)
print(result)
