from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import timedelta

import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjdsfsdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + \
        os.path.join(
            'test.db')  # this creates the database as a personal file in called test.db
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.recipes import recipes
    from app.index import index
    from app.ingredients import ingredients  # these imports are the blueprints
    from app.account import account
    from app.authentication import authentication
    from app.favorites import favorites

    app.register_blueprint(index.index, url_prefix="")
    app.register_blueprint(recipes.recipes, url_prefix="/recipes")
    # these registers the blueprints so they
    app.register_blueprint(ingredients.ingredients, url_prefix="/ingredients")
    # can be used in the app in differnt files
    app.register_blueprint(account.account, url_prefix="/account")
    app.register_blueprint(authentication.authentication, url_prefix="")
    app.register_blueprint(favorites.favorites, url_prefix="")

    from app import DatabaseComponent

    login_manager = LoginManager()
    # controls the login with in the authentication branch
    login_manager.login_view = 'authentication.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # loads the users id which contain the emails, names and passwords.
        return DatabaseComponent.User.query.get(int(id))

    from app.DatabaseComponent import User
    from app.DatabaseComponent import ingredients_table
    from app.DatabaseComponent import recipe_table

    with app.app_context():
        # You create the database and tables by following the instructions in the README.md
        # You populate the tables with data by writing some code here.

        inspector = inspect(db.engine)

        # First, make sure the table you are trying to populate exists.
        # Make sure the table exists before doing anything with it
        if not inspector.has_table('user'):
            print(
                "user table does not exist! did you run 'flask db upgrade' from the terminal?")
        else:
            current_users = User.query.all()
            # First, check to see if there is already data. If so, do not add your initial data.
            if current_users:
                print("The user table already exists! Printing all users...")
                for u in current_users:
                    print(f'\t{u}')
                print("I printed them!")
            else:
                print("No users detected. Adding one!")
                u = User(name="Bob", email="bob@abc.com", password="abc123")
                db.session.add(u)
                db.session.commit()
                print("The user is added. Inspect the database file or re-run the app to see it.")

        # Make sure the table exists before doing anything with it
        if not inspector.has_table('recipe_table'):
            print(
                "Recipe table does not exist! Did you run 'flask db upgrade' from the terminal?")
        else:
            current_recipe = recipe_table.query.all()
            # First, check to see if there is already data. If so, do not add your initial data.
            if current_recipe:
                print("The recipe table already exists! Printing all recipes...")
                for i in current_recipe:
                    print(f'\t{i}')
                print("I printed them!")
            else:
                print("No recipes detected. Adding them")
                recipes_list = [
                    {"id": 1, "name": "Brown shake with nuts",
                        "calories": 5000, "fat": 0, "sugar": 0, "recipetext": "The greatest shake of all time, it is infinitely powerful"},
                    {"id": 2, "name": "Banana Shake",
                        "calories": 235, "fat": 7, "sugar": 7, "recipetext": "Combine 1 banana and 1/4 cup milk in a blender and blend until smooth."},
                    {"id": 3, "name": "Strawberry Banana Shake",
                        "calories": 60, "fat": 1, "sugar": 2, "recipetext": "Pour 1/2 cup milk in a blender. Add halved strawberries. Add 1/2 of a banana. Add 1/2 tbsp sugar."},
                    {"id": 4, "name": "Cherry-Blueberry Banana Shake",
                        "calories": 120, "fat": 4, "sugar": 4, "recipetext": "In a blender combine cherries, milk, yogurt, blueberries, and banana. Cover and blend until smooth."},
                    {"id": 5, "name": "Orange Vanilla Shake",
                        "calories": 130, "fat": 7, "sugar": 6, "recipetext": "Cut the orange into halves and remove seeds. Peel and dice into large pieces. Add into blender with 1 tsp vanilla and milk and blend until smooth."},
                    {"id": 6, "name": "Triple Berry Oat Shake",
                        "calories": 145, "fat": 2, "sugar": 7, "recipetext": "Add 1/4 cup frozen blueberries, 1/4 cup frozen raspberries, 1/2 cup frozen strawberries, 1/2 cup rolled oats, 1/2 cup yogurt, and 1 banana to the blender and blend until smooth."},
                    {"id": 7, "name": "Tropical Shake",
                        "calories": 90, "fat": 1, "sugar": 1, "recipetext": "Place pineapple, yogurt, coconut, and regular milk in blender and blend until smooth."},
                    {"id": 8, "name": "Light orange shake",
                        "calories": 160, "fat": 7, "sugar": 9, "recipetext": ""},
                    {"id": 9, "name": "Light purple shake",
                        "calories": 140, "fat": 5, "sugar": 4, "recipetext": ""},
                    {"id": 10, "name": "Light red shake",
                        "calories": 145, "fat": 4, "sugar": 3, "recipetext": ""},
                    {"id": 11, "name": "Light yellow shake",
                        "calories": 180, "fat": 8, "sugar": 5, "recipetext": ""},
                    {"id": 12, "name": "White shake",
                        "calories": 220, "fat": 7, "sugar": 12, "recipetext": ""},
                    {"id": 13, "name": "Blue shake",
                        "calories": 110, "fat": 5, "sugar": 5, "recipetext": ""},    
                    {"id": 14, "name": "Green shake",
                        "calories": 50, "fat": 2, "sugar": 3, "recipetext": ""},
                    {"id": 15, "name": "Dark blue shake",
                        "calories": 140, "fat": 9, "sugar": 20, "recipetext": ""},
                    {"id": 16, "name": "Light red shake",
                        "calories": 120, "fat": 10, "sugar": 5, "recipetext": ""},    
                    {"id": 17, "name": "Orange shake",
                        "calories": 145, "fat": 7, "sugar": 8, "recipetext": ""},
                    {"id": 18, "name": "Purple shake",
                        "calories": 170, "fat": 2, "sugar": 4, "recipetext": ""},
                    {"id": 19, "name": "Yellow shake",
                        "calories": 110, "fat": 3, "sugar": 46, "recipetext": ""},    
                    {"id": 20, "name": "Green with Kiwi shake",
                        "calories": 145, "fat": 8, "sugar": 15, "recipetext": ""},
                ]
                for i in range(len(recipes_list)):
                    new_recipe = recipe_table(id=recipes_list[i].get("id"), name=recipes_list[i].get("name"), calories=recipes_list[i].get("calories"),
                                              fat=recipes_list[i].get("fat"), sugar=recipes_list[i].get("sugar"))
                    db.session.add(new_recipe)
                    db.session.commit()
                print("The recipes are added. Inspect the database file or re-run the app to see it.")
        
        if not inspector.has_table('ingredients_table'):    # Make sure the table exists before doing anything with it
            print("Ingredient table does not exist! did you run 'flask db upgrade' from the terminal?")
        else:
            current_ingredients = ingredients_table.query.all()
            # First, check to see if there is already data. If so, do not add your initial data.
            if current_ingredients:
                print("The ingredient table already exists! Printing all ingredients...")
                for i in current_ingredients:
                    print(f'\t{i}')
                print("I printed them!")
            else:
                print("No ingredients detected. Adding them")
                ingredientList = [
                    {'id': 1, 'name': 'Bananas'},
                    {'id': 2, 'name': 'Blueberries'},
                    {'id': 3, 'name': 'Cherries'},
                    {'id': 4, 'name': 'Kale'},
                    {'id': 5, 'name': 'Mangoes'},
                    {'id': 6, 'name': 'Oats'},
                    {'id': 7, 'name': 'Peaches'},
                    {'id': 8, 'name': 'Peanuts'},
                    {'id': 9, 'name': 'Strawberries'},
                    {'id': 10, 'name': 'Oranges'},
                    {'id': 11, 'name': 'Vanilla'},
                    {'id': 12, 'name': 'Coconut'},
                    {'id': 13, 'name': 'Pineapple'},
                    {'id': 14, 'name': 'Raspberries'}
                ]
                for i in range(len(ingredientList)):
                    new_ingredient = ingredients_table(id=ingredientList[i].get("id"), name=ingredientList[i].get("name"))
                    db.session.add(new_ingredient)
                    db.session.commit()
                print("The ingredients are added. Inspect the database file or re-run the app to see it.")

        if not inspector.has_table('filter_table'):
            print("Filter table does not exist! did you run 'flask db upgrade' from the terminal?")
        else:
            print("Filter table already exists!")
            # brown shake with nuts
            current_recipe[0].ingredients.append(current_ingredients[7])
            # Banana shake- bananas
            current_recipe[1].ingredients.append(current_ingredients[0])
            # Strawberry Banana Shake
            current_recipe[2].ingredients.append(current_ingredients[0])
            current_recipe[2].ingredients.append(current_ingredients[8])
            # Cherry-Blueberry Banana Shake
            current_recipe[3].ingredients.append(current_ingredients[0])
            current_recipe[3].ingredients.append(current_ingredients[1])
            current_recipe[3].ingredients.append(current_ingredients[2])
            # Orange Vanilla Shake
            current_recipe[4].ingredients.append(current_ingredients[9])
            current_recipe[4].ingredients.append(current_ingredients[10])
            # Triple Berry Oat Shake
            current_recipe[5].ingredients.append(current_ingredients[0])
            current_recipe[5].ingredients.append(current_ingredients[1])
            current_recipe[5].ingredients.append(current_ingredients[13])
            current_recipe[5].ingredients.append(current_ingredients[8])
            current_recipe[5].ingredients.append(current_ingredients[5])
            # Tropical Shake
            current_recipe[6].ingredients.append(current_ingredients[11])
            current_recipe[6].ingredients.append(current_ingredients[12])
            # Light orange shake
            current_recipe[7].ingredients.append(current_ingredients[4])
            # Light purple shake
            current_recipe[8].ingredients.append(current_ingredients[6])
            # Light red shak
            current_recipe[9].ingredients.append(current_ingredients[4])        
            # Light yellow shake
            current_recipe[10].ingredients.append(current_ingredients[1])
            current_recipe[10].ingredients.append(current_ingredients[0])
        	# White shake
            current_recipe[11].ingredients.append(current_ingredients[0])
            # Blue shake
            current_recipe[12].ingredients.append(current_ingredients[2])
            # Green shake
            current_recipe[13].ingredients.append(current_ingredients[4])
            # Dark blue shake
            current_recipe[14].ingredients.append(current_ingredients[2])
            # Light red shake
            current_recipe[15].ingredients.append(current_ingredients[8])        
            # Orange shake
            current_recipe[16].ingredients.append(current_ingredients[7])
        	# Purple shake
            current_recipe[17].ingredients.append(current_ingredients[2])
            # Yellow shake
            current_recipe[18].ingredients.append(current_ingredients[5])
            # Green with Kiwi shake
            current_recipe[19].ingredients.append(current_ingredients[4])
            db.session.commit()
                
            # Setting ingredients to the recipes they are in for the filter    
    with app.app_context():
        db.create_all()

    return app
