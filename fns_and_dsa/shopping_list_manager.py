# Define shopping list
shopping_list = []

# Define the display menu function


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. View List")
    print("3. Exit")

# Main program loop


def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                item = input("Enter the item to add: ")
                shopping_list.append(item)
            elif choice == 2:
                print("Your Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            elif choice == 3:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please choose between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Entry point
if __name__ == "__main__":
    main()
