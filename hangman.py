#Hangman with swedish fruits and berries, 65 words
import random
import os

hangmanlist = [ "äpple", "apelsin", "banan", "jordgubbe", "kiwi",
                "mango", "ananas", "blåbär", "vattenmelon", "citron",
                "persika", "päron", "plommon", "körsbär", "granatäpple",
                "hallon", "melon", "mandarin", "nektarin", "aprikos",
                "papaya", "passionsfrukt", "kaktusfikon", "kivifrukt", "avokado",
                "klementin", "kokosnöt", "fikon", "körsbärstomat", "druva",
                "citronmeliss", "vinbär", "vindruva", "maracuja", "tranbär",
                "lingon", "apelsinmeliss", "litchi", "kumquat", "boysenbär",
                "fläderbär", "gojibär", "guava", "nashipäron", "svartvinbär",
                "rabarber", "kiwanobär", "citronverbena", "clementin", "longan",
                "stjärnfrukt", "pomelo", "soursop", "sapote", "physalis",
                "citronkaktus", "kiwanomelon", "rönnbär", "kastanj", "kvitten",
                "fikonkaktus", "fikon", "körsbärspaprika", "acaibär", "ackee" ]

# Controls if the character "charGuess" exists in the word "theWord"
def doesCharExist(theWord, charGuess, rightGuess):
    exist = False
    for i in range(0,len(theWord)):
        if theWord[i] == charGuess:
            rightGuess[i] = charGuess
            exist = True
    return exist

# Controls if the player has won the game
def checkIfRight(rightGuess):
    gamewin = True
    for i in range(0,len(rightGuess)):
        if rightGuess[i] == "*":
            gamewin = False
    if gamewin:
        print("Du vann!!! Bra jobbat.")        
    return gamewin

# Starts the game Hangman
def playHangMan():
    index = random.randint(0,64)
    theWord =hangmanlist[index]
    thewordLength = len(theWord)
    rightGuess = ["*"] * len(theWord)
    numOfGuesses = 0

    print(f"\nOrdet du skall gissa är på {thewordLength} bokstäver. \nDu får tio felaktiga gissningar på dig innan spelet avslutas.")
    
    while numOfGuesses < 11 and not checkIfRight(rightGuess):
        charGuess = input('Gissa på en bokstav:')
        os.system('cls')
        if len(charGuess) == 1 and charGuess.isalpha():
            
            if doesCharExist(theWord, charGuess, rightGuess):
                print(f"Bokstaven {charGuess} finns i ordet:      {rightGuess}")
            else:
                print(f"Bokstaven {charGuess} finns inte i ordet: {rightGuess}")    
                numOfGuesses += 1

        else:
            print("Mata bara in en bokstav:")
            continue
        
        hangmanGrapic(numOfGuesses)
    if numOfGuesses == 11:
        print(f"\nTyvärr du förlorade. Det rätta ordet var {theWord}. \n")

def hangmanGrapic(x):
    if x == 0:
        print('   ',  '      ')
        print('   ',  '      ')
        print('   ',  '      ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 1:
        print('   ',  '      ')
        print('   ',  '      ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 2:
        print('   ',  '      ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 3:
        print('   ',  '------')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 4:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 5:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')        
    if x == 6:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   - ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')    
    if x == 7:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 8:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 9:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|    ')
        print('------------')     
    if x == 10:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|   / ')
        print('------------')    
    if x == 11:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|   / \\')
        print('------------')
            
# Menu
while True:
    print("\n-------------------------")
    print("| Välj en åtgärd:       |")
    print("| 1. Spela \"hangman\"    |")
    print("| 2. Avsluta programmet |")
    print("-------------------------")

    choice = input('Ange ditt val (1-2):')

    if choice == '1':
        os.system('cls')
        playHangMan() 
    elif choice == '2':
        print('Programmet avslutas. Hej då!')
        break
    else:
        print('Ogiltigt val. Försök igen.')
