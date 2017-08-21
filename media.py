import webbrowser


"""This class is provides the common information that
could be used for more media than just movies"""


class Video():
    """Class variable"""
    VALIDRATINGS = ["G", "PG", "PG-13", "R"]

    """Here we define the instance variables of the Parent class Video"""

    def __init__(self, title, storyLine,
                 poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyLine = storyLine
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def showMovieTrailer(self):
        webbrowser.open(self.trailer_youtube_url)


"""This class provides a way to store movie related information"""


class Movie(Video):
    """Below is the definition of the Child class Movie"""

    def __init__(self, title, storyLine,
                 poster_image_url, trailer_youtube_url):
        """Here we call the Parent class Video to utilize in Movie"""
        Video.__init__(self, title, storyLine,
                       poster_image_url, trailer_youtube_url)
