import json
import managerD  # Importing managerD module to use the existing Item class and functions
from logger import configure_logger
logger = configure_logger(__name__)


# Global variables
shopping_cart = []

def read_items():
    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print("File 'data.json' not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from 'data.json'.")
        return None

def add_item_to_shopping_cart():
    items = read_items()
    if items:
        print("Available Items:")
        for item in items:
            print(f"ID: {item['item_id']}, Name: {item['name']}, Price: {item['price']}")
        
        item_id = int(input("Enter the ID of the item you want to add to the shopping cart: "))
        quantity = int(input("Enter the quantity: "))
        
        for item in items:
            if item["item_id"] == item_id:
                selected_item = managerD.Item(item["name"], item["price"], item["item_id"], quantity)
                shopping_cart.append(selected_item.__dict__)
                print(f"{selected_item.name} added to the shopping cart.")
                break
        else:
            print("Item not found.")

def delete_item_from_shopping_cart():
    if not shopping_cart:
        print("Shopping cart is empty.")
        return

    print("Shopping Cart:")
    for i, item in enumerate(shopping_cart):
        print(f"{i + 1}. Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

    try:
        item_index = int(input("Enter the number of the item to remove: ")) - 1
        if 0 <= item_index < len(shopping_cart):
            removed_item = shopping_cart.pop(item_index)
            print(f"{removed_item['name']} removed from the shopping cart.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def print_shopping_cart():
    if not shopping_cart:
        print("Shopping cart is empty.")
        return

    total_price = sum(item["price"] * item["quantity"] for item in shopping_cart)

    print("Shopping Cart:")
    for i, item in enumerate(shopping_cart):
        print(f"{i + 1}. Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

    print(f"Total Price: ${total_price:.2f}")

def checkout():
    print_shopping_cart()
    
    if not shopping_cart:
        print("Shopping cart is empty.")
        return

    total_price = sum(item["price"] * item["quantity"] for item in shopping_cart)
    
    pay = input("Do you want to pay for these items? (yes/no): ").strip().lower()
    if pay == "yes":
        print("The order is paid.")
        shopping_cart.clear()  # Clear the shopping cart after payment
    else:
        print("The order is not paid.")

def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Add Item to Shopping Cart")
        print("2. Delete Item from Shopping Cart")
        print("3. Print Shopping Cart")
        print("4. Checkout")
        print("5. Return to Main Menu")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            add_item_to_shopping_cart()
        elif choice == "2":
            delete_item_from_shopping_cart()
        elif choice == "3":
            print_shopping_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    customer_menu()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.error("This is an error message")
