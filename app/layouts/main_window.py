import tkinter as tk
import pygame

from tkinter import *

from app.layouts.library_layout import LibraryLayout
from app.layouts.player_layout import PlayerLayout
from app.models.library import Library

class MainWindow (tk.Tk): 
    
    title = ""  

    # Constructeur
    def __init__(self, title):
        self.title = title

    def init_window(self):
        window = Tk()
        pygame.mixer.init()
        
        # Ajout d'un titre à la fenêtre principale :
        window.title(self.title)
        window.iconbitmap("ressources\\icons\\logo.ico")
        window.anchor(CENTER)
        window.geometry("1000x800")
        window.resizable(False,False)
        window.config(bg='#141414')
        window.maxsize(1500,1500)
        window.minsize(600,750)

        library = Library()
        player_layout = PlayerLayout(window, library)
        library_layout = LibraryLayout(window, library, player_layout)
        library_layout.show()

        # Affichage de la fenêtre créée :
        window.mainloop()