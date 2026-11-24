# 🍽️ Restaurant Ordering CLI

A Python CLI restaurant ordering system with a structured menu, quantity tracking, total price calculation, and input validation. Built as a foundation for a future full-stack application.

---

## ✨ Key Features

- **Structured Menu Display:** Displays menu items and prices dynamically from a dictionary.
- **Multi-Item Ordering:** Order multiple meals with custom quantities in a single session.
- **Input Validation:** Handles invalid menu selections, non-numeric input, and invalid quantities using `try-except` blocks without crashing.
- **Order Summary:** Generates an itemized receipt with quantities and the total price at checkout.

---

## 🛠️ Tech Stack

- Python 3.x

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/ezzcodes-hub/restaurant-ordering-cli.git
cd restaurant-ordering-cli
```

2. Run the application:

```bash
python foodOrder.py
```

---

## 💡 Example Output

```text
Our Menu:

1. Chicken Shawarma - Price: $8
2. Beef Burger - Price: $7
3. Chicken Burger - Price: $6
4. Fish Burger - Price: $5
5. Pizza - Price: $4

----------------------------------------

Enter the meal number to order (or 0 to print the total amount with details): 2
Enter the number of meals: 3

Great!

Our Menu:

1. Chicken Shawarma - Price: $8
2. Beef Burger - Price: $7
3. Chicken Burger - Price: $6
4. Fish Burger - Price: $5
5. Pizza - Price: $4

----------------------------------------

Enter the meal number to order (or 0 to print the total amount with details): 0

Your meal/s:

1. Beef Burger x3 for $21

Total amount: $21

----------------------------------------
```

---

## ⭐️ Future Improvements

- 🗄️ Store menu items and orders in a SQLite or PostgreSQL database.
- ✏️ Allow users to edit or remove items before checkout.
- 🌐 Build a web interface using Flask or Django.
- 🔌 Develop a REST API for menu and order management.
- 👤 Add user authentication and order history.