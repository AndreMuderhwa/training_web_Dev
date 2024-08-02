# print("Bienvenue dans le Terminal")
# nom = input("Saisi ton nom \n")
# age= int(input("Saisi ton age \n"))

# if age >= 18:
#     print(f"Votre nom est {nom}\n Votre age est {age}, Donc vous etes Majeur")
# elif age == 30:
#     print("Debut de la vieillesse")
# else:
#     print(f"Votre nom est {nom}\n Votre age est {age}, Donc vous etes Mineur")



# i=1
# a=0
# while i<11:
#     while a <= 5:
#         m="Bonjour"
#         a=a+1
#     print(f"Hell0 {m}")
#     i=i+1

# for a in range(10):
#     print("Bonjour")

# nombre = int(input("Saisir un nombre \n"))
# i=1
# while i <11:
#     print(f"{nombre} X {i} = {nombre*i}")
#     i=i+1
# for i in range(10):
#     print(f"{nombre} X {i+1} = {nombre *(i+1)}")

# i=1
# while i<11:
#     print("Hello")

# while True:
#     print("Hello")



#DEVINETTE
# nomAdeviner="Timothee"

# while True:
#     nom=input("Deviner le nom \n")
#     if nom == nomAdeviner:
#         print("Bravo tu as reussi")
#         break
#     else:
#         re=input("Voulez-vous continuer ?? O/N \n")
#         if re == 'O' or re=='o':
#             continue
#         elif re=='N' or re=='n':
#             break
#         else:
#             print("Mauvais choix !")
#             break

#TABLE DE MULTIPLICATION DE 12


# for i in range(12):
#     for j in range(12):
#         print(f"{(i+1)} X {(j+1)} = {(i+1)*(j+1)}")

# i=1
# j=1
# while i<13:
#     while j <13:
#         print(f"{i} X {j} = {i*j}")
#         j=j+1
#     i=i+1
#2em question
# nb1 =int(input("Saisi le premier nombre \n"))
# nb2 =int(input("Saisi le deuxieme nombre \n"))
# for i in range(nb2):
#     print(f"{nb1} X {(i+1)} = {nb1 * (i+1)}")

#LES LISTES
# MyList=[]       # liste vide
# maListe=list()   # liste vide

#MaListe =['Timotee', 'Julien', 'Jean Robert', 'Jean de la croix', 'Andre KIM']
# print(MaListe[2:4])
#n=[q for q in MaListe if MaListe[q] !=0 and MaListe[q] !=4]
# print((f"{MaListe[0]} , {MaListe[4]}"))
#MaListe[1]='Jacques'
# MaListe.append("JACQUES VERNEAU")

# for i in MaListe:
#     print(i)

# newList=[MaListe[0],MaListe[-1]]
# newList =[MaListe[i] for i in [0,-1]]
# print(newList)

# ListeNombre=[23,45,67,90,11.3,68,900]
# #premier element de la liste
# print(f"Premier element : {ListeNombre[0]}")
# #dernier element
# #print(f"Dernier element : {ListeNombre[6]}")
# print(f"Dernier element : {ListeNombre[-1]}")
# #ajouter une valeur
# ListeNombre.append(2024)
# #supprimer une valeur
# ListeNombre.remove(900)
# print(ListeNombre)

# Maliste=[1,2,3,4,5,6,7,8,9,10]
# print(Maliste[3:7])
#DICTIONNAIRE

# MonDico={}
# MyDico=dict()
# MonDico={
#     "nom": "Tim",
#     "age":32,
#     "adresse":"Goma",
#     "profession" :"Etudiant",
#     "institution":"ISIG-GOMA",
#     "promotion": "LIC3",
#     "faculte":"LIAGE",
#     "numeroTel":"+243 991 900 843"
# }

#print(MonDico.keys())
#print(MonDico.values())
# MonDico["faculte"] ="LSI"
# print(MonDico.get('numeroTel'))


# DicoAnglFR={}
# for i in range(2):
#     mot_angl=input("Saisi un mot en anglais \n")
#     mot_fr=input(f"Saisissez l'equivalent de {mot_angl} en francais \n")
#     DicoAnglFR[mot_angl]=mot_fr

# search=input("Rechercher un mot \n")
# if search in DicoAnglFR.keys():
#     print(f"L'equivalent de {search} en francais c'est {DicoAnglFR.get(search)}")

# elif search in DicoAnglFR.values():
#     newSearch=[q for q in DicoAnglFR if DicoAnglFR[q]==search]
#     newString="".join(newSearch)
#     print(f"l'equivalent de {search} en anglais c'est {newString}")
# else:
#     print(f"Le mot {search} est introuvable !")

#LES  MODULES 
# import math
# from math import sqrt
# from random import randint
# #print(math.sqrt(9))
# print(sqrt(9))
# print(randint(1,9))


# def sayHello1():      #+++> METHODE
#     print('Hello')

# def sayHello2():         #====> Fonction
#     return 'Hello'


# sayHello1()

# print(sayHello2())