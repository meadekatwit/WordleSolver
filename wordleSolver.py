import random

WORD_LENGTH = 6

words = []

def initialClear(fileName, outputFile = ""):
    if outputFile == "":
        outputFile = fileName
    
    f = open(fileName)
    words = f.readlines()
    f.close()

    ln = len(words)

    f = open(outputFile, "w")
    
    i = 0
    for word in words:
        if len(word) != WORD_LENGTH: #Remove improper word lengths
            words.remove(word)
        elif not word.rstrip().isalpha(): #Remove improper word sizes
            words.remove(word)
        else:
            f.write(word.lower())

        i += 1
        if i % (ln // 100) == 0:
            print(str(i // (ln // 100)) + "%")

    f.close()

#initialClear("words.txt", "fiveLetter.txt")

def loadWords(fileName):
    f = open(fileName)
    words = f.readlines()
    f.close()
    return words

def clearLetter(words, letter):
    newWords = words.copy()
    for word in words:
        if letter in word:
            newWords.remove(word)
    return newWords

def includeLetter(words, letter, position = -1, force = False):
    newWords = words.copy()
    for word in words:
        if force:
            if not (word[position] == letter): 
                newWords.remove(word)
        else:
            if not (letter in word and word[position] != letter):
                newWords.remove(word)
    return newWords

def inputCheck(words, inp, check):

    #print(check)
    
    prevLength = len(words)
    prevGreen = []
    
    for i in range(WORD_LENGTH - 1):
        #print(check[i])
        if check[i] == "g":
            words = includeLetter(words, inp[i], i, True)
            prevGreen.append(inp[i])
        elif check[i] == "y":
            words = includeLetter(words, inp[i], i, False)
        elif check[i] == "b" and not (inp[i] in prevGreen):
            words = clearLetter(words, inp[i])

    print("Cut words from " + str(prevLength) + " to " + str(len(words)) + ". (" + str((1 - len(words) / prevLength) * 100) + "% cut)")
    return words

def randomWord(words):
    noRep = []
    for word in words:
        letters = []
        for letter in word:
            if not letter in letters:
                letters.append(letter)
        #print(str(len(letters)) + " " + word)
        if len(letters) == WORD_LENGTH:
            noRep.append(word)

    if len(noRep) > 0:
        return random.choice(noRep)
    return random.choice(words)

words = loadWords("fiveLetter.txt")
