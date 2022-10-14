import unittest
from tkinter import *
import shutil
import os 

from mutagen.mp3 import MP3
from app.models.library import Library
from app.models.music import Music
from app.models.playlist import Playlist


LIBRARY_PATH = "ressources/songs"

library = Library()
music_list = library.get_music_list()

window = Tk()

name_playlist = "playlist_test"

playlist = Playlist(name_playlist, library)

music_space = Listbox(window, fg="black", bg="grey", width=100, font=('helvetica', 18))
music_space.pack(padx=18, pady=18)
for music in music_list:
    music_space.insert('end', music.get_title())

class MyTestCase(unittest.TestCase):
    
    #test de l'initialisation de la librairie
    def test_a_init_music_list_library(self):
        assert  len(music_list) == 7
        assert  music_list[1].get_title() == "Cry Baby- Tokyo Revengers"
        assert  music_list[6].get_title() == "You Want a Battle_ (Here's a War)"
        print(music_list[1].get_title())
    #vérification de la présence d'une musique dans la librairie
    def test_b_is_music_exist_library(self):
        assert library.is_music_exist("Cry Baby- Tokyo Revengers")
        assert not library.is_music_exist("Dry Baby- Tokyo Revengers")

    #test de recherche d'une musique dans la librairie
    def test_c_find_music_by_name_library(self):
        name = "Cry Baby- Tokyo Revengers.mp3"
        music = library.find_music_by_name(name)
        assert music.get_title() == name

    #test la suppression d'une musique dans la librairie
    def test_d_delete_music_library(self):
        assert library.is_music_exist("Demon Slayer - Kimetsu no Yaiba")
        assert  len(music_list) == 7
        music_space.select_anchor(2)
        library.delete_music(music_space)
        library2 = Library()
        assert not library2.is_music_exist("Demon Slayer - Kimetsu no Yaiba")
        music_list2 = library2.get_music_list()
        assert  len(music_list2) == 6

    #test de la creation d'une musique dans la librairie
    def test_e_create_music_by_name_library(self):
        library = Library()
        music_list = library.get_music_list()
        assert  len(music_list) == 6
        song = "ressources/song_test/Demon Slayer - Kimetsu no Yaiba.mp3"
        shutil.copy(song, LIBRARY_PATH)    
        song_split = song.split("/")
        song_rename = song_split[len(song_split)-1]        
        music_list.append(song_rename.replace(".mp3",""))
        library.create_music_by_name(song_rename)
        library = Library()
        assert  len(music_list) == 7
        assert library.is_music_exist("Demon Slayer - Kimetsu no Yaiba")

    #test de l'initialisation d'une musique
    def test_f_music(self):
        audio = MP3("ressources/song_test/Demon Slayer - Kimetsu no Yaiba.mp3")
        library = Library()
        audio_info = audio.info
        duration = int(audio_info.length)
        music = Music("ressources/song_test/Demon Slayer - Kimetsu no Yaiba.mp3".replace(".mp3", "").replace("ressources/song_test/", ""), duration, library)
        assert music.get_title() == "Demon Slayer - Kimetsu no Yaiba"
        assert music.get_duration() == duration

    #test de l'initialisation d'une playlist
    def test_g_init_playlist(self):
        playlist.create()
        assert os.path.isfile("ressources\playlists\playlist_test.txt") == True
        assert len(playlist.music_list) == 0


    #test de l'ajout d'une musique dans une playlist
    def test_h_add_music_playlist(self):
        audio = MP3("ressources\songs\Demon Slayer - Kimetsu no Yaiba.mp3")
        audio_info = audio.info
        duration = int(audio_info.length)
        music = Music("Demon Slayer - Kimetsu no Yaiba", duration, library)
        playlist.add_music(music)
        playlist.add_music(music)
        playlist_file = open('ressources\playlists\playlist_test.txt', 'r')
        count = 0
        lines = playlist_file.readlines()
        for line in lines:
            count += 1
        assert count == 2
        print(count)
        assert lines[0] == 'Demon Slayer - Kimetsu no Yaiba\n'
        assert lines[1] == 'Demon Slayer - Kimetsu no Yaiba\n'
        playlist_file.close()

    #test de l'ajout d'une playlist dans la librairie
    def test_i_add_playlist_library(self):
        cpt_playlist = len(library.get_playlist_list())
        library.add_playlist(playlist)
        cpt = 0
        assert cpt_playlist + 1 == len(library.get_playlist_list())

    #test de la suppression d'une playlist dans la librairie
    def test_j_remove_playlist_library(self):
        cpt_playlist = len(library.get_playlist_list())
        library.remove_playlist(playlist)
        assert cpt_playlist - 1 == len(library.get_playlist_list())

    #test de la suppression d'une musique dans une playlist        
    def test_x_remove_music_by_index_playlist(self):
        playlist.remove_music_by_index(0)
        playlist_file = open('ressources\playlists\playlist_test.txt', 'r')
        lines = playlist_file.readlines()
        count = 0
        for line in lines:
            count += 1
        assert count == 1
        playlist_file.close()

    #test de la suppression d'une musique dans une playlist
    def test_y_remove_music_playlist(self):
        audio = MP3("ressources\song_test\Demon Slayer - Kimetsu no Yaiba.mp3")
        audio_info = audio.info
        duration = int(audio_info.length)
        music = Music("Demon Slayer - Kimetsu no Yaiba", duration, library)
        playlist.remove_music(music)
        playlist_file = open('ressources\playlists\playlist_test.txt', 'r')
        count = 0
        lines = playlist_file.readlines()
        for line in lines:
            count += 1
        assert count == 0
        playlist_file.close()

    #test de la suppression d'une playlist
    def test_z_delete_playlist(self):
        playlist.delete()
        assert os.path.isfile("ressources\playlists\playlist_test.txt") == False

if __name__ == '__main__':
    unittest.main()