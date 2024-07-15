"""
    In ra các số có ít hơn 4 chữ số và chia hết cho cả 5 và 7
"""
n = input("Enter a number: ")
if len(n) < 4:
    print("let go")
    for i in range(999):
        if i % 5 == 0 and i % 7 == 0:
            print(i)



else:
    print("Exception")

# print(420/7)

