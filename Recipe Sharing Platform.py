from abc import ABC, abstractmethod

class Recipe(ABC):
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.comments = []

    @abstractmethod
    def display_recipe(self):
        pass

    def add_comment(self, comment):
        self.comments.append(comment)

class VegetarianRecipe(Recipe):
    def __init__(self, title, ingredients, instructions, is_vegetarian=True):
        super().__init__(title, ingredients, instructions)
        self.is_vegetarian = is_vegetarian

    def display_recipe(self):
        print(f"\nVegetarian Recipe: {self.title}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print("Instructions:")
        for step in self.instructions:
            print(f"  - {step}")
        print("Comments:")
        for comment in self.comments:
            print(f"  - {comment}")

class DessertRecipe(Recipe):
    def __init__(self, title, ingredients, instructions, is_sweet=True):
        super().__init__(title, ingredients, instructions)
        self.is_sweet = is_sweet

    def display_recipe(self):
        print(f"\nDessert Recipe: {self.title}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print("Instructions:")
        for step in self.instructions:
            print(f"  - {step}")
        print("Comments:")
        for comment in self.comments:
            print(f"  - {comment}")

class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.favorite_recipes = []

    def save_recipe(self, recipe):
        self.favorite_recipes.append(recipe)

    def display_favorite_recipes(self):
        print(f"\nFavorite Recipes of {self.name}:")
        for recipe in self.favorite_recipes:
            recipe.display_recipe()

class Rating:
    def __init__(self, recipe, user, score):
        self.recipe = recipe
        self.user = user
        self.score = score

    def display_rating(self):
        print(f"\nRating for '{self.recipe.title}' by {self.user.name}: {self.score}")



if __name__ == "__main__":
    vegetarian_recipe = VegetarianRecipe("Vegetarian Pasta", ["Pasta", "Tomatoes", "Spinach"], ["Boil pasta", "Mix with tomatoes and spinach"])
    dessert_recipe = DessertRecipe("Chocolate Cake", ["Flour", "Sugar", "Cocoa"], ["Mix dry ingredients", "Bake in preheated oven"])

    user1 = User("Lexus", "lexus@gmail.com")

    user1.save_recipe(vegetarian_recipe)
    user1.save_recipe(dessert_recipe)

    user1.display_favorite_recipes()

    rating1 = Rating(vegetarian_recipe, user1, 5)
    rating2 = Rating(dessert_recipe, user1, 4)

    rating1.display_rating()
    rating2.display_rating()
