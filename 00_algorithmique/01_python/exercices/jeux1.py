# on a pour depart, un chiffre aleatoire qui est choisi
# apres, le jeu nous demande de taper un nombre entre 0 et 100
# si la reponse est inferieur au nombre aleatoire
# il doit afficher "le nombre est plus grand"
# si la reponse est superieur au nombre aleatoire
# il doit afficher " le nombre est plus petit"
# et sinon, vous avez gagné

# ici, on importe une libraire qui contient    
# des fonctions aleatoires
import random

# initialise nos variables nbAleatoire et trouver
# nb aleatoire sera generer par l'ordinateur
# trouver est un boolean qui est egale a Faux
nbAleatoire = random.randrange(0,100)
trouver = False

# Tant que trovuer est egale a Faux, on continue
while trouver == False:
    print("tape un nombre entre 0 et 100")
    # on convertit le nombre taper au clavier en int
    reponse = int( input() )
    
    # on compare notre reponse avec le nb aleatoire
    if reponse < nbAleatoire :
        print("le nombre est plus grand")
    elif reponse > nbAleatoire :
        print("le nombre est plus petit")
    else :
        print("Vous avez gagné !")
        # on passe trouver a Vrai pour arreter la boucle
        trouver = True