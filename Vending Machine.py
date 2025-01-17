import time
class VendingMachine:
    def __init__(self):
        self.categories = {
            "drinks": {
                "coke": 1.50,
                "pepsi": 1.40,
                "water": 1.00,
                "fanta": 1.30,
                "sprite": 1.20
            },
            "Snacks": {
                "chips": 0.80,
                "chocolate": 1.20,
                "biscuits": 0.90,
                "cookies": 1.10,
                "nuts": 1.50
            }
        }
        self.stock = {
            "coke": 5,
            "pepsi": 5,
            "water": 10,
            "fanta": 7,
            "sprite": 6,
            "chips": 7,
            "chocolate": 6,
            "biscuits": 8,
            "cookies": 5,
            "nuts": 4
        }

    def display_menu(self):
        print("\nAvailable Items:")
        for category, items in self.categories.items():
            print(f"\n{category}:")
            for item, price in items.items():
                print(f"  {item} - £{price:.2f} ({self.stock[item]} in stock)")

    def validate_input(self, prompt, valid_options):
        while True:
            choice = input(prompt).strip()
            if choice in valid_options:
                return choice
            print("Invalid input. Please try again.")

    def process_transaction(self, item, amount):
        price = self.categories[item["category"]][item["name"]]
        change = amount - price
        print(f"Dispensing {item['name']}... Please collect your change: £{change:.2f}")
        self.stock[item["name"]] -= 1

    def suggest_items(self, category):
        suggestions = [item for item in self.categories[category] if self.stock[item] > 0]
        if suggestions:
            print("\nYou might also like:")
            for suggestion in suggestions:
                print(f"  {suggestion}")

    def run(self):
        print("Welcome to the Vending Machine!")
        while True:
            self.display_menu()
            item_name = input("\nEnter the name of the item you want to purchase: ").strip()

            # Validate the item selection:
            item = None
            for category, items in self.categories.items():
                if item_name in items and self.stock[item_name] > 0:
                    item = {"name": item_name, "category": category}
                    break

            if not item:
                print("\nItem not available or out of stock. Please select another item.")
                continue

            price = self.categories[item["category"]][item["name"]]
            amount = float(input(f"\n{item['name']} costs £{price:.2f}. Enter payment amount: "))

            # Validate the payment: 
            if amount < price:
                print("\nInsufficient payment. Please try again.")
                continue

            self.process_transaction(item, amount)
            self.suggest_items(item["category"])

            another = self.validate_input("\nWould you like to buy another item? (yes/no): ", ["yes", "no"])
            if another == "no":
                print("\n 🤩 Thank you for using the Farhan's Vending Machine! Goodbye👋")
                break
            time.sleep(1)

# Run the Vending Machine:
vending_machine = VendingMachine()
vending_machine.run()


# Creating some helper functions to make the code easier to understand:
def print_separator():
    print("=" * 40)

def welcome_message():
    print_separator()
    print(" 👋 Welcome to the Farhan's Vending Machine 👋, Enjoy your experience.🌛")
    print_separator()

def goodbye_message():
    print_separator()
    print(" 🍻 Thank you for using the Farhan's Vending Machine, See you again 👌")
    print_separator()

# Using helper functions in the code:
welcome_message()
vending_machine.run()
goodbye_message()
