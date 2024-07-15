"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các từ bất kì
    2. 1 số tự nhiên k
    In ra các từ trong list có độ dài lớn hơn k ký tự
"""

word_list = ["apple", "banana", "cherry", "date", "monkey", "blackpink"]
k = 5
def myF(words,k):
    for i in words:
        if len(i) > 5:
            print(i)

print(myF(word_list,k))