"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 chuỗi ký tự bất kỳ
    2. 1 số tự nhiên i bất kỳ
    Loại bỏ phần tử thứ k khỏi chuỗi và trả về chuỗi kết quả
"""


def remove_char(input_string, i):
    if i < 0 or i >= len(input_string):
        return input_string
    else:
        return input_string[:i] + input_string[i + 1:]


string = "Today is a beautiful day!"
i = 5

print("Original string", string)
print("Modified string", remove_char(string, i))
