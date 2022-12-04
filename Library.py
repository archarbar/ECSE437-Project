from Movie import *
from Serie import *
from Song import *

class Library:
  def __init__(self, movies=[], series=[], songs=[]):
    self.movies = movies
    self.series = series
    self.songs = songs

  def addMovie(self, movie):
    self.movies.append(movie)

  def addSerie(self, serie):
    self.series.append(serie)

  def addSong(self, song):
    self.songs.append(song)
  
  def removeMovie(self, title):
    for movie in self.movies:
      if movie.title == title:
        self.movies.remove(movie)

  def removeSerie(self, title):
    for serie in self.series:
      if serie.title == title:
        self.series.remove(serie)

  def removeSong(self, title):
    for song in self.songs:
      if song.title == title:
        self.songs.remove(song)

  def getMovies(self):
    return self.movies

  def getSeries(self):
    return self.series

  def getSongs(self):
    return self.songs

  def doesMovieExist(self, title):
    for movie in self.movies:
      if movie.title == title:
        return True
    return False

  def doesSerieExist(self, title):
    for serie in self.series:
      if serie.title == title:
        return True
    return False

  def doesSongExist(self, title):
    for song in self.songs:
      if song.title == title:
        return True
    return False
