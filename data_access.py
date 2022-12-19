from connection import MyConnection

class DataAccess:
    @classmethod
    def get_all_movies(cls):
        MyConnection.connection_cursor()
        return MyConnection.execution_query('select f.title from Film as f')
            
    @classmethod
    def get_all_actors(cls):
        MyConnection.connection_cursor()
        return MyConnection.execution_query('select a.first_name, a.last_name from Actor as a')
        