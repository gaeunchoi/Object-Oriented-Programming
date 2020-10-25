# Assignment 2, Exercise 2


def returnListOfDict(name, code):
    # Write code here!
    list_out = []
    for i in range(0, len(name)):
        list_out.append({'name': name[i], 'code': code[i]})
    return list_out

# Test
dog_name = ["Puddle", "Retriever", "Shepherd", "Bulldog"]
dog_code = ["#00A", "#FB0", "#8AC", "#EFD"]
print("Input")
print("dog_name=", dog_name)
print("dog_code=", dog_code)

dog_data = returnListOfDict(dog_name, dog_code)
print("Output")
print(dog_data)
