import unittest

from Library import *

class TestStringMethods(unittest.TestCase):
  def setUp(self):
    self.library = Library([],[],[])

  def test_new_library(self):
    self.assertEqual(len(self.library.series), 0)
    self.assertEqual(len(self.library.series), 0)
    self.assertEqual(len(self.library.songs), 0)

  def test_add_remove(self):
    movie = Movie('No Country For Old Men', 'Ethan Coen', 2007)
    self.library.addMovie(movie)
    serie = Serie('Breaking Bad', 'Vince Gilligan', 2008)
    self.library.addSerie(serie)
    song = Song('Lose Yourself', 'Eminem', 2002)
    self.library.addSong(song)
    self.library.removeSong('Lose Yourself')
    movie2 = Movie('The Departed', 'Martin Scorsese', 2006)
    self.library.addMovie(movie2)
    self.assertEqual(self.library.movies, [movie, movie2])
    self.assertEqual(self.library.series, [serie])
    self.assertEqual(self.library.songs, [])

  # ----------------- MOVIE --------------------

  def test_add_movie(self):
    movie = Movie('No Country For Old Men', 'Ethan Coen', 2007)
    self.library.addMovie(movie)
    self.assertEqual(self.library.movies, [movie])

  def test_remove_movie(self):
    movie = Movie('No Country For Old Men', 'Ethan Coen', 2007)
    self.library.addMovie(movie)
    self.assertEqual(len(self.library.movies), 1)
    self.library.removeMovie('No Country For Old Men')
    self.assertEqual(len(self.library.movies), 0)

  def test_get_movies(self):
    movie = Movie('No Country For Old Men', 'Ethan Coen', 2007)
    self.library.addMovie(movie)
    self.assertEqual(self.library.getMovies(), self.library.movies)

  def test_movie_exists(self):
    movie = Movie('No Country For Old Men', 'Ethan Coen', 2007)
    self.library.addMovie(movie)
    self.assertTrue(self.library.doesMovieExist('No Country For Old Men'))

  def test_movie_not_exists(self):
    self.assertFalse(self.library.doesMovieExist('No Country For Old Men'))

  # ----------------- SERIE --------------------Breaking

  def test_add_serie(self):
    serie = Serie('Breaking Bad', 'Vince Gilligan', 2008)
    self.library.addSerie(serie)
    self.assertEqual(self.library.series, [serie])

  def test_remove_serie(self):
    serie = Serie('Breaking Bad', 'Vince Gilligan', 2008)
    self.library.addSerie(serie)
    self.assertEqual(len(self.library.series), 1)
    self.library.removeSerie('Breaking Bad')
    self.assertEqual(len(self.library.series), 0)

  def test_get_series(self):
    serie = Serie('Breaking Bad', 'Vince Gilligan', 2008)
    self.library.addSerie(serie)
    self.assertEqual(self.library.getSeries(), self.library.series)

  def test_serie_exists(self):
    serie = Serie('Breaking Bad', 'Vince Gilligan', 2008)
    self.library.addSerie(serie)
    self.assertTrue(self.library.doesSerieExist('Breaking Bad'))

  def test_serie_not_exists(self):
    self.assertFalse(self.library.doesSerieExist('Breaking Bad'))
  
  # ----------------- SONG --------------------

  def test_add_song(self):
    song = Song('Lose Yourself', 'Eminem', 2002)
    self.library.addSong(song)
    self.assertEqual(self.library.songs, [song])

  def test_remove_song(self):
    song = Song('Lose Yourself', 'Eminem', 2002)
    self.library.addSong(song)
    self.assertEqual(len(self.library.songs), 1)
    self.library.removeSong('Lose Yourself')
    self.assertEqual(len(self.library.songs), 0)

  def test_get_songs(self):
    song = Song('Lose Yourself', 'Eminem', 2002)
    self.library.addSong(song)
    self.assertEqual(self.library.getSongs(), self.library.songs)

  def test_song_exists(self):
    song = Song('Lose Yourself', 'Eminem', 2002)
    self.library.addSong(song)
    self.assertTrue(self.library.doesSongExist('Lose Yourself'))

  def test_song_not_exists(self):
    self.assertFalse(self.library.doesSongExist('Lose Yourself'))

if __name__ == '__main__':
  unittest.main()
  