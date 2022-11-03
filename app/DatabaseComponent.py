# Database Component
# from Shake import *
# from User import *
# from ingredients.Ingredient import *
from flask_login import UserMixin

from app import db

class User(db.Model, UserMixin): ## creates the database table which stores the user login info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(80))

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email}, password={self.password})'


class ingredients_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f'Ingredient(id={self.id}, name={self.name})'


class recipe_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    calories = db.Column(db.String(100))
    fat = db.Column(db.String(100))
    sugar = db.Column(db.String(100))

    def __repr__(self):
        return f'Recipe(id={self.id}, name={self.name}, calories={self.calories}, fat={self.fat}, sugar={self.sugar})'


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
