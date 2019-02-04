#! Python program that prints prime factors of an integer.
#! Created by Kostas Simiriotis, February 2019 for the Python test of the 1st semester.

import math #Θα το χρησιμοποιησω ΜΟΝΟ για να βρω την ριζα του αριθμου αφου ξεμπερδεψω με τα 2αρια.

def primeFactors(n):
    print("The prime factorisation of",n,"is:")
    #Εκτυπωνω τα 2αρια που τον διαιρουν.
    while n%2 == 0:
        print(2)
        n /= 2

    #Σε αυτο το σημειο ο αριθμος θα εχει γινει μονος και επομενος μπορω να βαλω βημα 2.
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            print(i)
            n /= i

    #Η επομενη if ειναι για τη περιπτωση που ο αριθμος ειναι κ αυτος πρωτος μεγαλυτερος του 2
    if n>2:
        print(n)


number = int(input("Please provide an integer: "))
primeFactors(number)
