# ============================================================
#          SMART LIBRARY MANAGEMENT SYSTEM
#          Python + DSA Mini Project
# ============================================================

# -------------------- LINKED LIST ----------------------------

class Node:
    def __init__(self, book_id):
        self.book_id = book_id
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add book to linked list
    def add(self, book_id):
        new_node = Node(book_id)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Delete book from linked list
    def delete(self, book_id):
        if self.head is None:
            return False

        if self.head.book_id == book_id:
            self.head = self.head.next
            return True

        temp = self.head

        while temp.next:
            if temp.next.book_id == book_id:
                temp.next = temp.next.next
                return True
            temp = temp.next

        return False

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.book_id, end=" -> ")
            temp = temp.next

        print("None")


# -------------------- QUEUE ----------------------------------

class Queue:
    def __init__(self):
        self.items = []

    # Add student to waiting list
    def enqueue(self, student_name):
        self.items.append(student_name)

    # Remove first student
    def dequeue(self):
        if not self.items:
            return None

        return self.items.pop(0)

    # Display waiting list
    def display(self):
        if not self.items:
            print("Waiting list is empty.")
            return

        print("\nWaiting List:")
        for i, student in enumerate(self.items, start=1):
            print(f"{i}. {student}")

    def is_empty(self):
        return len(self.items) == 0


# -------------------- LIBRARY CLASS --------------------------

class Library:

    def __init__(self):
        # Dictionary / Hashing
        self.books = {}

        # Linked List
        self.book_list = LinkedList()

        # Waiting List
        self.waiting_list = {}

    # ---------------- ADD BOOK ----------------

    def add_book(self):
        try:
            book_id = int(input("Enter Book ID: "))

            if book_id in self.books:
                print("Book ID already exists!")
                return

            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            self.books[book_id] = {
                "title": title,
                "author": author,
                "available": True,
                "issued_to": None
            }

            self.book_list.add(book_id)

            print("Book added successfully!")

        except ValueError:
            print("Invalid Book ID!")

    # ---------------- DISPLAY BOOKS ----------------

    def display_books(self):
        if not self.books:
            print("No books available in library.")
            return

        print("\n" + "=" * 75)
        print("                         ALL BOOKS")
        print("=" * 75)

        print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Status':<15}")
        print("-" * 75)

        for book_id, book in self.books.items():

            if book["available"]:
                status = "Available"
            else:
                status = "Issued"

            print(
                f"{book_id:<8}"
                f"{book['title'][:23]:<25}"
                f"{book['author'][:18]:<20}"
                f"{status:<15}"
            )

    # ---------------- SEARCH BOOK ----------------

    def search_book(self):
        choice = input(
            "\nSearch by:\n"
            "1. Book ID\n"
            "2. Title\n"
            "3. Author\n"
            "Enter choice: "
        )

        # Hashing search
        if choice == "1":

            try:
                book_id = int(input("Enter Book ID: "))

                if book_id in self.books:
                    self.show_book(book_id)
                else:
                    print("Book not found.")

            except ValueError:
                print("Invalid Book ID!")

        # Linear searching
        elif choice == "2":

            title = input("Enter title to search: ").lower()
            found = False

            for book_id, book in self.books.items():

                if title in book["title"].lower():
                    self.show_book(book_id)
                    found = True

            if not found:
                print("Book not found.")

        # Linear searching
        elif choice == "3":

            author = input("Enter author name: ").lower()
            found = False

            for book_id, book in self.books.items():

                if author in book["author"].lower():
                    self.show_book(book_id)
                    found = True

            if not found:
                print("Book not found.")

        else:
            print("Invalid choice!")

    # Show single book
    def show_book(self, book_id):

        book = self.books[book_id]

        print("\nBook Details")
        print("-" * 40)
        print("Book ID :", book_id)
        print("Title   :", book["title"])
        print("Author  :", book["author"])

        if book["available"]:
            print("Status  : Available")
        else:
            print("Status  : Issued")
            print("Issued To:", book["issued_to"])

    # ---------------- ISSUE BOOK ----------------

    def issue_book(self):

        try:
            book_id = int(input("Enter Book ID to issue: "))

            if book_id not in self.books:
                print("Book not found.")
                return

            book = self.books[book_id]

            if book["available"]:

                student = input("Enter Student Name: ")

                book["available"] = False
                book["issued_to"] = student

                print(f"Book issued successfully to {student}.")

            else:

                print("Book is already issued.")

                student = input(
                    "Enter Student Name to add to waiting list: "
                )

                if book_id not in self.waiting_list:
                    self.waiting_list[book_id] = Queue()

                self.waiting_list[book_id].enqueue(student)

                print(
                    f"{student} added to waiting list "
                    f"for Book ID {book_id}."
                )

        except ValueError:
            print("Invalid Book ID!")

    # ---------------- RETURN BOOK ----------------

    def return_book(self):

        try:
            book_id = int(input("Enter Book ID to return: "))

            if book_id not in self.books:
                print("Book not found.")
                return

            book = self.books[book_id]

            if book["available"]:
                print("This book is already available.")
                return

            previous_student = book["issued_to"]

            book["available"] = True
            book["issued_to"] = None

            print(
                f"Book returned successfully by "
                f"{previous_student}."
            )

            # Check waiting list
            if (
                book_id in self.waiting_list
                and not self.waiting_list[book_id].is_empty()
            ):

                next_student = self.waiting_list[book_id].dequeue()

                book["available"] = False
                book["issued_to"] = next_student

                print(
                    f"Book automatically issued to waiting "
                    f"student: {next_student}"
                )

        except ValueError:
            print("Invalid Book ID!")

    # ---------------- DELETE BOOK ----------------

    def delete_book(self):

        try:
            book_id = int(input("Enter Book ID to delete: "))

            if book_id not in self.books:
                print("Book not found.")
                return

            if not self.books[book_id]["available"]:
                print("Issued book cannot be deleted.")
                return

            del self.books[book_id]

            # Delete from Linked List
            self.book_list.delete(book_id)

            # Delete waiting list if exists
            if book_id in self.waiting_list:
                del self.waiting_list[book_id]

            print("Book deleted successfully!")

        except ValueError:
            print("Invalid Book ID!")

    # ---------------- SORT BOOKS ----------------

    def sort_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\nSort Books By:")
        print("1. Book ID")
        print("2. Title")
        print("3. Author")

        choice = input("Enter choice: ")

        # Convert dictionary data to list
        book_data = list(self.books.items())

        # Manual Bubble Sort
        n = len(book_data)

        for i in range(n - 1):

            for j in range(n - i - 1):

                current_id, current_book = book_data[j]
                next_id, next_book = book_data[j + 1]

                swap = False

                if choice == "1":

                    if current_id > next_id:
                        swap = True

                elif choice == "2":

                    if (
                        current_book["title"].lower()
                        > next_book["title"].lower()
                    ):
                        swap = True

                elif choice == "3":

                    if (
                        current_book["author"].lower()
                        > next_book["author"].lower()
                    ):
                        swap = True

                else:
                    print("Invalid choice!")
                    return

                if swap:
                    book_data[j], book_data[j + 1] = (
                        book_data[j + 1],
                        book_data[j]
                    )

        print("\nBooks after sorting:")
        print("-" * 75)

        print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Status':<15}")
        print("-" * 75)

        for book_id, book in book_data:

            status = (
                "Available"
                if book["available"]
                else "Issued"
            )

            print(
                f"{book_id:<8}"
                f"{book['title'][:23]:<25}"
                f"{book['author'][:18]:<20}"
                f"{status:<15}"
            )

    # ---------------- AVAILABLE BOOKS ----------------

    def show_available_books(self):

        found = False

        print("\n" + "=" * 70)
        print("                    AVAILABLE BOOKS")
        print("=" * 70)

        for book_id, book in self.books.items():

            if book["available"]:

                print(
                    f"ID: {book_id} | "
                    f"Title: {book['title']} | "
                    f"Author: {book['author']}"
                )

                found = True

        if not found:
            print("No books are currently available.")

    # ---------------- ISSUED BOOKS ----------------

    def show_issued_books(self):

        found = False

        print("\n" + "=" * 70)
        print("                     ISSUED BOOKS")
        print("=" * 70)

        for book_id, book in self.books.items():

            if not book["available"]:

                print(
                    f"ID: {book_id} | "
                    f"Title: {book['title']} | "
                    f"Issued To: {book['issued_to']}"
                )

                found = True

        if not found:
            print("No books are currently issued.")

    # ---------------- WAITING LIST ----------------

    def show_waiting_list(self):

        if not self.waiting_list:
            print("No waiting list available.")
            return

        print("\n" + "=" * 70)
        print("                     WAITING LIST")
        print("=" * 70)

        found = False

        for book_id, queue in self.waiting_list.items():

            if not queue.is_empty():

                found = True

                print(f"\nBook ID: {book_id}")
                print(f"Book Title: {self.books[book_id]['title']}")

                queue.display()

        if not found:
            print("Waiting list is empty.")

    # ---------------- LINKED LIST DISPLAY ----------------

    def show_linked_list(self):

        print("\nBook IDs stored in Linked List:")
        self.book_list.display()


# ============================================================
#                       MAIN PROGRAM
# ============================================================

def main():

    library = Library()

    while True:

        print("\n")
        print("=" * 60)
        print("          SMART LIBRARY MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1.  Add Book")
        print("2.  Display Books")
        print("3.  Search Book")
        print("4.  Issue Book")
        print("5.  Return Book")
        print("6.  Delete Book")
        print("7.  Sort Books")
        print("8.  Show Available Books")
        print("9.  Show Issued Books")
        print("10. Waiting List")
        print("11. Show Linked List")
        print("0.  Exit")

        print("=" * 60)

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.delete_book()

        elif choice == "7":
            library.sort_books()

        elif choice == "8":
            library.show_available_books()

        elif choice == "9":
            library.show_issued_books()

        elif choice == "10":
            library.show_waiting_list()

        elif choice == "11":
            library.show_linked_list()

        elif choice == "0":
            print("\nThank you for using Smart Library Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Start program
if __name__ == "__main__":
    main()