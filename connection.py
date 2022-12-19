import mysql.connector

class MyConnection:
    
    @classmethod
    def connection_cursor(cls):
        cls.connection = None
        cls.cursor = None 
        
        try:
            cls.connection = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "Matrix1999@",port="3306",database="sakila" )
            cls.cursor= cls.connection.cursor()
        except mysql.connector.Error as error:
            print("Si è verificato un errore") 
            print(error)
    
    @classmethod
    def execution_query(cls, query):
        cls.cursor.execute(query)  
        result= cls.cursor.fetchall()
        return result   
    
    @classmethod 
    def close_connection(cls):
        if cls.connection is not None:
            cls.connection.close()
        print('Connesione chiusa!!')
            
        