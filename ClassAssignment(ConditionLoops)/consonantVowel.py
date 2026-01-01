# ask the user input a word and count vowels and consontant using a function 

word=input("Enter a word:").lower()
vowels='aeiou'

def count_(word):
    vowel=0 
    consonant=0
    for i in word:
        if i in vowels:
            vowel+=1
        else:
            consonant+=1
        
    print(f"The total number of vowel in the word is {vowel} and cosntant is {consonant}")

count_(word)
            