from model import RecipesBase
from view import UserInterface


class Controller:
    def __init__(self):
        self.recipes_base = RecipesBase()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            self.add_recipe()
        elif answer == '2':
            self.remove_recipe()
        elif answer == '3':
            self.show_recipe()
        elif answer == '4':
            self.show_all_recipes()
        elif answer == 'q':
            pass
        else:
            print(f'Команды {answer} не существует!')

    def add_recipe(self):
        recipe = self.user_interface.add_user_recipe()
        self.recipes_base.add_recipe(recipe)

    def show_recipe(self):
        user_recipe = self.user_interface.get_user_recipe()
        recipe = self.recipes_base.get_recipe_by_title(user_recipe)
        self.user_interface.show_user_recipe(recipe)

    def remove_recipe(self):
        user_recipe = self.user_interface.get_user_recipe()
        self.recipes_base.remove_recipe(user_recipe)

    def show_all_recipes(self):
        recipes = self.recipes_base.get_all_recipes()
        self.user_interface.user_show_all_recipes(recipes)
