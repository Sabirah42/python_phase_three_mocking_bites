from lib.music_library import *
from lib.track import *

def test_music_library_adds_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("Slow Show", "The National")
    track_2 = Track("In The End", "The National")
    library.add(track_1)
    library.add(track_2)

    assert library.tracks == [track_1, track_2]

# def test_music_library_returns_matching_tracks():
#     library = MusicLibrary()
#     track_1 = Track("Slow Show", "The National")
#     track_2 = Track("Green Gloves", "The National")
#     library.add(track_1)
#     library.add(track_2)

#     assert library.search("Show") == [track_1]