import unittest
from tkinter import *

from app.models.music import Music
from pygame import mixer



window = Tk()

music_path = "ressources\\songs"
music_space = Listbox(window, fg="black", bg="grey", width=100, font=('helvetica', 18))
music_space.pack(padx=18, pady=18)

space = Label(window, text="Boutons space", bg='#5DC863', fg='black', font=('poppin', 22))
space.pack(pady=150)

class MyTestCase(unittest.TestCase):
    def test_prev_music(self):
        music = Music()
        music.play_music(music_path, music_space, space)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()