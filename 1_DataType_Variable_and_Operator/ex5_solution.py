"""
    Nhập vào số giây bất kỳ t (t là số nguyên dương bất kỳ)
    In ra màn hình thời gian tương ứng trong ngày dưới dạng
    hh : mm : ss
"""
t = int(input("Enter the second: "))
hours = (t // 3600) % 24
minutes = (t % 3600) // 60
seconds = (t % 3600) % 60
print(hours, ":", minutes, ":", seconds)
