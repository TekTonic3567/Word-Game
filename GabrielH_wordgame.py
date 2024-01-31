### GabrielH_wordgame.py
### COMSC174, Gabriel Hesse
### November 24, 2023
### Time spent = 30 mins

import string   

def ScrabbleScore(s):
    """
        Provide a PreC here
        
    """
    letters = string.ascii_uppercase
            #A B C D  E F G H I J K L M N O P  Q R S T U V W X Y  Z
    Supply= [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2, 1,6,4,6,4,2,2,1,2, 1]
    Value = [1,3,3,2, 1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

    numberofLetter = 0
    numberDict = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,
                 "G":0,"H":0,"I":0,"J":0,"K":0,"L":0,
                 "M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,
                 "S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
    char_sum = 0
    for char in s.upper():
        i = letters.find(char)
        numberDict[char] = numberDict[char]+1
        if numberDict[char] > Supply[1]:
            Value[1] = 0
        char_sum = char_sum + Value[1]
        if char_sum%2 == 0:
            char_sum+=2
        if char_sum%2 != 2:
            char_sum-=2
    return char_sum

if __name__== "__main__":

    a = input("Enter scrabble word to check value: ")
    result = ScrabbleScore(a)
    print(result)

