import pdb
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Fleetwood Mac")
artist_repository.save(artist_1)

album_1 = Album('Rumours', 'Rock', artist_1)
album_repository.save(album_1)

album_2 = Album('Tango in the Night', 'Rock', artist_1)
album_repository.save(album_2)

all_artists = artist_repository.select_all()
all_albums = album_repository.select_all_by_artist(artist_1)
pdb.set_trace()