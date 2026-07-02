import os
menu = {
    "1": {"name": "Chicken Shawarma", "price": 8},
    "2": {"name": "Beef Burger", "price": 7},
    "3": {"name": "Chicken Burger", "price": 6},
    "4": {"name": "Fish Burger", "price": 5},
    "5": {"name": "Pizza", "price": 4},
}
def show_menu():
    for item_id, details in menu.items():
        print(f"{item_id}. {details['name']} - Price: ${details['price']}")
    print('-----------------------------------')
current_order = []
current_nb_of_meals = []
totalPrice = 0
while True:
    print("Our Menu:\n")
    show_menu()
    choice = input("\nEnter the meal number to order (or 0 to print the total amount with details): ")
    if choice == "0":
        if len(current_order) > 0:
            print("\nYour meal/s:\n")
            index = 1
            for item in current_order:
                current_nb = current_nb_of_meals[index - 1]
                print(f"{index}. {item['name']} x{current_nb} for ${item['price'] * current_nb}")
                index = index + 1
                totalPrice = totalPrice + item['price'] * current_nb
        print(f"\nTotal amount: ${totalPrice}\n")
        print('-----------------------------------\n')
        break
    elif choice in menu:
        try:
            nb_of_meals = int(input("Enter the number of meals: "))
            if nb_of_meals > 0:
                current_nb_of_meals.append(nb_of_meals)
                current_order.append(menu[choice])
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid input!\nThe number must be an integer greater than zero ^_^\n")
                continue
        except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid input!\nThe number must be an integer greater than zero ^_^\n")
                continue
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Great!\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid input!\n")
