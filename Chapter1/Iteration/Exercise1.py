total = 0
count = 0

while 1:
    try:
        get = input("Enter Number:")
        if get=="done":
            break;
        else:
            total += float(get)
            count+=1
    except:
        print("Invalid Input")
        continue
if count!=0:
    print( str(total) + " " + str(count) + " " + str(total/count))
