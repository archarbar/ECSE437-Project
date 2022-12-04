import unittest

from Movie import *
from Serie import *
from Song import *
from Library import *

class TestStringMethods(unittest.TestCase):
  def test_new_movie(self):
    movie = Movie('No Country For Old Men', 'Ethan Coen', 2007)
    self.assertEqual(movie.title, 'No Country For Old Men')
    self.assertEqual(movie.director, 'Ethan Coen')
    self.assertEqual(movie.year, 2007)

  def test_update_movie(self):
    movie = Movie('The Gentlemen', 'Guy Ritchie', 2020)
    movie.update('No Country For Old Men', 'Ethan Coen', 2007)
    self.assertEqual(movie.title, 'No Country For Old Men')
    self.assertEqual(movie.director, 'Ethan Coen')
    self.assertEqual(movie.year, 2007)

  def test_new_series(self):
    serie = Serie('Breaking Bad', 'Vince Gilligan', 2008)
    self.assertEqual(serie.title, 'Breaking Bad')
    self.assertEqual(serie.creator, 'Vince Gilligan')
    self.assertEqual(serie.year, 2008)

  def test_update_serie(self):
    serie = Serie('Peaky Blinders', 'Steven Knight', 2013)
    serie.update('Breaking Bad', 'Vince Gilligan', 2008)
    self.assertEqual(serie.title, 'Breaking Bad')
    self.assertEqual(serie.creator, 'Vince Gilligan')
    self.assertEqual(serie.year, 2008)
  
  def test_new_song(self):
    song = Song('Lose Yourself', 'Eminem', 2002)
    self.assertEqual(song.title, 'Lose Yourself')
    self.assertEqual(song.artist, 'Eminem')
    self.assertEqual(song.year, 2002)
  
  def test_update_song(self):
    song = Song('Money Trees', 'Kendrick Lamar', 2012)
    song.update('Lose Yourself', 'Eminem', 2002)
    self.assertEqual(song.title, 'Lose Yourself')
    self.assertEqual(song.artist, 'Eminem')
    self.assertEqual(song.year, 2002)

if __name__ == '__main__':
  unittest.main()