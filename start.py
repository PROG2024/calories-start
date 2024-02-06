"""Starting code for a calorie calculator with graphical UI.

   1. Create a class for the GUI using this code.
   The class should have these methods:

   __init__(self)     Initialize window and attributes, call init_componennts()
   init_components()  Create, style, and arrange GUI components
   handle_select_food Write event handlers
   run(self)          Start Tkinter and wait for user input

   2. Write a small "app" script that instantiates and starts this class.

   3. Apply *dependency injection*:
   Modify the constructor to *set* the FoodCalculator instance in the
   UI instead of the UI creating a FoodCalculator instance itself.
"""
import tkinter as tk
from tkinter import ttk
from foodcalculator import FoodCalculator


# Create the FoodCalculator that we use to get foods and calories.

foodcalc = FoodCalculator()

# Create a Tkinter window and set a few properties

root = tk.Tk()
root.title("Calorie Calculator")

# initialize components in the window

# a variable that is tied to the input field to get/set the value

selected_food = tk.StringVar()

# event handler to do something when user selects a food

def handle_select_food(*args):
    """Handle a food selection event."""
    food_name = selected_food.get()
    calories = foodcalc.get_calories(food_name)
    # set the text in a label
    food_info['text'] = f"{calories} Calories"

# combobox containing list of food names
foodchooser = ttk.Combobox(root, textvariable=selected_food)
foodchooser['values'] = foodcalc.get_foods()
# show a food in the combo box
foodchooser.current(newindex=0)
# when something is selected, invoke the event handler
# '<<ComboboxSelected>>' is called a Virtual Event, enclosed in <<...>>
foodchooser.bind('<<ComboboxSelected>>', handle_select_food)

label = tk.Label(root, text="has")
# a label where we show number of calories
food_info = tk.Label(root, text="  ", width=12)

# position & size the components
# TODO improve size and spacing.  You can change to grid layout if you prefer.
foodchooser.pack(side=tk.LEFT)
label.pack(side=tk.LEFT)
food_info.pack(side=tk.LEFT)
 
# Run and wait for input
root.mainloop()

