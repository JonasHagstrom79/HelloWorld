rate = input('Enter Hourly Rate:')
r = float(rate)

hrs = input('Enter Hours:')
h = float(hrs)


pay = r * h

#ot = overtime
ot = r * 1.5

payWithOt = pay + ot

if h == 40:
 totalPay = pay
if h > 40:
 totalPay = pay + ot
print(totalPay)