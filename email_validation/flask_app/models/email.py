from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

#connecting the form to the database
class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO email_log (email, created_at, updated_at); VALUES ( %(email)s, NOW(), NOW());"
        return connectToMySQL('emails_schema').query_db(query, data)

    # @classmethod
    # def get_last_survey(cls):
    #     query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
    #     results = connectToMySQL('survey_schema').query_db(query)
    #     return Survey(results[0])

    # #basic validation for our form
    # @staticmethod
    # def is_valid(survey):
    #     is_valid = True # we assume this is true
    #     if len(survey['name']) < 3:
    #         is_valid = False
    #         flash("Name must be at least 3 characters.")
    #     if len(survey['location']) < 1:
    #         is_valid = False
    #         flash("Must choose a dojo location.")
    #     if len(survey['language']) < 1:
    #         is_valid = False
    #         flash("Must choose a programming language.")
    #     if len(survey['comment']) < 3:
    #         is_valid = False
    #         flash("Comment must be at least 3 characters.")
    #     return is_valid