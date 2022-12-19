from connection import MyConnection
from data_access import DataAccess
from test import Test

MyConnection.connection_cursor()

DataAccess.get_all_movies()
DataAccess.get_all_actors()

Test().print_movies()
Test().print_actors()

print(MyConnection.close_connection())