text = input()
text = text.split(" ")

newtext = ""

for x in text:
    newtext += x[::-1]
    newtext += " "

print(newtext[:-1])