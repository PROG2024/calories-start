from enum import Enum

class Food(Enum):
    Apple = 75
    Banana = 80
    Cantalope = 110
    Durian = 90
    Orange = 62

    @property
    def calories(self):
        return self.value

    def __str__(self):
        return self.name
