from tkinter import font
from app.layouts.playlists_layout import *
from app.layouts.player_layout import *

class LibraryLayout : 
    pygame.init()

    # Constructeur
    def __init__(self, window, library):
        self.window = window
        self.library = library

    def show(self):
        font_text_button = font.Font(size=15, family=('Sans Serif'))
        music_list = self.library.get_music_list()
       
        def on_click_playlist():
            self.clear()
            PlaylistLayout(self.library).show()

        def on_click_music(event):
            supp_button.place(anchor = 'e', height= 40, width=210, x=self.window.winfo_height()+150,y=40)

        def on_double_click_music(event):
            music_clicked = self.library.find_music_by_name(music_space.get("anchor"))
            self.library.set_current_music(music_clicked)
            self.library.play_music(music_clicked)
            retrieve_player()

        def retrieve_player(): 
            PlayerLayout(self.window, self.library).show() 
            
        top_buttons = Frame(self.window, width=self.window.winfo_width(), height=80, bg="#141414")
        top_buttons.pack(side=TOP)
        
        import_button = Button(top_buttons, text="Importer des musiques", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : self.library.import_music(music_space))
        playlist_button = Button(top_buttons, text="Accéder aux playlists", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : on_click_playlist())
        supp_button = Button(top_buttons,text="🗑️ Supprimer", activebackground='#ff5e57', bg='#ff3f34', fg ='white', borderwidth=0, command=lambda : self.library.delete_music(music_space))
       
        import_button['font'] = font_text_button
        playlist_button['font'] = font_text_button
        supp_button['font'] = font_text_button
       
        import_button.place(anchor = 'w', height= 40, width=210, x=20, y=40)
        playlist_button.place(anchor = 'w', height= 40, width=210, x=300, y=40)
        supp_button.place_forget()
        
        musics_frame = Frame(self.window, width= 900, height= 400, bg="#141414")
        musics_frame.pack(padx= (30,30) ,pady=(20,40))
        
        scrollbar = Scrollbar(musics_frame, orient=VERTICAL)
        music_space = Listbox(musics_frame, fg="white",width=70,height=15, bg="#2f3542",font=('helvetica',18), selectbackground="#4b4b4b", relief=FLAT, selectforeground="white", highlightthickness=0, activestyle=NONE, yscrollcommand=scrollbar.set)
        scrollbar.config(command=music_space.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        music_space.pack(padx=10, pady=10)
        
        for music in music_list: 
            music_space.insert('end', music.get_title()) 
            
        music_space.bind("<Double-Button>", on_double_click_music)
        music_space.bind("<Button>", on_click_music)
         
    def clear(self):
        self.destroy()