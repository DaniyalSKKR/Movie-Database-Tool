# File: objecttier.py
#
# objecttier
#
# Builds Movie-related objects from data retrieved through
# the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#   Project #02
#
import datatier


##################################################################
#
# Movie:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:

  def __init__(self, movieID, title, releaseYear):
    self._Movie_ID = movieID
    self._Title = title
    self._Release_Year = releaseYear

  @property
  def Movie_ID(self):
    return self._Movie_ID

  @property
  def Title(self):
    return self._Title

  @property
  def Release_Year(self):
    return self._Release_Year


##################################################################
#
# MovieRating:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:

  def __init__(self, movieID, title, releaseYear, numReviews, avgRating):
    self._Movie_ID = movieID
    self._Title = title
    self._Release_Year = releaseYear
    self._Num_Reviews = numReviews
    self._Avg_Rating = avgRating

  @property
  def Movie_ID(self):
    return self._Movie_ID

  @property
  def Title(self):
    return self._Title

  @property
  def Release_Year(self):
    return self._Release_Year

  @property
  def Num_Reviews(self):
    return self._Num_Reviews

  @property
  def Avg_Rating(self):
    return self._Avg_Rating


##################################################################
#
# MovieDetails:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string, date only (no time)
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#   Genres: list of string
#   Production_Companies: list of string
#
class MovieDetails:

  def __init__(self, movieID, title, releaseDate, runTime, origLanguage,
               budget, rev, numReviews, avgRating, tagLine, genres,
               prodCompanies):
    self._Movie_ID = movieID
    self._Title = title
    self._Release_Date = releaseDate
    self._Run_Time = runTime
    self._Original_Language = origLanguage
    self._Budget = budget
    self._Revenue = rev
    self._Num_Reviews = numReviews
    self._Avg_Rating = avgRating
    self._Tagline = tagLine
    self._Genres = genres
    self._Production_Companies = prodCompanies

  @property
  def Movie_ID(self):
    return self._Movie_ID

  @property
  def Title(self):
    return self._Title

  @property
  def Release_Date(self):
    return self._Release_Date

  @property
  def Runtime(self):
    return self._Run_Time

  @property
  def Original_Language(self):
    return self._Original_Language

  @property
  def Budget(self):
    return self._Budget

  @property
  def Revenue(self):
    return self._Revenue

  @property
  def Num_Reviews(self):
    return self._Num_Reviews

  @property
  def Avg_Rating(self):
    return self._Avg_Rating

  @property
  def Tagline(self):
    return self._Tagline

  @property
  def Genres(self):
    return self._Genres

  @property
  def Production_Companies(self):
    return self._Production_Companies


##################################################################
#
# num_movies:
#
# Returns: # of movies in the database; if an error returns -1
#
def num_movies(dbConn):
  try:
    sql = "Select Distinct count(Movie_ID) from Movies;"
    row = datatier.select_one_row(dbConn, sql)
    return row[0]
  except Exception as err:
    print("return num_movies failed:", err)
    return None


##################################################################
#
# num_reviews:
#
# Returns: # of reviews in the database; if an error returns -1
#
def num_reviews(dbConn):
  try:
    sql = "Select count(Rating) from Ratings;"
    row = datatier.select_one_row(dbConn, sql)
    return row[0]
  except Exception as err:
    print("return num_reviews failed:", err)
    return None


##################################################################
#
# get_movies:
#
# gets and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of movies in ascending order by name;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_movies(dbConn, pattern):
  try:
    #(self, movieID, title, releaseYear):
    sql = "Select Movie_ID, Title, strftime('%Y', date(Movies.Release_Date)) from Movies where Title like ? group by Movie_ID order by Movie_ID asc;"
    rows = datatier.select_n_rows(dbConn, sql, [pattern])
    #print(len(rows))
    data = []
    for row in rows:
      aMovie = Movie(row[0], row[1], row[2])
      data.append(aMovie)
    return data
  except Exception as err:
    print("return get_movies failed:", err)
    return None


##################################################################
#
# get_movie_details:
#
# gets and returns details about the given movie; you pass
# the movie id, function returns a MovieDetails object. Returns
# None if no movie was found with this id.
#
# Returns: if the search was successful, a MovieDetails obj
#          is returned. If the search did not find a matching
#          movie, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_movie_details(dbConn, movie_id):
  # def __init__(self, movieID, title, releaseDate, runTime, origLanguage,
  #budget, rev, numReviews, avgRating, tagLine, genres,
  #prodCompanies):
  try:
    #get almost all info from instructor 
    sql = "Select Distinct Movies.Movie_ID, Movies.Title, date(Movies.Release_Date), Movies.Runtime, Movies.Original_Language, Movies.Budget, Movies.Revenue, avg(Ratings.Rating), Movie_Taglines.Tagline, group_concat(Genres.Genre_Name, ' ') from Movies left Join Ratings on Movies.Movie_ID = Ratings.Movie_ID left Join Movie_Taglines on Movies.Movie_ID = Movie_Taglines.Movie_ID left Join Movie_Genres On Movies.Movie_ID = Movie_Genres.Movie_ID left join Genres on Movie_Genres.Genre_ID = Genres.Genre_ID where Movies.Movie_ID = ? group by Movies.Movie_ID;"
    
    sql2 = "Select count(Ratings.Movie_ID) from Ratings where Movie_ID = ?" # number of ratings for movie 
    sql3 = "Select group_concat(Companies.Company_Name, ', ') from Companies join Movie_Production_Companies on Companies.Company_ID = Movie_Production_Companies.Company_ID where Movie_Production_Companies.Movie_ID = ? order by Company_Name desc;"
    sql4 = "Select group_concat(Genres.Genre_Name, ', ') from Genres join Movie_Genres On Genres.Genre_ID = Movie_Genres.Genre_ID where Movie_Genres.Movie_ID = ?"
    rows = datatier.select_n_rows(dbConn, sql, [movie_id])
    row2 = datatier.select_one_row(dbConn, sql2, [movie_id])
    row3 = datatier.select_one_row(dbConn, sql3, [movie_id])
    row4 = datatier.select_one_row(dbConn, sql4, [movie_id])

    genres = []
    taglines = ""
    companies = []
    avgRating = 0
    if(row3[0] != None):
        companies = row3[0].split(', ')
        companies.sort()
          
    for row in rows:
    
      if(row[7] != None):
        avgRating = row[7] 
      
      if(row[9] != None):
        genres = row4[0].split(', ')
        genres.sort()
        # genres = row[9].split()
        # genres = [*set(genres)]
        # genres.sort()
      
        
      
      if(row[8] != None):
        taglines = row[8]
      theMovie = MovieDetails(row[0], row[1], (row[2]), row[3], row[4], row[5],
                              row[6], row2[0], avgRating, taglines, genres, companies)
      return theMovie

  except Exception as err:
    print("return get_movie_details failed:", err)
    return None


##################################################################
#
# get_top_N_movies:
#
# gets and returns the top N movies based on their average
# rating, where each movie has at least the specified # of
# reviews. Example: pass (10, 100) to get the top 10 movies
# with at least 100 reviews.
#
# Returns: returns a list of 0 or more MovieRating objects;
#          the list could be empty if the min # of reviews
#          is too high. An empty list is also returned if
#          an internal error occurs (in which case an error
#          msg is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
  #self, movieID, title, releaseYear, numReviews, avgRating
  try:
    sql = "Select Movies.Movie_ID, Movies.Title, strftime('%Y', date(Movies.Release_Date)), count(Ratings.Rating), avg(Ratings.Rating) from Movies left join Ratings on Movies.Movie_ID = Ratings.Movie_ID GROUP BY Ratings.Movie_ID HAVING COUNT(Ratings.Movie_ID) >= ? Order by avg(Ratings.Rating) desc limit ?"
    rows = datatier.select_n_rows(dbConn, sql, [min_num_reviews, N])
    #rows = datatier.select_n_rows(dbConn, sql, [9, 5])
    data = []
    for row in rows:
      aMovie = MovieRating(row[0], row[1], row[2], row[3], row[4])
      data.append(aMovie)
    return data
    
  except Exception as err:
    print("return get_top_N_movies failed:", err)
    return []


##################################################################
#
# add_review:
#
# Inserts the given review --- a rating value 0..10 --- into
# the database for the given movie. It is considered an error
# if the movie does not exist (see below), and the review is
# not inserted.
#
# Returns: 1 if the review was successfully added, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
  try:
    sqlX = "Select count(Movie_ID) from Movies where Movie_ID = ?"
    temp = datatier.select_one_row(dbConn, sqlX, [movie_id])
    if(temp[0] == 0):
      return 0
    sql = """Insert Into Ratings(Movie_ID, Rating)
    Values(?, ?);"""
    datatier.perform_action(dbConn, sql, [movie_id, rating])
    return 1
  except Exception as err:
    print("return add_review failed:", err)
    return 0
  


##################################################################
#
# set_tagline:
#
# Sets the tagline --- summary --- for the given movie. If
# the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively
# deletes the existing tagline. It is considered an error
# if the movie does not exist (see below), and the tagline
# is not set.
#
# Returns: 1 if the tagline was successfully set, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
  try:
    sqlX = "Select count(Movie_ID) from Movies where Movie_ID = ?"
    temp = datatier.select_one_row(dbConn, sqlX, [movie_id])
    if(temp[0] == 0):
      return 0
    sql = """Update Movie_Taglines Set Tagline = ?
    Where Movie_ID = ?;"""
    x = datatier.perform_action(dbConn, sql, [tagline, movie_id])

    if(x == 0):
      sql = """Insert Into Movie_Taglines(Movie_ID, tagline)
    Values(?, ?);"""
      datatier.perform_action(dbConn, sql, [movie_id, tagline])
    return 1
  except Exception as err:
    print("return add_review failed:", err)
    return 0

