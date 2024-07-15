"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra n số Fibonacci đầu tiên
    Định nghĩa dãy Fibonacci: Dãy Fibonacci bắt đầu với 2 số 1
    Các số sau được xác định bẳng tồng của 2 số ngay trước nó.
    1 vài số Fibonacci đầu tiên trong dãy: 1, 1, 2, 3, 5, 8
"""
num = int(input("Enter a number: "))
n1, n2 = 1, 1
count = 0
while count < num:
    print(n1)
    new_n = n1 + n2
    n1 = n2
    n2 = new_n
    count += 1

