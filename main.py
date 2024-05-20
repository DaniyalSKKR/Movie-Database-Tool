import objecttier  #import
import sqlite3

dbConn = sqlite3.connect('MovieLens.db')


def comm5(dbConn):
  print()
  tag = input("tagline? ")
  movie = input("movie id? ")
  print()
  check = objecttier.set_tagline(dbConn, movie, tag)
  if (check == 1):
    print("Tagline successfully set")
  else:
    print("No such movie...")


def comm4(dbConn):
  print()
  inp = input("Enter rating (0..10): ")
  if (int(inp) < 0 or int(inp) > 10):
    print("Invalid rating...")
    return

  id = input("Enter movie id: ")
  check = objecttier.add_review(dbConn, id, int(inp))
  print()
  if (check == 1):
    print("Review successfully inserted")
  else:
    print("No such movie...")


def comm3(dbConn):  #Gets top_N_movies
  strN = input("N? ")
  if (int(strN) < 1):  #edge case
    print("Please enter a positive value for N...")
    return

  strR = input("min number of reviews? ")
  if (int(strR) < 1):  #edge case
    print("Please enter a positive value for min number of reviews...")
    return
    
  data = objecttier.get_top_N_movies(dbConn, int(strN), int(strR))
  print()

  if (len(data) == 0):  #check for empty
    return

  for d in data:  #loop prints all data for movies in data
    print(d.Movie_ID, ":", d.Title, f'({d.Release_Year}),', "avg rating =",
          f'{d.Avg_Rating:.2f}', f'({d.Num_Reviews} reviews)')


def comm2(dbConn):  #get movie details from given movie_id
  
  str = input("Enter movie id: ")
  print()
  data = objecttier.get_movie_details(dbConn, str)
  if (data == None):  #check for empty
    print("No such movie...")
    return

  genre = data.Genres
  prod = data.Production_Companies

  # if(genre == []):
  #   genre = ""

  # if(prod == []):
  #   prod = ""


  budget = '{:,}'.format(data.Budget)
  rev = '{:,}'.format(data.Revenue)
  #Print all aspects of a movie (details)
  print(data.Movie_ID, ":", data.Title)
  print("  Release date:", data.Release_Date)
  print("  Runtime:", data.Runtime, "(mins)")
  print("  Orig language:", data.Original_Language)
  print("  Budget:", f'${budget}', "(USD)")
  print("  Revenue:", f'${rev}', "(USD)")
  print("  Num reviews:", data.Num_Reviews)
  print("  Avg rating:", f'{data.Avg_Rating:.2f}', "(0..10)")
  print("  Genres:", end = ' ')
  for g in genre:
    print(g, end = ', ')
  print()
  print("  Production companies:", end = ' ')
  for p in prod:
    print(p, end = ', ')
  print()
  print("  Tagline:", data.Tagline)


def comm1(dbConn):  #Get list of movies based upon title
  print()
  str = input("Enter movie name (wildcards _ and % supported): ")
  print()
  data = objecttier.get_movies(dbConn, str)
  print("# of movies found:", len(data))
  print()
  if (len(data) <= 100):
    for d in data:
      print(d.Movie_ID, ":", d.Title, f'({d.Release_Year})')
  else:
    print(
      "There are too many movies to display, please narrow your search and try again..."
    )  #edge case


def print_stats(dbConn):  #Simple initial data is printed
  dbCursor = dbConn.cursor()

  print("General stats:")
  numM = objecttier.num_movies(dbConn)
  numR = objecttier.num_reviews(dbConn)
  print("  # of movies:", '{:,}'.format(numM))
  print("  # of reviews:", '{:,}'.format(numR))

  dbCursor.close()


# main
#
print('** Welcome to the MovieLens app **')

print()
print_stats(dbConn)
print()
cmd = input(
  "Please enter a command (1-5, x to exit): ")  #Run through options for user
while cmd != "x":
  print()
  if cmd == "1":
    comm1(dbConn)
  elif cmd == "2":
    comm2(dbConn)
  elif cmd == "3":
    comm3(dbConn)
  elif cmd == "4":
    comm4(dbConn)
  elif cmd == "5":
    comm5(dbConn)
  else:
    print("**Error, unknown command, try again...")  #error checking

  print()
  cmd = input("Please enter a command (1-5, x to exit): ")

dbConn.close()
