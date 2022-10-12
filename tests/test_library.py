import unittest
from tkinter import *

from app.models.library import Library

library = Library()
music_list = library.get_music_list()

window = Tk()

music_space = Listbox(window, fg="black", bg="grey", width=100, font=('helvetica', 18))
music_space.pack(padx=18, pady=18)
for music in music_list:
    music_space.insert('end', music.get_title())


class MyTestCase(unittest.TestCase):

    def test_init_music_list(self):
        assert  len(music_list) == 3
        assert  music_list[0].get_title() == "Avicii - The Nights"
        assert  music_list[2].get_title() == "Demon Slayer - Kimetsu no Yaiba"

    def test_is_music_exist(self):
        assert library.is_music_exist("Avicii - The Nights")
        assert not library.is_music_exist("Bvicii - The Nights")

    def test_delete_music(self):
        assert library.is_music_exist("Avicii - The Nights")
        assert  len(music_list) == 3
        music_space.select_anchor(0)
        library.delete_music(music_space)
        assert not library.is_music_exist("Avicii - The Nights")
        assert  len(music_list) == 2
