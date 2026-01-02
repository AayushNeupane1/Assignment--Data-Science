# 2. Count frequency of characters using Counter.


from collections import Counter as c

def char_frequency(s):
    return c(s)


input_string = input("Enter the word:")
frequency = char_frequency(input_string)
print("The character frequency of the string is", frequency) 