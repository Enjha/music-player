import tkinter as tk
from tkinter import font
from app.models.library import *
from app.models.music import *
from app.layouts.library_layout import LibraryLayout
from app.layouts.player_layout import PlayerLayout

class PlaylistLayout : 

    # Constructeur
    def __init__(self, window, library):
        self.window = window
        self.library = library

    def show(self):
        font_text_button = font.Font(size=15, family=('Sans Serif'))

        top_buttons = Frame(self.window, width=self.window.winfo_width(), height=80, bg="green")
        top_buttons.pack(side=TOP)

        back_button = Button(top_buttons, text="🔙", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : back_to_library())
        back_button.place(anchor = 'nw', height= 40, width=90, x=20,y=20)
        back_button['font'] = font_text_button

        def back_to_library():
            self.clear()
            LibraryLayout(self.window).show()
            PlayerLayout(self.window).show()
        
    def clear(self):
        self.destroy()