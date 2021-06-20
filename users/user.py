# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.uploaded_at = data['uploaded_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('flask_schema').query_db(query)
        users = []
        for user in results: 
            users.append(cls(user))
        return users



    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE users.id = %(id)s'
        results = connectToMySQL('flask_schema').query_db(query,data)
        print(results)
        return cls(results[0])    

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, uploaded_at ) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() )";
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('flask_schema').query_db( query, data )

    @classmethod
    def updateuser(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, uploaded_at = NOW() WHERE id = %(id)s"
        results = connectToMySQL('flask_schema').query_db(query,data)
        return results


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL('flask_schema').query_db(query,data)
        return results