# MOSTLY CREATED BY FOLLOWING ALONG IN THE UDACITY LESSONS

# Four things I want:
# title
# storyline
#poster_image
#trailer_youtube
import webbrowser

class Movie():
    """A class for storing information about a movie"""

    def __init__(self,
                movie_title,
                movie_storyline,
                poster_image,
                trailer_youtube):
        # These values will get created when we make an
        # instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # shows the movie's trailer
        webbrowser.open(self.trailer_youtube_url)
