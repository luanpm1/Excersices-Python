"""
    Một khách sạn có N phòng đôi được đánh số từ 1
    đến N và M đoàn khách.

Với mỗi đoàn khách, ta xếp mỗi cặp khách của đoàn vào
một phòng trống theo thứ tự phòng tăng dần.

Nếu đoàn khách có số người lẻ thì người khách cuối cùng
được xếp vào một phòng trống tiếp theo.

Nếu đã hết phòng còn trống thì ta sẽ xếp khách vào
những phòng mới chỉ có 1 khách theo thứ tự phòng tăng dần.

In ra số khách của mỗi phòng sau khi xếp.

Giả sử không có 2 đoàn khách nào đến cùng một lúc.

Ví dụ 1:
N = 7, M = 3
doankhach = [3,7,3]
Ta in: 2, 2, 2, 2, 2, 1, 2

Ví dụ 2:
N = 5, M = 3
doankhach = [2,3,2]
Ta in: 2, 2, 1, 2, 0
"""