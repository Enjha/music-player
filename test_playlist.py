import unittest
import os 
from mutagen.mp3 import MP3

from app.models.library import Library
from app.models.music import Music
from app.models.playlist import Playlist

name_playlist = "playlist_test"

library = Library()

playlist = Playlist(name_playlist)



class MyTestCase(unittest.TestCase):
    def test_a_init(self):
        playlist.create()
        assert os.path.isfile("ressources\playlists\playlist_test.txt") == True
        assert len(playlist.music_list) == 0

    def test_b_add_music(self):
        audio = MP3("ressources\songs\Demon Slayer - Kimetsu no Yaiba.mp3")
        audio_info = audio.info
        duration = int(audio_info.length)
        music = Music("Demon Slayer - Kimetsu no Yaiba", duration, library)
        playlist.add_music(music)
        playlist_file = open('ressources\playlists\playlist_test.txt', 'r')
        count = 0
        lines = playlist_file.readlines()
        for line in lines:
            count += 1
        assert count == 1
        assert lines[0] == 'Demon Slayer - Kimetsu no Yaiba\n'
        playlist_file.close()

    def test_c_remove_music(self):
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

    def test_z_delete(self):
        playlist.delete()
        assert os.path.isfile("ressources\playlists\playlist_test.txt") == False

        


if __name__ == '__main__':
    unittest.main()