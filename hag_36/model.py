class Recipe:
    def __init__(self, author, r_type, kitchen, title, ingredients, description):
        self.author = author
        self.r_type = r_type
        self.kitchen = kitchen
        self.title = title
        self.ingredients = ingredients
        self.description = description

    def __repr__(self):
        return f'{self.author}. "{self.title}"'


class RecipesBase:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe):
        recipe = Recipe(*recipe.values())
        self.recipes[recipe.title] = recipe

    def remove_recipe(self, title):
        try:
            self.recipes.pop(title)
        except KeyError:
            print('Такого рецепта нет')

    def get_recipe_by_title(self, title):
        recipe: Recipe = self.recipes[title]
        recipe_dict = {
            'Автор рецепта': recipe.author,
            'Тип рецепта': recipe.r_type,
            'Название кухни': recipe.kitchen,
            'Название рецепта': recipe.title,
            'Список ингредиентов': recipe.ingredients,
            'Описание': recipe.description
        }
        return recipe_dict

    def get_all_recipes(self):
        return self.recipes.values()
