import os

MENU = {
    "1": {"name": "Chicken Shawarma", "price": 8},
    "2": {"name": "Beef Burger", "price": 7},
    "3": {"name": "Chicken Burger", "price": 6},
    "4": {"name": "Fish Burger", "price": 5},
    "5": {"name": "Pizza", "price": 4},
}

SEPARATOR = "-----------------------------------"
INVALID_NUMBER_MSG = "Invalid input!\nThe number must be an integer greater than zero ^_^\n"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("Our Menu:\n")
    for item_id, details in MENU.items():
        print(f"{item_id}. {details['name']} - Price: ${details['price']}")
    print(SEPARATOR)


def take_order(current_order, current_nb_of_meals):
    """Loop until the user enters 0. Fills the two lists in place."""
    while True:
        show_menu()
        choice = input("\nEnter the meal number to order (or 0 to print the total amount with details): ")

        if choice == "0":
            return

        if choice not in MENU:
            clear_screen()
            print("Invalid input!\n")
            continue

        try:
            nb_of_meals = int(input("Enter the number of meals: "))
        except ValueError:
            nb_of_meals = 0

        if nb_of_meals <= 0:
            clear_screen()
            print(INVALID_NUMBER_MSG)
            continue

        current_order.append(MENU[choice])
        current_nb_of_meals.append(nb_of_meals)
        clear_screen()
        print("Great!\n")


def print_receipt(current_order, current_nb_of_meals):
    total_price = 0
    if current_order:
        print("\nYour meal/s:\n")
        for index, item in enumerate(current_order, start=1):
            nb = current_nb_of_meals[index - 1]
            line_total = item["price"] * nb
            print(f"{index}. {item['name']} x{nb} for ${line_total}")
            total_price += line_total
    print(f"\nTotal amount: ${total_price}\n")
    print(SEPARATOR + "\n")


def main():
    current_order = []
    current_nb_of_meals = []
    take_order(current_order, current_nb_of_meals)
    print_receipt(current_order, current_nb_of_meals)


if __name__ == "__main__":
    main()