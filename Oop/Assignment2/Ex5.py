# Assignment 2, Exercise 5

def writeFile(input_list):
    # Write code here!
    f = open("hw2_ex5.txt", 'w')
    print_list = []
    for i in input_list :
        f.write(i)
        f.write("\n")
    f.close()
    pass

# Test
input_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Input")
print(input_list)

writeFile(input_list)
