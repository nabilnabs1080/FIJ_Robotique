#il existe 3 types de variable sous python

variable1 = 5 #integer > int qui symbolise un nombre entier
variable2 = 3.2 # float > float qui symbolise un chiffre a virgule
variable3 = "Coucou" # string > str qui symbolise du texte 
variable4 = True #boolean > bool symbolise une variable soit vrai 
                #soir faux
variable5 = ["1er","2eme","3eme"] #list > une variable liste qui 
                                  #comprend 3 string

#première fonction qui permet d 'afficher du texte a l'écran

print("texte",variable1, variable2, variable3, variable4)

#Fonction permetant de connaitre le type d'une variable
print(type(variable1) )

typeDeVariable = type(variable1)

print("le type de la variable1 =", typeDeVariable)

variable1 = str(variable1)
typeDeVariable = type(variable1)
typeDeVariable = type(variable1)
print("le type de la variable1 =", typeDeVariable)

# En python, il existe plusiseurs operateurs
#addition            > +
# soustraction       > -
# multiplication     > *
# l'exposant         > **
#  division          > /
# division entière   > //
# modulo             > %