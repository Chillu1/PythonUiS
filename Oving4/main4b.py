infoDict = dict()

while True:
    filename = input("File with emails: ")
    try:
        file = open("Oving4/"+filename, "r")
        break
    except FileNotFoundError:
        print("File not found: " + filename + ", try again.")
listLines = file.readlines()

for currentLine in listLines:
    currentLine = currentLine.strip()
    
    if currentLine.startswith("From:"):
        domainStartIndex = currentLine.find("@")
        domainEndIndex = currentLine.find(">")
        domainName = currentLine[domainStartIndex:domainEndIndex]

        if domainName in infoDict:
            infoDict[domainName] += 1
        else:
            infoDict[domainName] = 1

print(infoDict)