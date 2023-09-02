import json
from enum import Enum
from logger import configure_logger
logger = configure_logger(__name__)

 

class SUPERMARKET_MANGEMENT(Enum):
    ADD = 1
    PRINT = 2
    DELETE = 3
    EXIT = 4

class Item:
    def __init__(self, name, price, item_id,quantity):
        self.name = name
        self.price = price
        self.item_id = item_id
        self.quantity = quantity

All_items = []

def displaymenu():
    for action in SUPERMARKET_MANGEMENT:
        print(f'{action.name}={action.value}')

def read_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{file_path}'.")
        return None

def write_json(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data written to '{file_path}' successfully.")
    except json.JSONDecodeError:
        print(f"Error encoding JSON data to file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing data to '{file_path}': {str(e)}")

def menu():
    global All_items  # Use the global variable
    while True:
        displaymenu()
        userinput = int(input("enter your choice : "))
        if userinput == SUPERMARKET_MANGEMENT.ADD.value:
            add_func()
        elif userinput == SUPERMARKET_MANGEMENT.PRINT.value:
            print_items()
        elif userinput == SUPERMARKET_MANGEMENT.DELETE.value:
            delete_item()   
        elif userinput == SUPERMARKET_MANGEMENT.EXIT.value:
            save_data()
            break

def add_func():
    inputs = str(input("enter the item name : "))
    price = int(input("enter the item price : "))
    id = int(input("enter the item id : "))
    quantity = int(input("enter the item quantity"))
    new_item = Item(inputs, price, id, quantity)
    All_items.append(new_item)
    print(f' all items added : ')
    save_data()

def print_items():
    data = read_json("data.json")
    total_cost = sum(item.price * item.quantity for item in All_items)
    print(f'Inventory value: {total_cost}')
    if data is not None:
        for item in data:
            print(f'Name: {item["name"]}, Price: {item["price"]}, ID: {item["item_id"]} Quantity: {item["quantity"]}')
    else:
        print(" no data available")

def delete_item():
    global All_items  # Use the global variable
    data = read_json("data.json")
    if data is not None:
        name = input(" which name items you want to delete : ")
        for item in data:
            if item['name'] == name:
                All_items = [x for x in All_items if x.name != name]  # Update All_items list
                print(f' item deleted : {name}')
                save_data()
                break
        else:
            print(" no data available")

def save_data():
    global All_items  # Use the global variable
    write_json([item.__dict__ for item in All_items], "data.json")

if __name__ == "__main__":
    # Try to load data from JSON file when starting the program
    loaded_data = read_json("data.json")
    if loaded_data is not None:
        All_items = [Item(item['name'], item['price'], item['item_id'], item['quantity']) for item in loaded_data]
    print(f'all items loaded : {len(All_items)}')
    menu()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.error("This is an error message")
    











