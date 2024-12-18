# library_item.py
import datetime

class LibraryItem:
    """Class representing an item in the library."""
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_checked_out = False
        self.due_date = None

    def __str__(self):
        status = "Available" if not self.is_checked_out else f"Checked out (Due: {self.due_date})"
        return f"{self.title} by {self.author} - {self.category} - {status}"
