# Assignment 1, Exercise 2

# Check condition
def checkCondition(x):
    # Write code here!
    if(100 <= x <= 200 or 300 <= x < 350) :
        print("%d:True" % x)
    else :
        print("%d:False" % x)

# Test
checkCondition(150)
checkCondition(400)
checkCondition(800)
