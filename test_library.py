import unittest
from tkinter import *
import shutil


from app.models.library import Library
from app.models.music import Music

LIBRARY_PATH = "ressources/songs"


library = Library()
music_list = library.get_music_list()

window = Tk()

music_space = Listbox(window, fg="black", bg="grey", width=100, font=('helvetica', 18))
music_space.pack(padx=18, pady=18)
for music in music_list:
    music_space.insert('end', music.get_title())


class MyTestCase(unittest.TestCase):


    def test_a_init_music_list(self):
        assert  len(music_list) == 3
        assert  music_list[0].get_title() == "Cry Baby- Tokyo Revengers"
        assert  music_list[2].get_title() == "You Want a Battle_ (Here's a War)"

    def test_b_is_music_exist(self):
        assert library.is_music_exist("Cry Baby- Tokyo Revengers")
        assert not library.is_music_exist("Dry Baby- Tokyo Revengers")

    def test_c_find_music_by_name(self):
        name = "Cry Baby- Tokyo Revengers"
        music = library.find_music_by_name(name)
        assert music.get_title() == name

    def test_d_delete_music(self):
        assert library.is_music_exist("Demon Slayer - Kimetsu no Yaiba")
        assert  len(music_list) == 3
        music_space.select_anchor(1)
        library.delete_music(music_space)
        library2 = Library()
        assert not library2.is_music_exist("Demon Slayer - Kimetsu no Yaiba")
        music_list2 = library2.get_music_list()
        assert  len(music_list2) == 2

    def test_e_create_music_by_name(self):
        library = Library()
        music_list = library.get_music_list()
        assert  len(music_list) == 2
        song = "Demon Slayer - Kimetsu no Yaiba.mp3"
        shutil.copy(song, LIBRARY_PATH)    
        song_split = song.split("/")
        song_rename = song_split[len(song_split)-1]        
        music_list.append(song_rename.replace(".mp3",""))
        library.create_music_by_name(song_rename)
        library = Library()
        assert  len(music_list) == 3
        assert library.is_music_exist("Demon Slayer - Kimetsu no Yaiba")



    
        

if __name__ == '__main__':
    unittest.main()