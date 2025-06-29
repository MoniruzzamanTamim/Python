# Base class
class Person:
    def __init__(self, name, email):
        self.__name = name          # Encapsulated
        self.__email = email        # Encapsulated

    def show_info(self):
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")


# Inherited class: Staff
class Staff(Person):
    def __init__(self, name, email, staff_id, position):
        super().__init__(name, email)
        self.staff_id = staff_id
        self.position = position

    def show_info(self):
        super().show_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Position: {self.position}")


# Inherited class: Member
class Member(Person):
    def __init__(self, name, email, member_id, membership_type):
        super().__init__(name, email)
        self.member_id = member_id
        self.membership_type = membership_type
        self.borrowed_books = []  # Track borrowed booksok

    def show_info(self):
        super().show_info()
        print(f"Member ID: {self.member_id}")
        print(f"Membership Type: {self.membership_type}")
        print(f"Borrowed Books: {[book.title for book in self.borrowed_books]}")

    def borrow_book(self, book):
        if book.available:
            if len(self.borrowed_books) < 2 or self.membership_type.lower() == "premium":
                book.borrow_book()
                self.borrowed_books.append(book)
                print(f"{book.title} borrowed successfully.")
            else:
                print("Borrow limit reached for Regular member.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{book.title} returned successfully.")
        else:
            print("You did not borrow this book.")


# Independent class: Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
        else:
            print("Book already borrowed.")

    def return_book(self):
        self.available = True

    def show_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")
        print("-" * 30)

# -------------------------
# ✅ Sample Usage
# -------------------------

# Staff instance
staff1 = Staff("Mr. Hossain", "hossain@library.com", "S101", "Librarian")
print("🧑‍💼 Staff Info:")
staff1.show_info()
print("\n")

# Member instance
member1 = Member("Anika Rahman", "anika@mail.com", "M501", "Regular")
print("👩‍🎓 Member Info:")
member1.show_info()
print("\n")

# Book instances
book1 = Book("Python Programming", "John Doe", "ISBN123")
book2 = Book("Data Structures", "Jane Smith", "ISBN456")

print("📚 Book Info:")
book1.show_info()
book2.show_info()

# Borrow and return books
print("🔁 Borrowing and Returning:")
member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book2)  # Should warn about limit

print("\n📚 Book Status After Borrowing:")
book1.show_info()
book2.show_info()

member1.return_book(book1)

print("\n📚 Book Status After Returning:")
book1.show_info()

print("\n👩‍🎓 Updated Member Info:")
member1.show_info()
