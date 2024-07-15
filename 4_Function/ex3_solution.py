"""
    Viết 1 hàm nhận vào 2 tham số đầu vào
    1. Cân nặng của 1 người (đơn vị: kg)
    2. Chiều cao của người đó (đơn vị: mét)
    Hàm trả về 3 thông tin sau:
    1. Chỉ số cân đối cơ thể BMI = cân nặng/chiều cao^2
    2. Thể trạng của người đó
    3. Nguy cơ phát triển bệnh
    2. và 3. được kết luận dựa vào bảng sau:
    BMI             Status (Thể trạng)  Disease risk (Nguy cơ phát triển bệnh)
    < 18.5          Underweight         Low
    18.5-24.9       Normal              Medium
    25.0-29.9       Overweight          High
    30.0-34.9       Obese               High
    > 35.0          Extremely Obese     Very High
"""


def estimate_infor(height, weight):
    bmi = 0.0
    status = ""
    risk = ""
    bmi = weight / (height ** 2)
    # status
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        status = "Normal"
    elif 25.0 <= bmi <= 29.9:
        status = "Overweight"
    elif 30.0 <= bmi <= 34.9:
        status = "Obese"
    else:
        status = "Extremely Obese"
    # risk
    if bmi < 18.5:
        risk = "Low"
    elif 18.5 <= bmi <= 24.9:
        risk = "Medium"
    elif 25.0 <= bmi <= 29.9:
        risk = "High"
    elif 30.0 <= bmi <= 34.9:
        risk = "High"
    else:
        risk = "Very High"
    return bmi, status, risk


height = float(input("Enter the height: "))
weight = float(input("Enter the weight: "))
bmi, status, risk = estimate_infor(height, weight)
print("BMI:", bmi)
print("Status:", status)
print("Disease risk:", risk)
