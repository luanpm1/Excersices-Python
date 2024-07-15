"""
    Nhập vào điểm của 1 học sinh (0-100)
    Quy đổi điểm từ thang điểm 100 sang thang điểm chữ theo quy tắc:
        Điểm                             Quy đổi
        > 90                                A
        > 80 và <=90                        B
        > 60 và <= 80                       C
        <= 60                               D
"""
point = float(input("Enter a number: "))
if point > 90 and point <= 100: print("A")
elif point <= 90 and point > 80: print("B")
elif point <= 80 and point > 60: print("C")
elif point <= 60 and point >= 0: print("D")
else: print("Exception")

