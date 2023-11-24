from unittest.mock import Mock
from lib.music_library import *

def test_music_library_returns_keyword_tracks():
    library = MusicLibrary()

    fake_matching = Mock()
    fake_not_matching = Mock()

    fake_matching.return_value = True
    fake_not_matching.return_value = False

    library.add(fake_matching)
    library.add(fake_not_matching)

    assert library.search("Slow") == [fake_matching]
