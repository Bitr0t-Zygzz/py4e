count = 0
high = 0
low = 0

while 1:
    try:
        get = input("Enter Number:")
        if get=="done":
            break;
        else:
            if count==0:
                high = float(get)
                low= float(get)

            if float(get)>high:
                high = float(get)

            if float(get)<low:
                low = float(get)

            count+=1
    except:
        print("Invalid Input")
        continue

if count!=0:
    print( "min: " + str(low) + "\nmax: " + str(high) + "\n# of inputs: " + str(count))
