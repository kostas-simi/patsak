#! Python program that removes comments (with #) for a python code.
#! Created by Kostas Simiriotis, January 2019 for the Python test of the 1st semester.

print("Welcome to Python comment remover, noComm1.0 by Kostas Simiriotis!")
filename = input("Please provide the name of the file: ")
print("Opening the file...")
finput = open(filename, 'r')

foutput = open('noComm_'+filename, 'w')
print("Removing comments...")
for line in finput:
    hashInPrint = False
    l = line.split("#")
    #The following 'if' is added for the cases of print("#not a comment") or print(" student #P18135")
    if len(l)>1 and ('(' in l[0]) and (')' in l[1]):
        foutput.write(l[0]+"#"+l[1]+"\n")
        hashInPrint = True
    if len(l) > 1 and not hashInPrint and l[0] != "":
        l[0] += "\n"

    if (l[0] != "") and not hashInPrint:
        foutput.write(l[0])
finput.close()
print('''New file can be found under the name:\n
            noComm_'''+filename)
foutput.close()
