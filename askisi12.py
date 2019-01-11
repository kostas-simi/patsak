#! Python program that makes the most popular letters the least and vice versa.
#! Created by Kostas Simiriotis, January 2019 for the Python test of the 1st semester.

import string

AB = [['' for i in range(2)] for j in range(26)]
for i in range(26):
    AB[i][0] = list(string.ascii_uppercase)[i]
    AB[i][1] = 0

text = input("Please type the text. ")
text = text.upper()

for i in range(26):
    AB[i][1] = text.count(AB[i][0])
