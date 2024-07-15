"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    hãy loại bỏ toàn bộ các dấu câu cũng như ký tự đặc biệt
    khỏi chuỗi ký tự đó và trả về kết quả
"""
from string import punctuation


def remove_punctuations(string):
    for p in punctuation:
        string = string.replace(p, "")
    return string


print(punctuation)
text = """
    Maya Angelo said, "If you don't like something, change it. 
    If you can't change it, change your attitude."
"""
print(remove_punctuations(text))
