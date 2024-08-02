from calculs import * 
from math import floor

def main():
    x1=float(input("Saisi le premier nombre \n"))
    x2=float(input("Saisi le deuxieme nombre \n"))
    s=input("Saisi le signe d'operation \n")
    if s == "+":
        print(f"La somme de {floor(x1)} et {floor(x2)} est {addition(x1,x2)}")
    elif s == "/":
        print(f"La division de {floor(x1)} et {floor(x2)} est {division(x1,x2)}")
    elif s == "*":
        print(f"La multiplication de {floor(x1)} et {floor(x2)} est {multiplication(x1,x2)}")
    else:
        print(f"L'operateur {s} est invalide !!")

def letterFrequency(phrase):
    frequency=dict()
    for letter in phrase:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter]=1
    
    return frequency

def wordFrequency(phrase):
    word=phrase.split(" ")
    return letterFrequency(word)



if __name__=="__main__":
    print(wordFrequency("papa maman"))
    



