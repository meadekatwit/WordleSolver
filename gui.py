import tkinter as tk
import wordleSolver
from tkinter import ttk


root = tk.Tk()
root.resizable(True, True)
root.title("Scrollbar Widget Example")

global chosenWord
chosenWord = "     "

def getRandomWord():
    global chosenWord
    chosenWord = wordleSolver.randomWord(wordleSolver.words)
    label_random.delete(1.0, 'end')
    label_random.insert(1.0, chosenWord)

label_random = tk.Text(root, height = 1, width = 5)
label_random.grid(row=1, column=0)

text_check = tk.Text(root, height = 1, width = 5)
text_check.grid(row = 2, column = 0)

def setTextBox(check = "", word = ""):
    try:
        if check != "     ":
            word = label_random.get(1.0, "end-1c")
            check = text_check.get(1.0, "end-1c")
        print("A: " + check)
        print("W: " + word)
        wordleSolver.words = wordleSolver.inputCheck(wordleSolver.words, word, check)
    except:
        pass

    text_wordList.delete(1.0, 'end')
    i = 0
    for word in wordleSolver.words:
        i += 1
        position = f'{i}.0'
        text_wordList.insert(position, f'{i}: {word}');



root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text_wordList = tk.Text(root, height=10, width = 11)
text_wordList.grid(row=1, column=1)

scrollbar = ttk.Scrollbar(root, orient='vertical', command=text_wordList.yview)
scrollbar.grid(row=1, column=2, sticky=tk.NS)

text_wordList['yscrollcommand'] = scrollbar.set

btn_word = ttk.Button(root, text = "Check word", command = setTextBox)
btn_word.grid(row=0, column=1)

btn_random = ttk.Button(root, text = "Pick word from list", command = getRandomWord)
btn_random.grid(row=0, column=0)

setTextBox(check = "     ")

root.mainloop()
