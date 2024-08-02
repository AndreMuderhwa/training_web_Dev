# def hello():  #methodes
#     print("Hello")

# def fun():
#     return "Hello"

# #hello()
# print(fun())

# def Somme(a, b):
#     return a+b

# print(Somme(3,7))
import math

def Number(n):
    Nums=[]
    i=1
    while i<=10:
        response=f"{n}X{i}={n*i}"
        Nums.append(response)
        i=i+1
    s=" ".join(Nums)
    return s



print(Number(12))
