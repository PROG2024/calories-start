"""Provides list of foods and nutritional info."""
from foods import Food


class FoodCalculator:

    def get_foods(self):
        """Get the known foods."""
        return list(Food)
    
    def get_calories(self, food_name: str) -> int:
        """Return the number of calories in a food."""
        # get a food from an Enum
        try:
            food = Food[food_name]
            return food.calories
        except KeyError:
            # unknown food
            return 0
        # Python "switch" statement


if __name__ == '__main__':
    # view food data
    calc = FoodCalculator()
    for food in calc.get_foods():
        print(f"A {food} has {calc.get_calories(food)} calories")
