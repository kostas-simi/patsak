#! Python program that remove comments (with #) for a python code.
#! Created by Kostas Simiriotis, January 2019 for the Python test of the 1st semester.

print("Welcome to python comment remover, noComm1.0 by Kostas Simiriotis!")
filename = input("Please provide the location of the file: ")
name = filename.split(".py")
print("Opening the file...")
finput = open(filename, 'r')

foutput = open(name[0]+'_noComm'+'.py', 'w')
print("Removing comments...")
for line in finput:
    wholeline = False
    l = line.split("#")
    if len(l)>1 and ('"' in l[0]) and ('"' in l[1]):
        foutput.write(line)
        wholeline = True
    if len(l) > 1 and not wholeline and l[0] != "":
        l[0] += "\n"

    if (l[0] != "") and not wholeline:
        foutput.write(l[0])
finput.close()

foutput.close()
