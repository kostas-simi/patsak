#! Python program that makes the most popular letters the least and vice versa.
#! Created by Kostas Simiriotis, January 2019 for the Python test of the 1st semester.

import string

AB = [['' for i in range(2)] for j in range(26)]

for i in range(26):
    AB[i][0] = list(string.ascii_uppercase)[i]
    AB[i][1] = 0
text = input("Please type the text. ")
# text = 'Python program that makes the most popular letters the least and vice versa.'
text = text.upper()

for i in range(26):
    AB[i][1] = text.count(AB[i][0])


for i in range(26):
    if (AB[i][1] == 0):
        AB[i].pop(0)
inText = [x for x in AB if x != [0]]
AB = [x for x in AB if x != [0]]

print(inText)

inText = sorted(inText, key=lambda x: x[1])
AB = sorted(inText, key=lambda x: x[1], reverse=True)

print(inText)
print(AB)
counter = len(inText) -1
for i in range(len(inText)):
    text = text.replace(inText[i][0],AB[i][0])
print(text)
