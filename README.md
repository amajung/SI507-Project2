SI 507 Project 2 by Amanda Jung

In this project, the goal was to create a simple banking app using code from the files movies_clean.csv, SI507_project2, movies_tools.py, and requirements.txt.

The file movies_clean.csv contains 3146 lines where each line contains information (separated by commas) about a movie such as it's Title, US Gross, Worldwide Gross, US DVD Sales, Production Budget, Release Date, MPAA Rating, Running Time (min), Distributor, Source, Major Genre, Creative Type, Director, Rotten Tomatoes Rating, IMDB Rating, and IMDB Votes.

In movies_tools.py, we see that

In SI507_project2.py, there is one class called Movie.
  - It contains a constructor that takes in a string as an argument and creates the instance variables "title" and "IMDBrating" from the information provided for each movie.
  - It also contains a str method, which prints out the movie title and IMDB rating.

In SI507_project2.py, we incorporate Flask and have different routes with specific set of inputs based on the url. Underneath each route is a function definition that incorporates information from movies_clean.csv and the Movie class from movies_tools.py and produces the desired output.

The file requirements.txt contains the packages (e.g. Flask) that are necessary to run the files of code listed above.
