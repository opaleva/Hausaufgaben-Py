import random
import sys
from collections import defaultdict

import pygame


class Game:
    """Класс игры, который содержит в себе основные настроки."""
    def __init__(self, width, height, caption, background, frame_rate):
        """
        caption - название окошка
        background - задний фон игры
        frame_rate - FPS игры
        surface - поверхность, на которой отображатся все игровые объекты
        clock - нужен для манипулирования fps
        mouse_handlers - словарь с событиями мышки с парами 'событие': [список методов-хендлеров каждого объекта, которому нужна мышка]
        """
        pygame.init()
        self.caption = caption
        self.background = background
        self.frame_rate = frame_rate
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        self.mouse_handlers = defaultdict(list)  # {pygame.MOUSEMOTION: [obj1], pygame.MOUSEBUTTONDOWN: [obj1, obj2, ...]}
        self.game_objects = []

    def start_game(self):
        """Главный игровой метод. Содержит бесконечный цикл, внутри которого работает всё."""
        pygame.mixer.music.load('datei/Kill_The_Target.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        while True:
            self.surface.blit(self.background, [0, 0])
            self.handle_events()
            self.update()
            self.blit(self.surface)
            pygame.display.update()

    def blit(self, surface):
        """Метод, отображающий все объекты"""
        for obj in self.game_objects:
            obj.blit(surface)

    def update(self):
        """Метод, обновляющий положения всех объектов."""
        for obj in self.game_objects:
            obj.update()

    # Обработчик событий
    def handle_events(self):
        """Главный обработчик игровых событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                for handler in self.mouse_handlers[event.type]:
                    handler(event.type, event.pos)


class Tir(Game):
    """Класс игровой логики, где связаны все объекты между собой и реализовано их взаимодействие"""
    def __init__(self):
        """
        score - показатель игровых очков
        scope - прицел
        target - цель
        """
        super().__init__(800, 630, 'Psycho shooter', (0, 0, 0), 60)
        self.score = 0
        self.scope = None
        self.target = None
        self.background = pygame.image.load('datei/stadt.jpg')
        self.create_objects()

    def create_objects(self):
        """Метод, вызывающий все остальные методы, которые что-то создают"""
        self.create_target()
        self.create_scope()
        self.create_labels()

    def create_scope(self):
        """Метод, создающий прицел"""
        self.scope = Scope()

        # Добавляем все события мышки в словарь
        self.mouse_handlers[pygame.MOUSEMOTION].append(self.scope.handle_mouse)
        self.mouse_handlers[pygame.MOUSEBUTTONDOWN].append(self.scope.handle_mouse)

        # Добавляем созданного игрока в список игровых объектов
        self.game_objects.append(self.scope)

    def create_target(self):
        """Метод, создающий цель"""
        self.target = Target('datei/etwas.png')
        self.game_objects.append(self.target)
        self.target2 = Target('datei/pumpkin.png')
        self.game_objects.append(self.target2)


    def create_labels(self):
        """Метод, создающий игровые надписи"""

        # Создание объектов для надписей
        text_obj11 = TextObject(360, 5, lambda: f'Score: ', (74, 61, 32), 'datei/deutsch-gothic.ttf', 18)
        text_obj12 = TextObject(420, 3, lambda: f' {self.score}', (170, 0, 0), 'datei/deutsch-gothic.ttf', 20)

        text_obj21 = TextObject(360, 30, lambda: f'Shots: ', (100, 61, 32), 'datei/deutsch-gothic.ttf', 18)
        text_obj22 = TextObject(420, 28, lambda: f' {self.scope.count_shot}', (170, 0, 0), 'datei/deutsch-gothic.ttf', 20)

        # Добавляем созданные надписи в список игровых объектов
        self.game_objects.append(text_obj11)
        self.game_objects.append(text_obj12)
        self.game_objects.append(text_obj21)
        self.game_objects.append(text_obj22)

    def handle_shot(self):
        """Обработчик выстрелов"""
        if self.scope.shot.colliderect(self.target.rect):
            self.score += 2
            self.target.change_position()
        if self.scope.shot.colliderect(self.target2.rect):
            self.score += 1
            self.target2.change_position()


    def update(self):
        """Запускает все хендлеры и вызывает update родителя"""
        self.handle_shot()
        super().update()


class Scope:
    """Класс игрового прицела. В начале каждой игры имеет случайный цвет"""
    def __init__(self):
        """
        red - на сколько много красного
        green - на сколько много зеленого
        blue - на сколько много синего
        linecolor - кортеж из трёх цветов выше
        x_mouse_pos - положение мышки на оси Х
        y_mouse_pos - положение мышки на оси Y
        size_scope - размер прицела
        shot_sound - объект звука, который отвечает за выстрел
        shot - прямоугольник 1х1 пикселей, который является выстрелом
        count_shot - счетчик выстрелов
        """
        self.linecolor = (54, 41, 12)
        self.x_mouse_pos = 0
        self.y_mouse_pos = 0
        self.size_scope = 8
        self.shot_sound = pygame.mixer.Sound('datei/shot.wav')
        self.shot_sound.set_volume(0)
        self.shot = pygame.Rect(-1, -1, 1, 1)
        self.count_shot = 0

    def handle_mouse(self, event_type, event_pos):
        """Обработчик мыши, на вход получает тип события и его координаты"""
        if event_type == pygame.MOUSEMOTION:
            self.x_mouse_pos, self.y_mouse_pos = event_pos
        if event_type == pygame.MOUSEBUTTONDOWN:
            self.shoot()

    def shoot(self):
        """Метод, который отвечает за выстрел"""
        self.shot_sound.play()
        self.shot = pygame.Rect(self.x_mouse_pos, self.y_mouse_pos, 1, 1)
        self.count_shot += 1

    def update(self):
        """
        Метод, отвечающий за обновление состояния прицела. Он пустой, так как прицел - это две линии, которые
        рисуются в методе blit()
        """
        pass

    def blit(self, surface):
        """Метод, отображающий прицел. Отображение происходит за счет отрисовки двух линий"""

        # Горизонтальная линия
        pygame.draw.line(surface, self.linecolor, (self.x_mouse_pos - self.size_scope, self.y_mouse_pos), (self.x_mouse_pos + self.size_scope, self.y_mouse_pos), 3)
        # Вертикальная линия
        pygame.draw.line(surface, self.linecolor, (self.x_mouse_pos, self.y_mouse_pos - self.size_scope), (self.x_mouse_pos, self.y_mouse_pos + self.size_scope), 3)


class Target:
    """Класс цели, по которой стреляем"""
    def __init__(self, image):
        """
        image - surface-объект картинки цели
        rect - прямоугольник с координатами, в который вписывеются картинка
        """
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.rect.w)
        self.rect.y = random.randint(0, 630 - self.rect.h)

    def update(self):
        """
        Метод, отвечающий за обновление состояния цели. Он пустой, так как она никуда не передвигается сама, только
        когда по ней попали встрелом
        """
        pass

    def blit(self, surface):
        """Метод, отображающий цель"""
        surface.blit(self.image, self.rect)

    def change_position(self):
        """Метод, меняющий позицию цели"""
        self.rect.x = random.randint(0, 800 - self.rect.w)
        self.rect.y = random.randint(60, 630 - self.rect.h)


class TextObject:
    """Класс текста"""
    def __init__(self, x, y, text_func, color, font_name, font_size):
        """
        x - координата Х надписи
        y - координата Y надписи
        text_func - функция, возвращающая текст. Обычно это что-то вроде lambda: f'Score: {self.score}'
        color - цвет надписи
        font - объект шрифта, который создаётся на основе шрифта и размера
        bounds - границы/прямоугольник/поверхность, на которой находится текст
        """
        self.x = x
        self.y = y
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.Font(font_name, font_size)
        self.bounds = self.get_surface(text_func())  # lambda: f'Score: {self.score}'

    def update(self):
        """
        Метод, отвечающий за обновление состояния текста. Он пустой, так как текст никуда не передвигается
        """
        pass

    def blit(self, surface):
        """Метод, отображающий текст"""
        text_surface, text_rect = self.get_surface(self.text_func())
        surface.blit(text_surface, (self.x, self.y))

    def get_surface(self, text):
        """Метод, возвращающий поверхность, содержащую текст и прямоугольник, в который вписана эта поверхность"""
        text_surface = self.font.render(text, True, self.color)
        return text_surface, text_surface.get_rect()


# "Запускатр" игры
if __name__ == '__main__':
    Tir().start_game()
