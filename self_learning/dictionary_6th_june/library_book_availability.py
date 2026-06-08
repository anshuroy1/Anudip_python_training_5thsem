#  Display books that are currently unavailable.
# • Count the number of available books.
# • Find the book with the maximum copies.
# • Create a list of books having less than 3 copies.
# • Calculate the total number of books available.

# Library Book Availability

books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Unavailable books
print("Unavailable Books:")

for book, copies in books.items():
    if copies == 0:
        print(book)

# Count available books
count = 0

for copies in books.values():
    if copies > 0:
        count += 1

print("\nAvailable Books:", count)

# Book with maximum copies
max_book = ""
max_copies = 0

for book, copies in books.items():
    if copies > max_copies:
        max_copies = copies
        max_book = book

print("\nBook with Maximum Copies:")
print(max_book, ":", max_copies)

# Books having less than 3 copies
low_stock = []

for book, copies in books.items():
    if copies < 3:
        low_stock.append(book)

print("\nBooks Having Less Than 3 Copies:")
print(low_stock)

# Total books available
total = 0

for copies in books.values():
    total += copies

print("\nTotal Number of Books:", total)