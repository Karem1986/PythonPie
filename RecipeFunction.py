# Create a python function so that guests can choose the type of meal and choose the specific option.
# Then, the chef receives a notification in the kitchen to prepare it.

def create_recipe():
    ask_name = input('Please enter your name')
    # Our meal options:
    # By using a set in Python, options can be modified and unordered. A list will also work.
    breakfast_options = {'toasts', 'pancakes', 'croissants'}
    lunch_options = {'hummus with grilled veggies', 'poke bowl with tofu', 'vegan quiche'}
    dinner_options = {'pizza', 'risotto', 'tofu with salad and bulgur'}

    which_meal = input(f"Which type of meal would you like to have {ask_name}: choose one option among breakfast, lunch or dinner?")

    if which_meal == 'breakfast':
        print(f'For breakfast we have{breakfast_options}')
        choice = input(
            f"Which breakfast would you like the chef to make {ask_name}: we have {breakfast_options}?")
        if choice == 'toasts':
            print('Your fruitcake will be ready in 30 mins.')
        else:
            print("In approx 15 mins a colleague will bring your chosen breakfast")
    elif which_meal == 'lunch':
        print(f'For lunch we have{lunch_options}')
    elif which_meal == 'dinner':
        print(f'For dinner we have{dinner_options}')

    return which_meal

# If import this file elsewhere, this block is completely ignored
if __name__ == "__main__":
    create_recipe()
