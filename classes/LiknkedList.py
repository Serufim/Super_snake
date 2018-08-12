class LinkedList:
    """Собственно класс для связного списка"""
    def __init__(self,start=None):
        self.head = Node(start)
        self.initial = self.head

    def add_node(self, cords):
        new_node = Node(cords)
        self.head.next = new_node
        self.head = new_node

    def taversing(self):
        start_node = self.initial
        while True :
            print(start_node.get_cords())
            if start_node.next is None:
                break
            start_node = start_node.next

    def get_last_node(self):
        start_node = self.initial
        while True:
            new_node = start_node.next
            if new_node.next is None:
                return start_node
            else:
                start_node = new_node

    def delete_last_node(self):
        self.initial = self.initial.next

    def get_item(self):
        return self.initial



class Node:
    """Узел связного списка"""
    def __init__(self,cords):
        self.x, self.y = cords
        self.next = None # Указатель на след элемент, изначально равен нулю

    def get_cords(self):
        return (self.x, self.y)

    def has_next(self):
        return True if self.next is not None else False

if __name__ == '__main__':
    my_list = LinkedList((1,2))
    my_list.add_node((10,11))
    my_list.add_node((11,12))
    my_list.taversing()
    print('-----------')
    my_list.delete_first_node()
    my_list.taversing()
    del my_list
    print('Имитация движения')
    my_list = LinkedList((1,1))
    my_list.add_node((1,2))
    my_list.add_node((1,3))
    my_list.taversing()
    print('----------')
    my_list.add_node((1,4))
    my_list.delete_last_node()
    my_list.taversing()
    print('----------')
    my_list.add_node((1,5))
    my_list.delete_last_node()
    my_list.taversing()
    print('----------')
    my_list.add_node((1,6))
    my_list.delete_last_node()
    my_list.taversing()
