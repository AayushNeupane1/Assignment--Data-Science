import re
#Input text
text = "play playing sing ring bring walking coding"
#Apply a simple stemming rule
stemmed_words = [
w[:-3]
for w in text.split()
if re.match(r".* [aeiou].*ings", w)
]
#Print the resulting words
print("".join(stemmed_words))