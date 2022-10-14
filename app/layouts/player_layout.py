from tkinter import *
from tkinter import font
import pygame

class PlayerLayout : 

    # Constructeur
    def __init__(self, window, library):
        self.window = window
        self.library = library

    #Permet d'afficher le player 
    def show(self):

        font_text_button = font.Font(size=20, family=('Comic Sans MS'), weight=font.BOLD)  
        #Permet de rassembler les boutons du player
        player_frame = Frame(self.window, width=self.window.winfo_width(), height=60, bg="#141414")
        player_frame.pack(side=BOTTOM)
        #Nom de la musique courante à afficher
        music_title = Label(player_frame, text= self.library.get_current_music().get_title() ,bg='#141414', fg='white', font=('poppin',22))
        music_title.pack()

        buttons = Frame(player_frame, bg='#141414')
        buttons.pack(anchor='center') 
        #Différents boutons du player
        prev_button = Button(player_frame, text="⏮", bg='#141414', fg='white',borderwidth=0, command=lambda : previous_music())
        prev_button.pack(padx=8, pady=10, in_=buttons, side=LEFT)
        prev_button['font'] = font_text_button   
        
        play_pause_button = Button(player_frame, text="⏸", bg='#141414', fg='white',borderwidth=0, command=lambda : play_pause_music())
        play_pause_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        play_pause_button['font'] = font_text_button   

        next_button = Button(player_frame, text="⏭", bg='#141414', fg='white',borderwidth=0, command=lambda : next_music())
        next_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        next_button['font'] = font_text_button  

        back_to_start = Button(player_frame, text="↻", bg='#141414', fg='white',borderwidth=0, command=lambda : back_to_start())
        back_to_start.pack(padx=8, pady=10, in_=buttons, side=LEFT)
        back_to_start['font'] = font_text_button   
        
        #Méthode permettant de passer à la musique suivante
        def next_music():
            play_pause_button["text"]= "⏸"
            next_music = self.library.get_next_music(self.library.get_current_music())
            self.library.set_current_music(next_music)
            self.library.play_music(next_music)
            music_title["text"] = next_music.get_title()
            
        #Méthode permettant de passer à la musique précédente
        def previous_music():
            play_pause_button["text"]= "⏸"
            previous_music = self.library.get_previous_music(self.library.get_current_music())
            self.library.set_current_music(previous_music)
            self.library.play_music(previous_music)
            music_title["text"] = previous_music.get_title()
            
        #Méthode permettant de recommencer une musique au départ 
        def back_to_start():
            self.library.play_music(self.library.get_current_music())
        
        #Permet de lire une musique 
        def play_pause_music():
            if(play_pause_button["text"]== "⏸"):
                pygame.mixer.music.pause()
                play_pause_button["text"] = "▶️"
            else:
                pygame.mixer.music.unpause()
                play_pause_button["text"]= "⏸"

        #Méthode permettant de savoir quand une musique est terminée afin de lancer la suivante.
        def check_event():
            for event in pygame.event.get():
                if event.type == MUSIC_END:
                    next_music()
            self.window.after(100,check_event) 

        MUSIC_END = pygame.USEREVENT+1
        pygame.mixer.music.set_endevent(MUSIC_END)

        check_event()
        
    def clear(self):
        self.destroy()