from tkinter import *
from tkinter import font
from pygame import mixer

class PlayerLayout : 

    # Constructeur
    def __init__(self, window, library):
        self.window = window
        self.library = library

    def show(self):

        font_text_button = font.Font(size=20, family=('Comic Sans MS'), weight=font.BOLD)

        label_zone = Frame(self.window, width=900, height=60, bg="#141414")
        label_zone.pack(side=TOP)
        music_title = Label(label_zone, text= self.library.get_current_music().get_title() ,bg='#141414', fg='white', font=('poppin',22))
        music_title.pack()
        
        player_frame = Frame(self.window, width=self.window.winfo_width(), height=40, bg="#141414")
        player_frame.pack(side=BOTTOM)

        buttons = Frame(player_frame, bg='#141414')
        buttons.pack(anchor='center') 
        
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
        
        def next_music():
            play_pause_button["text"]= "⏸"
            next_music = self.library.get_next_music(self.library.get_current_music())
            self.library.set_current_music(next_music)
            self.library.play_music(next_music)
            music_title["text"] = next_music.get_title()
            

        def previous_music():
            play_pause_button["text"]= "⏸"
            previous_music = self.library.get_previous_music(self.library.get_current_music())
            self.library.set_current_music(previous_music)
            self.library.play_music(previous_music)
            music_title["text"] = previous_music.get_title()
            
        
        def back_to_start():
            self.library.play_music(self.library.get_current_music())
        
        def play_pause_music():
            if(play_pause_button["text"]== "⏸"):
                mixer.music.pause()
                play_pause_button["text"] = "▶️"
            else:
                mixer.music.unpause()
                play_pause_button["text"]= "⏸"

        def retrieve_player():
            player_zone.grid()   
            prev_button.pack(in_=buttons, side=LEFT)
            pause_button.pack(in_=buttons,side=LEFT)
            next_button.pack(in_=buttons, side=LEFT)
            play_button["text"] = "🔁"
            play_button.pack(padx=8, pady=15,in_=buttons, side=LEFT)  
               
    def clear(self):
        self.destroy()