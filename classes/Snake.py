from .LiknkedList import LinkedList


# Создаем обычную змеюку как связный список
class Snake:
    """Класс змеюки"""

    def __init__(self, head):
        self.head = head  # Координаты головы
        self.snake_color = (0, 255, 0)
        self.snake_start_size = 8
        self.direction = 0b00  # Направление следования змеи бинарно задаем
        self.body = LinkedList(head)  # Тут будет наш связный список который отвечает за туловище змеи
        self._initialize_snake(self.snake_start_size, head)

    def _initialize_snake(self, size, head):
        for i in range(size):
            self.body.add_node([head[0], head[1] - i])  # Тут будет наш связный список который отвечает за туловище змеи

    def get_snake_cords(self):
        """Получаем все координаты змеи"""
        item = self.body.get_item()
        out = []
        while item.has_next():
            out.append(item.next.get_cords())
            item = item.next
        return out

    def move(self, field_area):
        """Двигаем змею"""
        new_position = list(self.body.head.get_cords())
        if self.direction == 0b00:  # Вверх
            new_position[1] -= 1
        elif self.direction == 0b01:  # Вниз
            new_position[1] += 1
        elif self.direction == 0b10:  # Вправо
            new_position[0] += 1
        elif self.direction == 0b11:  # Влево
            new_position[0] -= 1

        if new_position[0] < 0:
            new_position[0] = field_area[0] - 1
        elif new_position[0] > field_area[0] - 1:
            new_position[0] = 0

        if new_position[1] < 0:
            new_position[1] = field_area[1] - 1
        elif new_position[1] > field_area[1] - 1:
            new_position[1] = 0
        self.body.add_node(new_position)
        self.body.delete_last_node()

    def change_direction(self, key):
        if key in [0b11, 0b10]:
            if self.direction not in [0b01, 0b00]:  # Все совпадает, ничего не делаем
                return
            else:
                self.direction = key
        elif key in [0b01, 0b00]:
            if self.direction not in [0b11, 0b10]:
                return
            else:
                self.direction = key

    def grow(self):
        """растим змею"""
