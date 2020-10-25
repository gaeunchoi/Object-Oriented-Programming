# Assignment 1, Exercise 6

def check_list(data):
    # Write code here!
    data_out = []

    for i in range(len(data) - 4) :
        check = 0
        tmp = data[i:i+4]
        for j in range(len(tmp)):
            k = j+1
            while(k <= j) :
                if(tmp[j] == tmp[k]) :
                    check = 1
            k = k + 1

        if(check == 0) :
            data_out = tmp

    return data_out


# Test
data_in = [1, -1, 0, 1, 0, 0, 2, 1, -1, 0]
data_out = check_list(data_in)
print(data_out)
