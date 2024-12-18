# library.py
from library_item import LibraryItem
import datetime

class Library:
    """Class representing the library system."""
    def __init__(self):
        self.items = []

    def add_item(self, title, author, category):
        new_item = LibraryItem(title, author, category)
        self.items.append(new_item)
        print(f"Item '{title}' added successfully.")

    def search_item(self, query):
        results = [item for item in self.items if 
                   query.lower() in item.title.lower() or 
                   query.lower() in item.author.lower() or 
                   query.lower() in item.category.lower()]
        return results

    def check_out_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower() and not item.is_checked_out:
                item.is_checked_out = True
                item.due_date = datetime.date.today() + datetime.timedelta(days=14)
                print(f"Item '{title}' checked out successfully. Due date: {item.due_date}")
                return
        print(f"Item '{title}' is not available for checkout.")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower() and item.is_checked_out:
                item.is_checked_out = False
                overdue_days = (datetime.date.today() - item.due_date).days if item.due_date else 0
                if overdue_days > 0:
                    fine = overdue_days * 2  # Example fine: $2 per day
                    print(f"Item '{title}' returned with a fine of ${fine}.")
                else:
                    print(f"Item '{title}' returned successfully.")
                item.due_date = None
                return
        print(f"Item '{title}' is not checked out or doesn't exist.")

    def display_items(self):
        if not self.items:
            print("No items in the library.")
        else:
            for item in self.items:
                print(item)
