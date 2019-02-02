#! Python program that makes the most popular letters the least and vice versa.
#! Created by Kostas Simiriotis, January 2019 for the Python test of the 1st semester.

import string

AB = [['' for i in range(2)] for j in range(26)]
# Φτιάχνω μια λίστα ΑΒ με το λατινικο αλφάβητο (με κεφαλαια) και εναν αριθμο που αντιπροσωπευει ποσες φορες εμφανιζεται καθε γραμμα.
for i in range(26):
    AB[i][0] = list(string.ascii_uppercase)[i]
    AB[i][1] = 0
text = input("Please type the text. ")
text = text.upper()
newText = ''
for i in range(26):
    AB[i][1] = text.count(AB[i][0])

# αφαιρω απο την ΑΒ τους χαρακτηρες με μηδενικη εμφανιση
for i in range(26):
    if (AB[i][1] == 0):
        AB[i].pop(0)
# φτιαχνω δυο νεες λιστες
inText = [x for x in AB if x != [0]]
toText = [x for x in AB if x != [0]]

# Η inText περιεχει τα γραμματα που υπαρχουν ηδη στο κειμενο και τον αριθμο εμφανισης τους
inText = sorted(inText, key=lambda x: x[1])
# Η toText εχει αναποδη ταξινομηση απο την inText. Ετσι το πρωτο στοιχειο της toText ειναι το τελευταιο της inText κλπ.
toText = sorted(toText, key=lambda x: x[1], reverse=True)

#προσθετω στο νεο κειμενο τα στοιχεια της toText(με την πρωτη if)
for i in range(len(text)):
    entered = False
    for j in range(len(inText)):
        if text[i] == inText[j][0]:
            newText += toText[j][0]
            entered = True
# Βαζω αυτη την if για ειδικους χαρακτηρες περαν του αλφαβητου (π.χ. θαυμαστικα, κομματα, κενα κλπ) που μπορει να υπηρχαν στο αρχικο κειμενο.
    if not entered:
        newText += text[i]
    print(newText)
