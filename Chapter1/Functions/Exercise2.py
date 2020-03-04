def computegrade(score):
    if score>1.0 or score<0:
        print("Bad Score");
    else:
        if score>=0.9:
            return("A");
        elif score>=0.8:
            return("B");
        elif score>=0.7:
            return("C");
        elif score>=0.6:
            return("D");
        else:
            return("F");

try:
    scoreg = float(input("Enter Score:"))
except:
    print("Bad Score")


print(computegrade(scoreg))
