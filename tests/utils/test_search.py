import pytest

from spotdl.types.saved import SavedError
from spotdl.utils.search import (
    parse_query,
    get_search_results,
    create_empty_song,
    get_simple_songs,
)


SONG = ["https://open.spotify.com/track/2Ikdgh3J5vCRmnCL3Xcrtv"]
PLAYLIST = ["https://open.spotify.com/playlist/78Lg6HmUqlTnmipvNxc536"]
ALBUM = ["https://open.spotify.com/album/4MQnUDGXmHOvnsWCpzeqWT"]
YT = [
    "https://www.youtube.com/watch?v=BZKwsPIhVO8|https://open.spotify.com/track/4B2kkxg3wKSTZw5JPaUtzQ"
]
ARTIST = ["https://open.spotify.com/artist/1FPC2zwfMHhrP3frOfaai6"]

QUERY = SONG + PLAYLIST + ALBUM + YT + ARTIST

SAVED = ["saved"]


@pytest.mark.vcr()
def test_parse_song():
    songs = parse_query(SONG)

    song = songs[0]
    assert len(songs) == 1
    assert song.download_url == None


@pytest.mark.vcr()
def test_parse_playlist():
    songs = parse_query(PLAYLIST)

    assert len(songs) > 1
    assert songs[1].url == "https://open.spotify.com/track/3pMVdkRKbHDV4zmvqWNlND"


@pytest.mark.vcr()
def test_parse_album():
    songs = parse_query(ALBUM)

    assert len(songs) == 16
    assert songs[0].url == "https://open.spotify.com/track/2Ikdgh3J5vCRmnCL3Xcrtv"


@pytest.mark.vcr()
def test_parse_yt_link():
    songs = parse_query(YT)

    assert len(songs) == 1
    assert songs[0].url == "https://open.spotify.com/track/4B2kkxg3wKSTZw5JPaUtzQ"
    assert songs[0].download_url == "https://www.youtube.com/watch?v=BZKwsPIhVO8"


@pytest.mark.vcr()
def test_parse_artist():
    songs = parse_query(ARTIST)

    assert len(songs) > 1


@pytest.mark.vcr()
def test_parse_saved():
    with pytest.raises(SavedError):
        parse_query(SAVED)


@pytest.mark.vcr()
def test_parse_query():
    songs = parse_query(QUERY)

    assert len(songs) > 1


@pytest.mark.vcr()
def test_get_search_results():
    results = get_search_results("test")
    assert len(results) > 1


def test_create_empty_song():
    song = create_empty_song("test")
    assert song.name == "test"
    assert song.url == None
    assert song.download_url == None
    assert song.duration == None
    assert song.artists == None


@pytest.mark.vcr()
def test_get_simple_songs():
    songs = get_simple_songs(QUERY)
    assert len(songs) > 1
