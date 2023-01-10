#Gets string and sets all letters to lowercase
sentence = input("Type sentence: ")
sentence = sentence.lower()

#Splits string by each word
words = sentence.split()

#Creates an empty newSentence string and an error boolean
newSentence = ""
error = False

#Loops through each word, capitalizes it, and adds it to the newSentence string
for word in words:
    if not word.isalpha(): #If first character is not a letter, prints an error and breaks loop
        print("Error: All words must start with a letter")
        error = True
        break
    newSentence += word.title()

#Prints string if no error
if not error:
    print(newSentence)