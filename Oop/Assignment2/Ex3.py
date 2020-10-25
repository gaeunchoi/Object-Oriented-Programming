# Assignment 2, Exercise 3

import random
def createSortedRandomList(len):
    # Create sorted random list (0 ~ 10)
    randomList = []
    for i in range(0,len):
        n = random.randint(0,10)
        randomList.append(n)

    randomList.sort()
    
    return randomList


def compress(list_in):
    # Compress list
    # Write code here!
    list_compressed = []
    while True:
        if(len(list_in) == 0) :
            break;

        tmp = list_in[0]
        tmp_list = []

        cnt = list_in.count(tmp)

        for i in range(0, cnt) :
            tmp_list.append(tmp)
            list_in.remove(tmp)

        list_compressed.append(tmp_list)

    return list_compressed


# Test
input_list = createSortedRandomList(12)
print("Input")
print(input_list)

output_list = compress(input_list)
print("Output")
print(output_list)


