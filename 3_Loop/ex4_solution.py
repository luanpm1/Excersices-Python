"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra tất cả các số Armstrong nhỏ hơn hoặc bằng n
    Định nghĩa số Armstrong: 1 số n được gọi là số Armstrong nếu:
    Tổng các chữ số của số đó, với mỗi chữ số được lũy thừa với
    số mũ k bằng chính số đó, với k là số chữ số của n
    Ví dụ: 153 là số Amstrong vì:
    153 có 3 chữ số, và 153 = 1^3 + 5^3 + 3^3
"""
n = int(input("Enter a number: "))
for num in range(1, n+1):
    num_digits = len(str(num))
    sum_of_powers = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_powers += digit**num_digits
        temp_num //= 10
    if sum_of_powers == num:
        print(num, "is an Armstrong number")

