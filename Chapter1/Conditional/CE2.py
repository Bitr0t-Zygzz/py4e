while 1:
    try:
        hour = int(input("Enter Hours:"))
        rate = float(input("Enter Rate:"))
        break;
    except:
        print("Error please enter numeric input.")
        continue


if hour>40:
    pay= 40*rate + (hour-40)*rate*1.5
else:
    pay = hour*rate

print("Your pay is "+ str(pay))
