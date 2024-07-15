"""
    Cho 1 danh sách gồm các số
    Viết các chương trình để tìm ra:
    1. Số lớn nhất
    2. Số lớn thứ nhì
    3. k số lớn nhất

"""

numbers = [20, 10, -4, 5, 15, 36, -16]
print("Largest number is:", max(numbers))
secondLargestNumber = sorted(numbers)
print("Second largest number is:", secondLargestNumber[-2])


def findKLargestNumber(num, k):
    result = sorted(num)
    print(result)
    return result[-k:]


print(findKLargestNumber(numbers, 2))
