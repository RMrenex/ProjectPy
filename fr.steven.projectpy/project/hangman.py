import random


def getRandomWord():
    lines = open("words.txt").read().splitlines()
    word = random.choice(lines)
    return word


def hideWord(word):
    size = len(word)
    hidenWord = ""
    for i in range(size):
        hidenWord += "_"
    return hidenWord


def charposition(string, char):
    index = []
    for i in range(len(string)):
        if string[i] == char:
            index.append(i)
    return index


def replace_char_at_index(org_str, index, replacement):
    new_str = org_str

    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str


def replace_char_all_index(baseStr, indexList, letter):
    for index in indexList:
        baseStr = replace_char_at_index(baseStr, index, letter)
    return baseStr


def checkWin(word):
    if not word.__contains__("_"):
        return True
    else:
        return False


def isCorrect(letter):
    correct = False
    if len(letter) == 1:
        if not letter.isdigit():
            correct = True
        else:
            print(">>> Error : please enter an letter")
    else:
        print(">>> Error : please enter one letter")
    return correct


def start():
    currentWord = getRandomWord().upper()
    hiddenWord = hideWord(currentWord)
    fail = 0
    while fail < 6:
        if not checkWin(hiddenWord):
            print(f"guess the word {hiddenWord}")
            userResponse = str(input(">>> Guess your letter : ")).upper()

            if isCorrect(userResponse):

                if userResponse in currentWord:
                    positions = charposition(currentWord, userResponse)
                    hiddenWord = replace_char_all_index(hiddenWord, positions, userResponse)
                else:
                    fail += 1
                    print(f">>>Incorrect! You have {fail}/6")
            else:
                print("")
        else:
            print(f"Congratulation the word was {currentWord}")
            break
    if fail == 6:
        print(f"Sorry the word was {currentWord}")


start()
