# General Overview

### User Interface: 
The main.py file contains the main program logic and provides a command-line interface for interacting with the movie database.

### Database Interaction: 
The objecttier.py file defines classes and functions for creating and interacting with movie-related objects (e.g., Movie, MovieRating, MovieDetails) and handling database operations such as retrieving movies, adding reviews, setting taglines, etc.

### Database Access Layer: 
The datatier.py file contains functions for executing SQL queries against the database. It abstracts away the details of database connectivity and cursor management, providing a convenient interface for interacting with the database.

### Functionality:
Users can perform various actions such as searching for movies (comm1), retrieving movie details (comm2), getting top-rated movies (comm3), adding reviews (comm4), and setting taglines (comm5).
The program displays general statistics about the movie database at the beginning (print_stats).
Users can enter commands (1-5) to execute different functionalities, and they can exit the program by entering 'x'.

# Commands
### Command 1 (comm1): Search for Movies
  Allows users to search for movies based on the title using wildcard characters (_ and %).
  Users enter a movie name, and the program retrieves movies whose titles match the provided pattern.
  If there are too many matching movies, the program informs the user to narrow down the search.

### Command 2 (comm2): Get Movie Details
  Enables users to retrieve detailed information about a specific movie based on its ID.
  Users input the movie ID, and the program fetches and displays various details about the movie, including release date, runtime, language, budget, revenue, average rating, tagline, genres, and production companies.

### Command 3 (comm3): Get Top-N Rated Movies
  Provides users with a list of the top N-rated movies, where each movie has at least a specified number of reviews.
  Users input the value of N and the minimum number of reviews.
  The program fetches and displays the top-rated movies along with their average ratings and the number of reviews.

### Command 4 (comm4): Add Review for a Movie
  Allows users to add a review (rating) for a specific movie.
  Users input the rating (0 to 10) and the movie ID.
  The program verifies the input and inserts the review into the database, notifying the user of the success or failure of the operation.

### Command 5 (comm5): Set Tagline for a Movie
  Permits users to set or update a tagline for a specific movie.
  Users input the tagline and the movie ID.
  The program sets the tagline for the movie in the database, informing the user of the success or failure of the operation.

### General Statistics Display (print_stats):
  Provides users with general statistics about the movie database, including the total number of movies and reviews stored in the database.
