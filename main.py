# AIM: Write a Python program that takes two 
# numbers as input and performs division. 
# Implement exception handling to manage division 
# by zero and invalid input errors gracefully.
# Coder: mohammed ayaan shaikh 
# Date: 16/02/26



#print("--- Extracting Words from Text File ---\n")
num = int(input("enter word length: "))
words =[]
with open("story.txt", "r") as file:
    content = file.read().split()
    for i in content:
        if len(i) == num:
            words.append(i)
words=set(words)
words=list(words)
words.sort()
print(words)
