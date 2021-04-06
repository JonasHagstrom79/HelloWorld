rate = input('Enter Hourly Rate:')
r = float(rate)
hrs = input('Enter Hours:')
h = float(hrs)
#ot = overtime
ot = r * 1.5
if h <= 40 :
    pay = r * h
totalPay = pay
print(totalPay)

elif h > 40 :
    pay = r * 40
    overtime = ot * (h - 40)

totalPay = pay+overtime
print(totalPay)