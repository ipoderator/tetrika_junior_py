
""" 
Обозначаем стороны прямоугольников. Для удобства и что-бы код был менее 
громоздким, решил обозначать стороны просто числами(one,two...)
"""
from test import * 

class Rectangle():

    def __init__(self, x1: int, y1: int, x2: int, y2: int, 
                        x3: int, y3: int, x4: int, y4: int) -> None:
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
 
        
    """ Функиця нахождения пересечения прямоугольников"""
    def intersection(self: int) -> bool :
                
        one = [self.x1, self.x2] # Первая сторона
        two = [self.x3, self.x4] # Вторая сторона
        three = [self.y1, self.y2] # Третья строна
        four = [self.y3, self.y4] # Четвертая сторона
        
        
        # Если стороны не пересекаются, то выводит False, пересекаются True
        if (max(one) < min(two)) or (max(three) < min(four)) or (min(three) > max(four)):
            return False     
        else:
            return True  
        
    
    """ Функция нахождения площади пересечения """
    def intersection_area(self: int) -> int:
        
        # Нахожу границы пересечения 
        one = max(self.x1, self.x3)
        four = max(self.y1, self.y3)
        three = min(self.x2, self.x4)
        two = min(self.y2, self.y4)
        
        
        #  Далее нахожу ширину и высоту пересечения
        width = three - one # Ширина
        height = two - four # Высота
        
        
        """ 
        Если удовлетворяет условие то выводит число - 0.
        Если нет, то площадь пересечения
        """
        
        if width <= 0 or height <= 0:
            return (f"Его площадь пересечения равна - {0}. Они не пересекаются")
        else:
            return (f"Площадь пересечения равна - {width * height}")
     

if __name__ == "__main__":
    
    rectangle1 = (Rectangle(1, 1, 2, 2, 3, 3, 4, 4)) # False
    print(rectangle1.intersection())
    print(rectangle1.intersection_area())
    
    rectangle2 = (Rectangle(10, 10, 200, 200, 211, 210, 10, 10)) # True
    print(rectangle2.intersection())
    print(rectangle2.intersection_area())
    
    rectangle3 = (Rectangle(2, 1, 4, 5, 1, 2, 5, 4)) # True
    print(rectangle3.intersection())
    print(rectangle3.intersection_area()) 

