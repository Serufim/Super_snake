import pygame
class GameField:
    """Класс игрового поля"""
    def __init__(self, screen):
        self._background_set_up(screen)
        self.size_field = (400,400) #Размер поля
        self.cell_size = 5 # Размер клетки в пыхселях
        self.game_area = (self.size_field[0] // self.cell_size, self.size_field[1] // self.cell_size)
        self._geometry_set_up(screen)

    def _geometry_set_up(self,screen):
        # Определяем размеры и границы поля
        self.size_x, self.size_y = self.size_field
        self.screen_x, self.screen_y = screen.get_size()
        # Начальные точки
        self.initial_x = (self.screen_x - self.size_x) // 2
        self.initial_y = (self.screen_y - self.size_y) // 2
        # Граничные точки
        self.final_x = self.initial_x + self.size_x
        self.final_y = self.initial_y + self.size_y

    def _background_set_up(self,screen):
        """Настраиваем фон"""
        self.background = pygame.Surface(screen.get_size())  # Вызываем объект surface размером с весь экран
        self.background = self.background.convert()  # Конвертируем в чо-то
        self.background.fill((0, 0, 0))  # Заливаем чернотой

    def _draw_area(self,screen):
        point_tl = (self.initial_x - 1, self.initial_y - 1)
        point_tr = (self.final_x + 1, self.initial_y - 1)
        point_bl = (self.initial_x - 1, self.final_y + 1)
        point_br = (self.final_x + 1, self.final_y + 1)
        pygame.draw.line(screen, (128, 128, 128), point_tl, point_bl, 2)
        pygame.draw.line(screen, (128, 128, 128), point_tl, point_tr, 2)
        pygame.draw.line(screen, (128, 128, 128), point_bl, point_br, 2)
        pygame.draw.line(screen, (128, 128, 128), point_tr, point_br, 2)

    def _draw_grid(self, screen):
        """Рисуем сетку на дисплее"""
        for i in range(1, self.game_area[0]):
            pygame.draw.line(screen, (128, 128, 128), [self.initial_x + i * self.cell_size, self.initial_y],
                             [self.initial_x + i * self.cell_size, self.final_y], 2)
        for i in range(1, self.game_area[1]):
            pygame.draw.line(screen, (128, 128, 128), [self.initial_x, self.initial_y + i * self.cell_size],
                             [self.final_x, self.initial_y + i * self.cell_size], 2)

    def _draw_snake(self,screen,snake):
        """Рисуем змею"""
        #Получаем координаты змеи
        cords = snake.get_snake_cords()
        #В цикле обрабатываем и рисуем на поверхности
        for cord in cords:
            position = (self.initial_x + cord[0] *self.cell_size + 1,
                        self.initial_y + cord[1] *self.cell_size + 1,
                        self.cell_size,
                        self.cell_size,)
            pygame.draw.rect(screen,snake.snake_color,position)

    def draw_frame(self,screen,snake):
        """Рисуем кадр"""
        #Заливаем все чернотой
        screen.blit(self.background, (0, 0))  # Заливаем дисплей
        self._draw_area(screen) # Рисуем границы
        #self._draw_grid(screen)
        self._draw_snake(screen,snake)

    def is_correct_position(self):
        """Проверяем, есть ли такая позиция"""
        pass
