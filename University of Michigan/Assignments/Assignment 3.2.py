hrs = input("Enter Hours:")
rate = input("Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
pay = r * h
ot = r * 1.5

if h <= 40 :
    pay = r * h
    print(pay)

if h > 40 :
    pay = r * 40
    overtime = ot * (h -40)
    print(pay + overtime)