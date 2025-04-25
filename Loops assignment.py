# Function to print menu
def print_menu():
    print("\n🌮 Welcome to Taco Palace! 🌮")
    print("Please view the menu below and enter the number that represents your selection:\n")
    print("1. Tacos - $3.00")
    print("2. Burritos - $4.50")
    print("3. Nachos - $4.00")
    print("4. Quesadillas - $4.25")
    print("5. Quit\n")

# Function to get the price of an item
def get_price(choice):
    prices = {
        1: 3.00,   # Tacos
        2: 4.50,   # Burritos
        3: 4.00,   # Nachos
        4: 4.25    # Quesadillas
    }
    return prices.get(choice, 0)

# Function to get item name
def get_item_name(choice):
    items = {
        1: "Tacos",
        2: "Burritos",
        3: "Nachos",
        4: "Quesadillas"
    }
    return items.get(choice, "Unknown Item")

# Main program
order_list = []
total_price = 0.0

while True:
    print_menu()
    
    try:
        user_choice = int(input("Enter your selection (1-5): "))

        if user_choice == 5:
            break
        elif user_choice in [1, 2, 3, 4]:
            item_name = get_item_name(user_choice)
            item_price = get_price(user_choice)
            order_list.append(item_name)
            total_price += item_price
            print(f"You have selected: {item_name} - ${item_price:.2f}")
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Final Output
print("\n🧾 Your Taco Palace Order Summary:")
for item in order_list:
    print(f" - {item}")
print(f"Total Price: ${total_price:.2f}")
print("Gracias for dining at Taco Palace! 🌮🎉")
print("Loops Assignment by Kidmar Desir")