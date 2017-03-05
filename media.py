import webbrowser

class Movie():
    """Class that encapsulates the details about a single movie"""

    # Class constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title 
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # Method to display movie trailer
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
            

    
