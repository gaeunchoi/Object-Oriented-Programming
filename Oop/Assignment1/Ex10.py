# Assignment 1, Exercise 10

def modify_list(l):
    l_new = []

    # Write code here!
    for i in l:
        is_tuple = type(i) is tuple
        if(is_tuple) :
            tmp = list(i)
            tmp[-1] = 'TMP'
            tmp = tuple(tmp)
            l_new.append(tmp)

        else :
            l_new.append(i)

    return l_new

# Test
l_in = [3, -1, ('a', 20, 'x'), (40, 'b', 'k'), (70, 80, 'c')]
l_out = modify_list(l_in)
print("Before:")
print(l_in)
print("After:")
print(l_out)
