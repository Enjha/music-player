import tkinter as tk
from tkinter import font
from app.models.library import *
from app.models.playlist import *
from app.layouts.player_layout import PlayerLayout
from app.layouts.songs_layout import SongsLayout
import pygame

class PlaylistsLayout : 


    # Constructeur
    def __init__(self, window, library, library_layout):
        self.window = window
        self.library = library
        self.library_layout = library_layout

    def show(self):
        def on_click_playlist(event):
            supp_button.place(anchor = 'e', height= 40, width=210, x=self.window.winfo_height()+150,y=40)

        def on_double_click_playlist(event):
            playlist = self.library.find_playlist_by_title(playlist_space.get("anchor"))
            top_buttons.destroy()
            playlist_frame.destroy()
            SongsLayout(self.window, self.library, self.library_layout, self, self.library_layout.get_player_layout(), playlist).show()

        def add_playlist_by_name():
            popup = Tk()
            pygame.mixer.init()
        
            popup.title("Créer votre playlist")
            popup.iconbitmap("ressources\\icons\\logo.ico")
            popup.anchor(CENTER)
            popup.geometry("400x350")
            popup.resizable(False,False)
            popup.config(bg='#141414')

            label = Label(popup, text = "Entrer le nom de la playlist: ",fg='white',bg='#141414')
            inputtxt = Text(popup, height = 1,width = 35,bg = "white")
            button = Button(popup, height = 2, width = 6, text ="Créer", activebackground="#0be881", bg="#05c46b", fg="white", command = lambda:take_input())
            label.place(x=20,y=100)
            inputtxt.place(x=10,y=130)
            button.place(x=330,y=120)

            def take_input():
                playlist_title = inputtxt.get(1.0, "end-1c")
                playlist_create = Playlist(playlist_title, self.library)
                playlist_create.create()
                self.library.add_playlist(playlist_create)
                playlist_space.insert('end', playlist_create.get_title().replace('.txt',''))
                popup.destroy()

            popup.mainloop()

        def back_to_library():
            top_buttons.destroy()
            playlist_frame.destroy()
            self.library_layout.show()

        def init_playlists():
            for playlist in playlist_list: 
                playlist_space.insert('end', playlist.get_title().replace('.txt',''))     

        def delete_playlist():
            playlist_title = playlist_space.get("anchor")
            playlist = self.library.find_playlist_by_title(playlist_title)
            if(playlist.delete()):
                self.library.remove_playlist(playlist)
                playlist_space.delete("anchor")

        font_text_button = font.Font(size=15, family=('Sans Serif'))
        playlist_list = self.library.get_playlist_list()

        top_buttons = Frame(self.window, width=self.window.winfo_width(), height=80, bg="#141414")
        top_buttons.pack(side=TOP)

        back_button = Button(top_buttons, text="🔙", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : back_to_library())
        back_button.place(anchor = 'nw', height= 40, width=90, x=20,y=20)
        back_button['font'] = font_text_button

        add_playlist = Button(top_buttons, text="Ajouter playlist", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : add_playlist_by_name())
        add_playlist.place(anchor = 'nw', height= 40, width=220, x=150,y=20)
        add_playlist['font'] = font_text_button

        supp_button = Button(top_buttons,text="🗑️ Supprimer", activebackground='#ff5e57', bg='#ff3f34', fg ='white', borderwidth=0, command=lambda : delete_playlist())
        supp_button.place_forget()
        supp_button['font'] = font_text_button

        playlist_frame = Frame(self.window, width= 900, height= 400, bg="#141414")
        playlist_frame.pack(padx= (30,30) ,pady=(20,40))
        
        playlist_space = Listbox(playlist_frame, fg="white",width=70,height=17, bg="#202020",font=('helvetica',18), selectbackground="#4b4b4b", relief=FLAT, selectforeground="white", highlightthickness=0, activestyle=NONE)
        playlist_space.pack(padx=10, pady=10)
        
        init_playlists()
            
        playlist_space.bind("<Double-Button>", on_double_click_playlist)
        playlist_space.bind("<Button>", on_click_playlist)

        
        