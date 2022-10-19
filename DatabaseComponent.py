# Database Component
# from Shake import *
# from User import *
# from ingredients.Ingredient import *
from flask_login import UserMixin
from __init__ import db

class users(db.Model,UserMixin): ## creates the database table which stores the user login info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(80))



# def IngredientInfo(filter: List[Ingredient]) -> List[Ingredient]:
#     """
#     This method returns each ingredient and its nutrition info
#     :param filter: filters to load only selected ingredients, has no filter if empty list
#     :return: a multivalued list of ingredients and its nutrition information
#     """
#     pass

# def getUserInfo(user: User) -> (email, password):
#     """
#     This method returns the current user's email and password
#     :param: A user object
#     :return: A tuple consisting of email and password
#     """
#     pass

# def getUserHistory(user: User) -> List[Shake]:
#     """
#     This method returns a list of the current user's recently viewed shakes
#     :param user: The current user object
#     :return: A List containing Shake objects
#     """
#     pass

# def getUserFavorites(user: User) -> List[Shake]:
#     """
#     This method returns the current user's entire favorites list
#     :param: A user object
#     :return: A List containing Shake objects
#     """
#     pass