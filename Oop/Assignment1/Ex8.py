# Assignment 1, Exercise 8

def swap_case_str(str1):
    # Tip) use .lower() and .upper()
    result_str = ""
    # Write code here!

    for i in str1 :
        if i.isupper():
            result_str = result_str + i.lower()
        else :
            result_str = result_str + i.upper()

    return result_str

print(swap_case_str("Python Homework!"))
print(swap_case_str("Incheon University"))
