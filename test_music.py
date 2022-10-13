import unittest
from mutagen.mp3 import MP3

from app.models.library import Library
from app.models.music import Music


class MyTestCase(unittest.TestCase):
    def test_music(self):
        audio = MP3("Demon Slayer - Kimetsu no Yaiba.mp3")
        library = Library()
        audio_info = audio.info
        duration = int(audio_info.length)
        music = Music("Demon Slayer - Kimetsu no Yaiba.mp3".replace(".mp3", "").replace("tests/ressources/songs/", ""), duration, library)
        assert music.get_title() == "Demon Slayer - Kimetsu no Yaiba"

        assert music.get_duration() == duration


if __name__ == '__main__':
    unittest.main()