"""
    Nhập vào n

Tính S = 1 + 2 + 3 + 4 + … + n
"""

n = int(input("Nhập vào n: "))
s = 0
for i in range(1, n + 1):
    s += i
print(s)
