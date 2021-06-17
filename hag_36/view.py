class UserInterface:
    def wait_user_answer(self):
        print('Действия:'
              '\n1 - добавить рецепт'
              '\n2 - удалить рецепт'
              '\n3 - посмотреть рецепт'
              '\n4 - посмотреть все рецепты'
              '\nq - выйти из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    def add_user_recipe(self):
        dict_recipe = {
            'Автор рецепта': None,
            'Тип рецепта': None,
            'Название кухни': None,
            'Название рецепта': None,
            'Список ингредиентов': None,
            'Описание': None
        }
        print(' Добавление рецепта ')
        for key in dict_recipe:
            dict_recipe[key] = input(f'Введите "{key}": ')
        return dict_recipe

    def get_user_recipe(self):
        user_recipe = input('Введите название рецепта: ')
        return user_recipe

    def show_user_recipe(self, recipe):
        print(' Информация о рецепте:')
        for key in recipe:
            print(f'{key}: {recipe[key]}')

    def user_show_all_recipes(self, recipes):
        print(' Все доступные рецепты:')
        for idx, recipe in enumerate(recipes, start=1):
            print(f'{idx}. {recipe}')
