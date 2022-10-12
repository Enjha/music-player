import unittest

from app.models.playlist import Playlist

playlist = Playlist()

class MyTestCase(unittest.TestCase):
    def test_init(self):
        assert True == True


if __name__ == '__main__':
    unittest.main()