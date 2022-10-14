from tkinter import *
from tkinter import font
from app.layouts.playlists_layout import *

class SongsLayout : 

    # Constructeur
    def __init__(self, window, library, library_layout, playlists_layout, player_layout, playlist):
        self.window = window
        self.library = library
        self.library_layout = library_layout
        self.playlists_layout = playlists_layout
        self.player_layout = player_layout
        self.playlist = playlist

    #Affiche les musiques dans les playlists.
    def show(self):

        # Déclenchée lors d'un évènement activé avec un double clic
        def on_double_click_music(event):
            music_clicked = self.library.find_music_by_name(music_space.get("anchor"))
            self.library.set_current_music(music_clicked)
            self.library.play_music(music_clicked)
            if(len(self.window.children) <= 2):
                self.player_layout.show()  
        
        # Fait apparaitre le boutons supprimer quand on clique sur une musique 
        def on_click_music(event):
            supp_button.place(anchor = 'e', height= 40, width=210, x=self.window.winfo_height()+150,y=40)

        # Permet de retourner à la liste des playlists
        def back_to_playlists():
            top_buttons.destroy()
            musics_frame.destroy()
            self.playlists_layout.show()

        # Nous n'avons pas eu le temps...
        def add_music():
            pass   

        # Permet de supprimer une musique de la playlist uniquement. 
        def remove_music():
            self.playlist.remove_music_by_index(music_space.curselection()[0]) 
            music_space.delete(music_space.curselection()[0])

        # Interface ui similaire à celle de la main window :
        font_text_button = font.Font(size=15, family=('Sans Serif'))
        music_list = self.library.get_music_list()

        top_buttons = Frame(self.window, width=self.window.winfo_width(), height=80, bg="#141414")
        top_buttons.pack(side=TOP)
        
        back_button = Button(top_buttons, text="🔙", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : back_to_playlists())
        
        add_button = Button(top_buttons, text="Ajouter des musiques", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : add_music())
        supp_button = Button(top_buttons,text="🗑️ Retirer", activebackground='#ff5e57', bg='#ff3f34', fg ='white', borderwidth=0, command=lambda : remove_music())
       
        add_button['font'] = font_text_button
        supp_button['font'] = font_text_button
        back_button['font'] = font_text_button
       
        back_button.place(anchor = 'nw', height= 40, width=90, x=20,y=20)
        add_button.place(anchor = 'w', height= 40, width=220, x=150, y=40)
        supp_button.place_forget()
        
        musics_frame = Frame(self.window, width= 900, height= 400, bg="#141414")
        musics_frame.pack(padx= (30,30) ,pady=(20,40))
        
        music_space = Listbox(musics_frame, fg="white",width=70,height=17, bg="#202020",font=('helvetica',18), selectbackground="#4b4b4b", relief=FLAT, selectforeground="white", highlightthickness=0, activestyle=NONE)
        music_space.pack(padx=10, pady=10)
        
        music_space.delete(0,END)
        
        # Permet d'afficher les musiques 
        self.playlist.init_music_list()
        for music in self.playlist.get_music_list(): 
            music_space.insert('end', music.get_title()) 
            
        music_space.bind("<Double-Button>", on_double_click_music)
        music_space.bind("<Button>", on_click_music)

        # Méthode permettant de savoir quand une musique est terminée afin de lancer la suivante.
        def check_event():
            for event in pygame.event.get():
                if event.type == MUSIC_END:
                    self.player_layout.next_music()
            self.window.after(100,check_event) 

        MUSIC_END = pygame.USEREVENT+1
        pygame.mixer.music.set_endevent(MUSIC_END)

        check_event()

    # Destruction de la fenêtre
    def clear(self):
        self.destroy()