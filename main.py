from enum import Enum
import customers
import managerD
from logger import configure_logger
logger = configure_logger(__name__)


class MainDisplay(Enum):
    Manager = 1
    User = 2

    @staticmethod
    def menu():
        print("1. Manager")
        print("2. User")

if __name__ == "__main__":
    while True:
        MainDisplay.menu()
        user_input = input("Enter your choice (1/2/q to quit): ")
        
        if user_input == "1":
            # Manager menu
            managerD.menu()
        elif user_input == "2":
            # Customer menu
            customers.customer_menu()
        elif user_input.lower() == "q":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or q to quit.")
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.error("This is an error message")

