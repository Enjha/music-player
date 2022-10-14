from tkinter import *

#Classe permettant la gestion des musiques lors de la lecture
class Music (object):
    # Chemin pour le fichier des musiques.
    global LIBRARY_PATH
    LIBRARY_PATH = "ressources\songs"

    title = "" # titre de la musiques
    duration = 0 # durée de la musiques
    
    # Constructeur
    def __init__(self, title, duration, library):
        self.title = title
        self.duration = duration
        self.library = library

    # Getter du titre, et de la durée de la musique
    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration

    # Méthode équals classique
    def equals(self, music):
        if self.title == music.get_title() and self.duration == music.get_duration():
            return True
        else:
            return False