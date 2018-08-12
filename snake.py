"""Собственно сейчас попробуем сделать змейку"""
import pygame
from collections import namedtuple
from pygame.locals import *
from classes.GameField import GameField
from classes.LiknkedList import LinkedList
from classes.Snake import Snake

def main():
    # Обычная инициализация
    pygame.init() #Ну собственно грузим сам pygame
    screen = pygame.display.set_mode((640, 480)) # Дисплей настраиваем
    pygame.display.set_caption('Заряженый петон') # Устанавливаем название игры
    # Заливаем фон
    pygame.display.flip() # А хз чо это
    field = GameField(screen)
    snake = Snake((10,10))
    clock = pygame.time.Clock()
    move_snake = pygame.USEREVENT + 1
    pygame.time.set_timer(move_snake, 200)
    while 1:
        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Левая стрелочка
                    snake.change_direction(0b11)
                elif event.key == pygame.K_RIGHT:  # Правая стрелочка
                    snake.change_direction(0b10)
                elif event.key == pygame.K_UP:  # Верхняя стрелочка
                    snake.change_direction(0b00)
                elif event.key == pygame.K_DOWN:  # Верхняя стрелочка
                    snake.change_direction(0b01)
            elif event.type == move_snake:
                snake.move(field.game_area)
        clock.tick(60)
        field.draw_frame(screen, snake)
        pygame.display.update()

if __name__ == "__main__":
    main()