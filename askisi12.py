#! Python program that makes the most popular letters the least and vice versa.
#! Created by Kostas Simiriotis, January 2019 for the Python test of the 1st semester.

import string

AB = list(string.ascii_uppercase)

text = input("Please type the text. ")
text = text.upper()
print(text)

for i in range(0,26):
