from math import pi
from math import sqrt


class Exercice_3:
    """
    Ecrire une classe qui renvoie des informations sur un cercle
    """

    def __init__(self, r):
        self.r = r

    def aire(self):
        """
        Ecrire une fonction qui renvoie l'aire d'un disque de rayon r
        L'aire d'un disque de rayon R est égale à : π × R × R.
        """
        print(pi*self.r*self.r)
        return pi*self.r*self.r

    def perimetre(self):
        """
        Ecrire une fonction qui renvoie le perimètre d'un cercle de rayon r
        périmètre du cercle = 2 x pi x rayon
        """
        print(2 * pi * self.r)
        return 2 * pi * self.r

    def dans_cercle(self, x, y):
        """
        Ecrire une fonction qui renvoie True si le point (x, y) est dans
        le cercle de r et de centre (0, 0)
        """
        res = x**2 + y**2
        if sqrt(res) <= self.r:
            return True
        else:
            return False
