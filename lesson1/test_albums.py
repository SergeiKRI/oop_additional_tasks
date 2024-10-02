import pytest

from lesson1.albums import Album


@pytest.fixture
album_1 = Album( 'Queen', 'Killer Queen', ['Brighton rock', 'Killer Queen', 'Tenement Funster'])
album_2 = Album( 'Metallica', 'Black Album', ['Enter Sandman', 'Sad But True', 'Holier Than Thou'])

