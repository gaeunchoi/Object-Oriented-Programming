# Assignment 1, Exercise 7

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

# Write code here!
xKey = list(x.keys())
yKey = list(y.keys())

for i in range(0, min(len(xKey), len(yKey))):
    if(x[xKey[i]] == y[yKey[i]]) :
        print("%s: %d is present in both x and y" % (xKey[i], x[xKey[i]]))
