import tkinter as tk
import pygame

from tkinter import *

from app.layouts.player_layout import PlayerLayout

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

        player_layout = PlayerLayout(window)
        player_layout.print()

        # Affichage de la fenêtre créée :
        window.mainloop()
