Python program to change case of the String
String = input('Enter the string :')
String1 = str()
for i in String:
    if i.isupper():
        i = i.lower()
        String1 = String1 + i
    else:
        i = i.upper()
        String1 = String1 + i
#print String1
print(String + ' after changing ' + String1)
