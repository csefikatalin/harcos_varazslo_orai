""" adattagok: nev, poz, kaszt, hp - nem kívülről kapja, hanem egy belső fv-ény adja meg.  """

import random
class Jatekos:
    def __init__(self,nev:str="Játékos",poz:int=0,kaszt:str="harcos", emo:str="H" ):
        self.nev=nev
        self.poz=poz
        self.kaszt=kaszt
        self.emo=emo
        self.hp=3+random.randint(1,6)

    """  pozíció beállítása tagfüggvény set_pozicio  - setter"""
    def set_pozicio(self):
        self.poz=random.randint(0,2)

    def set_hp(self):
        self.hp=self.hp-random.randint(0,1)

    def __str__(self):
        return f"Név: {self.nev}, Pozíció: {self.poz}, Kaszt: {self.kaszt}, HP: {self.hp}, karkter: {self.emo}" 

