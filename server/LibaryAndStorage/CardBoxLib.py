import time
import pyfiglet
import os

BLUE = "\033[38;5;27m"
GREEN = "\033[38;5;28m"
BOLD = "\033[1m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

def initialize():
    os.system("clear")
    print(HIDE_CURSOR)
    print(GREEN)
    print(textToASCIIArt("Card Box", "larry3d"))
    print(textToASCIIArt("System", "larry3d"))
    print(BLUE + "Made by user19735"+ GREEN + " " + BOLD)

def menu():
    print(textToASCIIArt("Menu", "chunky"))
    print("[1] Train\n[2] Add a new Word\n[3] Delete a Word\n[4] Quit")
    option = str(input("Which Option do you choose: "))
    os.system("clear")
    if option == "1" or option == "2" or option == "3" or option == "4":
        if option == "1":
            train()    
        elif option == "2":
            addNewWord()
            os.system("clear")
        elif option == "3":
            deleteWord()
        elif option == "4":
            Exit()

def textToASCIIArt(text, font):
        return pyfiglet.figlet_format(text, font = font)

def Exit():
    print(SHOW_CURSOR)
    os.system("clear")
    exit()

def addNewWord():
    word = str(input("Enter a Word: "))
    definition = str(input("Enter a definition: "))
    file = open("LibaryAndStorage/Words", "a")
    file.write(f"{word}\n{definition}\n")
    return input("Enter again to go back to menu")
    os.system("clear")

def train():
    terms = splitLines(openFileAndSplitLines("LibaryAndStorage/Words"))[0]
    definitions = splitLines(openFileAndSplitLines("LibaryAndStorage/Words"))[1]
    number = input(f"Which word do you want? You can choose from {len(terms)} Word(s): ")
    try:
        number = int(number)
    except:
        os.system("clear")
        menu()
    for i in range(len(terms)+1):
        if i == number:
            print(terms[i-1])
            question = input("Press Enter if you want to hear the definition")
            print(definitions[i-1])
            return input("Enter again to go back to menu")
            os.system("clear")

def deleteWord():
    WordToDelete = input("Enter the Word you want to delete: ")
    openFile = open("LibaryAndStorage/Words", "r")
    lines = openFile.read().splitlines()
    # iterate each line
    with open("LibaryAndStorage/Words", 'w') as fp:
        i = 0
        for line in lines:
            if(line == WordToDelete):
                break
            i += 1
        for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
            if number not in [i, i+1]:
                fp.write(line + "\n")

def openFileAndSplitLines(path):
    file = open(path, "r")
    return file.read().splitlines()

def splitLines(lines):
    counter = 0
    wordCounter = 0
    terms = []
    definitions = []
    upperBorderRange = int(len(lines)/2)
    for i in range(0,upperBorderRange):
        terms.append(lines[counter])
        definitions.append(lines[counter+1])
        counter+= 2
        wordCounter += 1
    return terms, definitions

if __name__ == "__main__":
    pass
