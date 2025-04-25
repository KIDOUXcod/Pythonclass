class Beverage:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def dispense(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False
    
    def is_available(self):
        return self.quantity > 0
    
    def __str__(self):
        return f"{self.name} (${self.price:.2f}) - {self.quantity} available"

class VendingMachine:
    def __init__(self):
        # Initialize with 6 different beverages
        self.beverages = {
            'A1': Beverage("Cola", 1.50, 5),
            'A2': Beverage("Diet Cola", 1.50, 5),
            'B1': Beverage("Lemonade", 1.75, 5),
            'B2': Beverage("Iced Tea", 1.25, 5),
            'C1': Beverage("Bottled Water", 1.00, 5),
            'C2': Beverage("Sports Drink", 2.00, 5)
        }
        self.money_inserted = 0.0
    
    def display_selection(self):
        print("\nAvailable Beverages:")
        for code, beverage in self.beverages.items():
            if beverage.is_available():
                print(f"{code}: {beverage}")
            else:
                print(f"{code}: {beverage.name} - SOLD OUT")
        print(f"\nMoney inserted: ${self.money_inserted:.2f}")
    
    def insert_money(self, amount):
        if amount > 0:
            self.money_inserted += amount
            print(f"Added ${amount:.2f}. Total: ${self.money_inserted:.2f}")
        else:
            print("Please insert a positive amount.")
    
    def select_beverage(self, code):
        if code in self.beverages:
            beverage = self.beverages[code]
            if not beverage.is_available():
                print("Sorry, this beverage is sold out.")
                return
            
            if self.money_inserted >= beverage.price:
                if beverage.dispense():
                    change = self.money_inserted - beverage.price
                    print(f"Vending {beverage.name}... Enjoy your drink!")
                    if change > 0:
                        print(f"Dispensing ${change:.2f} in change.")
                    self.money_inserted = 0.0
                else:
                    print("Error dispensing beverage. Please try again.")
            else:
                needed = beverage.price - self.money_inserted
                print(f"Please insert ${needed:.2f} more to purchase {beverage.name}.")
        else:
            print("Invalid selection. Please try again.")
    
    def return_money(self):
        if self.money_inserted > 0:
            print(f"Returning ${self.money_inserted:.2f}.")
            self.money_inserted = 0.0
        else:
            print("No money to return.")
    
    def run(self):
        while True:
            self.display_selection()
            print("\nOptions:")
            print("1. Insert money")
            print("2. Select beverage")
            print("3. Return money")
            print("4. Exit (for demonstration purposes)")
            
            try:
                choice = input("Enter your choice (1-4): ")
                
                if choice == '1':
                    amount = float(input("Enter amount to insert: $"))
                    self.insert_money(amount)
                elif choice == '2':
                    code = input("Enter beverage code (e.g., A1, B2): ").upper()
                    self.select_beverage(code)
                elif choice == '3':
                    self.return_money()
                elif choice == '4':
                    print("Thank you for using the vending machine!")
                    break
                else:
                    print("Invalid choice. Please try again.")
                
                input("\nPress Enter to continue...")
            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")

# Create and run the vending machine
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()

print("Vending Machine project by Kidmar Desir")