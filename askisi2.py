#! Python program that prints prime factors of an integer.
#! Created by Kostas Simiriotis, February 2019 for the Python test of the 1st semester.

import math #Θα το χρησιμοποιησω ΜΟΝΟ για να βρω την ριζα του αριθμου αφου ξεμπερδεψω με τα 2αρια.

def primeFactors(n):
    factors = []
    willPrint = ''
    print("The prime factorisation of",n,"is:")
    #Βαζω τα 2αρια που τον διαιρουν στη λιστα με τους παραγοντες.
    while n%2 == 0:
        factors.append(2)
        n /= 2

    #Σε αυτο το σημειο ο αριθμος θα εχει γινει μονος και επομενος μπορω να βαλω βημα 2.
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            factors.append(i)
            n /= i

    #Η επομενη if ειναι για τη περιπτωση που ο αριθμος ειναι κ αυτος πρωτος μεγαλυτερος του 2
    if n>2:
        factors.append(n)

    i=0
    while True:
        #Ως times θεωρω τις φορες εμφανισης του καθε παραγοντα οι οποιες αποτελουν και την δυναμη του.
        times = factors.count(factors[i])
        if times > 1:
            willPrint += '('+str(factors[i])+'**'+str(times)+')'
        else:
            willPrint += '('+str(factors[i])+')'
        #Βαζω στο i βημα times για να προσπερασω τους αριθμους που εχω ηδη προσθεσει στο κειμενο που θα εκτυπωθει.
        i += times
        if i > 8:
            break
    print(willPrint)

number = int(input("Please provide an integer: "))
primeFactors(number)
