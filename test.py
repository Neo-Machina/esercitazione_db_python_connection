from data_access import DataAccess

class Test:
    @classmethod
    def print_movies(cls):
        movies = print(f'TUTTI I FILM: {DataAccess.get_all_movies()}')
        return movies
        
        
    @classmethod
    def print_actors(cls):
       actors = print(f'TUTTI GLI ATTORI: {DataAccess.get_all_actors()}')
       return actors
        