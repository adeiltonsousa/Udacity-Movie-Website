"""
Created on 11/08/2017
@author: Adeilton Sousa
"""

class Movie():
    def __init__(self, movie_title, movie_art, movie_trailer):
        self.title = movie_title
        self.poster_image_url = movie_art
        self.trailer_youtube_url = movie_trailer