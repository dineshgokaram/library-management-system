# main.py
from library import Library

def main():
    library = Library()

    print("Welcome to the Library Management System!")
    while True:
        print("\n--- Menu ---")
        print("1. Add a new item")
        print("2. Search for an item")
        print("3. Check out an item")
        print("4. Return an item")
        print("5. Display all items")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            category = input("Enter the category: ")
            library.add_item(title, author, category)
        elif choice == '2':
            query = input("Enter a search query (title, author, or category): ")
            results = library.search_item(query)
            if results:
                print("Search Results:")
                for item in results:
                    print(item)
            else:
                print("No items found.")
        elif choice == '3':
            title = input("Enter the title of the item to check out: ")
            library.check_out_item(title)
        elif choice == '4':
            title = input("Enter the title of the item to return: ")
            library.return_item(title)
        elif choice == '5':
            library.display_items()
        elif choice == '6':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
