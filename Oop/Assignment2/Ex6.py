# Assignment 2, Exercise 6

def longestWord(filename):
    # Write code here!
    f = open(filename, 'r')
    longest_text_len = 0
    longest_text = ""
    while True:
        line = f.readline()
        if not line:
            break;
        tmp_list = line.replace(',', ' ').replace('.', ' ').split()
        for i in tmp_list:
            if(longest_text_len < len(i)) :
                longest_text_len = len(i)
                longest_text = i

    return longest_text

# Test
longest_word = longestWord("hw2_ex6.txt")
print(longest_word)
