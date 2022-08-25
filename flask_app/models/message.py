from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'users_messages_db'

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages (message, user_id) VALUES (%(message)s, %(user_id)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE user_id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    # @classmethod
    # def get_sender(cls, data):
    #     query = "SELECT * FROM users JOIN messages ON messages.id = users.id WHERE messages.id = %(id)s"
    #     result = connectToMySQL(db).query_db(query, data)
    #     return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages;"
        results = connectToMySQL(db).query_db(query)
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages

    @staticmethod
    def validate_message(message):
        is_valid = True
        if len(message['message']) < 1:
            is_valid = False
            flash("Movie must be longer than 1 letters", "review")
        return is_valid