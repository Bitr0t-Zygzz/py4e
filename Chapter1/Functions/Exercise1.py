def computepay(rate,hours):
  if hours>40:
      pay= 40*rate + (hours-40)*rate*1.5
  else:
      pay = hours*rate
  return pay

while 1:
    try:
        hours = int(input("Enter Hours:"))
        rate = float(input("Enter Rate:"))
        break;
    except:
        print("Error please enter numeric input.")
        continue



pay = computepay(rate,hours)
print("Your pay is "+ str(pay))
