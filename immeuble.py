# module immeuble

from couleur_aleatoire import couleur_aleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard

    '''
    # Nombre d'étage (aléatoire)
    nbEtage = randint(0,5)
    #nbEtage = randint(1,4)
    turtle.pensize(3)
    pass
    #Couleurs des éléments (aléatoire)
    c_facade = couleur_aleatoire()
    c_porte = couleur_aleatoire()
    pass
    # Dessin du RDC
    rdc(x , y_sol,c_facade,c_porte)
    pass
    # Dessin des étages
    for etage in range(nbEtage):
        etage(x , y_sol, c_facade, etage)
    for i in range(1,nbEtage):

        etage(x , y_sol, c_facade, i)
    pass
    # Dessin du toit
    toit(x, y_sol)
    toit(x, y_sol,nbEtage)
    pass


if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()