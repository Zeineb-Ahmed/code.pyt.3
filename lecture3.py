#nombre pair ou impair
""" nombre=int(input("donner un nombre"))
if(nombre%2==0):
    print("nombre pair")
else:
    print("nombre impair") """
#table de multiplication
""" nombre=int(input("donner un nombre"))
 """"""
print(nombre*0)
print(nombre*1)
print(nombre*2)
print(nombre*3)
print(nombre*4)
print(nombre*5)
print(nombre*6)
print(nombre*7)
print(nombre*8)
print(nombre*9)
print(nombre*10)
 """
""" for  compteur in range(0,11):
    print(nombre*compteur) """
#excercice mot de passe 
""" password=""
while(len(password)<10):
    password=input("donner votre mot de passe ") """
""" for nombre in range(0,101):
    if((nombre%3==0) and (nombre%5==0)):
        print("FizzBuzz")
    elif((nombre%3==0) and (nombre%5!=0) ):
        print("Fizz")
    elif((nombre%3!=0) and (nombre%5==0)):
        print("Buzz")
    else :
        print(nombre)
 """
#un nombre divisible que par un et lui meme 
#7
""" nombre=int(input("donner un nombre "))
 """#methode 1
#9 2 3 4 5 6 7 8 
""" premier=True
diviseur=2


while((premier==True) and (diviseur<nombre)):
    if(nombre%diviseur==0):
        print("nombre non premier")
        premier=False
    else:
        diviseur=diviseur+1
if(premier==True):
    print("le nombre est premier")
else:
    print("le nombre n'est pas premier")
 """
# 17
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 
#8 
#1 2 3 4
#diviseurs=0+1=1+1=2
""" diviseurs=0
for divi in range(1,nombre+1):
    if(nombre%divi==0):
        diviseurs=diviseurs+1
if(diviseurs==2):
    print("le nombre est premier")
else:
    print("le nomber n'est pas premier") """
#### lire un nombre N donne par l'utilisateur  entre 5 et 12
### lire N nombres entre 10 et 100
    ### afficher la somme de ces N nombres
    ### afficher le maximum de ces nombres
    ### afficher le minimum de ces nombres
    ### afficher le moyenne de ces nombres

"""
7
3 6 5 8 9 8 7
la somme est 37

la moyenne est 6,...
"""
""" n=0



while((n<5) or (n>12)):
    n=int(input("donner le nombre N"))
somme=0

for compteur in range(0,n):
    x=0

    while((x<10) or (x>100)):
        print("donner le ",compteur+1," ieme nombre")
        x=int(input())
    somme=somme+x

print("la somme est ",somme)
print("la moyenne est ",(somme/n)) """
# genrer un nombre aleatoire entre 1 et 300
#demander a l'utilisateur de donner un nombre 
# si le nombre donnee est plus grand que le nombre generee alors afficher "le nombre donne est grand"
# si le nombre donnee est plus petit que le nombre generee alors afficher "le nombre donne est petit"
# le jeux s'arrete lorsque l'utilisateur donne une bonne suggestion


# cachee=225
# sugg=300 -->  grand
# sugg=200 -->  petit
# sugg=225 --> bravo
""" 
import random
nombreCachee=random.randint(1,300)
print(nombreCachee)

dev=0

while(nombreCachee!=dev):
    dev=int(input("donner une suggestion "))
    if(dev>nombreCachee):
        print("la valeur quye vous avez donnee est plus grande ")
    elif(dev<nombreCachee):
        print("le nombre que vous avez donnee est plus petit ")
    else:
        print("bravo vous avez devinee le nombre cachee ")
 """
nombre=int(input("donner un nombre de 3 chiffres "))
# 124
# 1+2+4=7
# 4 = nombre%10
# 124  124/10 -->12
# 2= 12%10
# 12   12/10--1
# 1 --> 1%10 
somme=0
reste=nombre%10
nombre=int(nombre/10)
somme=somme+reste

reste=nombre%10
nombre=int(nombre/10)
somme=somme+reste

reste=nombre%10
somme=somme+reste
print(somme)

#917
"""
somme=0

reste=917%10 --->reste=7
somme=0+7-->somme=7
nombre=917/10-->91

reste=91%10-->1
somme=7+1-->8
nombre=91/10-->9

reste=9%10-->9
somme=8+9-->17

"""