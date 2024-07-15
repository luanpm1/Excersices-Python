"""
    Yêu cầu người dùng nhập vào 2 chuỗi ký tự bất kỳ.
    Kiểm tra xem chúng có phải anagrams (phép đảo chữ)
    của nhau không?
    Định nghĩa anagram: 2 từ là anagram của nhau nếu ta có thể
    thu được từ này bằng cách đổi vị trí các ký tự của từ kia
    Các ví dụ:
    "New York Times" và "monkeys write"
    "coronavirus" và "carnivorous"
    "a gentleman" = "elegant man"
    "silent" = "listen"
"""

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)
