italian_food = [
    "Pasta Bolognese",
    "Pepperoni pizza",
    "Margherita pizza",
    "Lasagna"
]

indian_food = [
    "Curry",
    "Chutney",
    "Samosa",
    "Naan"
]

def find_meal(name, menu):
    return name if name in menu else None

def select_meal(name, food_type):
    if food_type == "italian":
        return find_meal(name, italian_food)
    elif food_type == "indian":
        return find_meal(name, indian_food)
    else:
        return None

def display_available_meals(food_type):
    if food_type == "italian":
        print("\nAvailable Italian Meals: ")
        for meal in italian_food:
            print(meal)
        return True
    elif food_type == "indian":
        print("\nAvailable Indian Meals: ")
        for meal in indian_food:
            print(meal)
        return True
    else:
        print("\nInvalid food type")
        return False

def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order:
        return f"\nYou ordered {amount} {name}"
    else:
        return "\nMeal not found"

print("Welcome to the Food Order System!")

type_input = input("Enter the type of menu: ").lower()

if display_available_meals(type_input):
  name_input = input("\nEnter the exact name of the meal you'd like to order: ")
  amount_input = int(input("Enter the quantity you want to order: "))
  result = create_summary(name_input, amount_input, type_input)
  print(result)