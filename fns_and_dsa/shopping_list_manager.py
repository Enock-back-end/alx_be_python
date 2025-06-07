# Global shopping list
shopping_list = []


def display_menu():
    print("=== Shopping List Manager ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")


def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to shopping list.")


def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from shopping list.")
    else:
        print(f"{item} not found in the shopping list.")


def view_list():
    print("Your shopping list:")
    for idx, item in enumerate(shopping_list, start=1):
        print(f"{idx}. {item}")


# Call display_menu at start
display_menu()

while True:
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_list()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
