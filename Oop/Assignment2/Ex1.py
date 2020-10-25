# Assignment 2, Exercise 1

def sortList(list_in):
    # Sort input list
    sorted_list = sorted(list_in)
    return sorted_list


def sortDict(dic_in):
    # Write code here!
    sorted_dict = {}
    dic_key = list(dic_in.keys())
    dic_value = list(dic_in.values())

    for i in range(0, len(dic_key)):
        sorted_dict[dic_key[i]] = sortList(dic_value[i])
    return sorted_dict


# Test
test_in = {'n1': [4, 1, 5], 'n2': [3, 1, 0], 'n3': [-1, 1, 9]}
print("Input")
print(test_in)

test_out = sortDict(test_in)
print("Output")
print(test_out)
