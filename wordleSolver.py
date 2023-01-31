WORD_LENGTH = 6
alphabet = "abcdefghijklmnopqrstuvwxyz"

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

words = loadWords("fiveLetter.txt")
#words = includeLetter(words, "d")
#words = includeLetter(words, "a")
#words = includeLetter(words, "i")
#words = includeLetter(words, "y", 4, True)
