class Library:
  def __init__(movies=[], series=[], songs=[]):
    self.movies = movies
    self.series = series
    self.songs = songs

  def addMovie(movie):
    self.movies.append(movie)

  def addSerie(serie):
    self.series.append(serie)

  def addSong(song):
    self.songs.append(song)
  
  def removeMovie(title):
    for movie in movies:
      if movie.title == title:
        self.movies.remove(movie)

  def removeSerie(title):
    for serie in series:
      if serie.title == title:
        self.series.remove(serie)

  def removeSong(title):
    for song in songs:
      if song.title == title:
        self.songs.remove(song)

  def getMovies():
    return self.movies

  def getSeries():
    return self.series

  def getSongs():
    return self.songs

  def doesMovieExist(title):
    for movie in movies:
      if movie.title == title:
        return True
    return False

  def doesSerieExist(title):
    for serie in series:
      if serie.title == title:
        return True
    return False

  def doesSongExist(title):
    for song in songs:
      if song.title == title:
        return True
    return False