# Smart Library Management System
# Problem Statement
# Create a digital library management system.
# Example Structure
# library = {
# "B101": {
# "title": "Python Basics",
# "author": "ABC",
# "copies": 5
# }
# }
# Maintain records of at least 30 books.
# Requirements
# 1. Add a book.
# 2. Remove a book.
# 3. Search a book by ID.
# 4. Search by title.
# 5. Update available copies.
# 6. Issue a book.
# 7. Return a book.
# 8. Display books with fewer than 3 copies.
# 9. Display books that are unavailable.
# 10. Find the most available book.
# 11. Generate a restocking report.
# 12. Create a separate dictionary of books requiring immediate purchase.

#empty dictionary to store book records
library = {}

#input of number of books
n=int(input("enter number of books"))

#validating number of books
if n<=0:
    print("invalid number of books")
    exit()

elif n<30:
    print("minimum 30 books required")
    exit()

else:
  
  #input of book records
  for i in range(1,n+1):

    #book_id
    book_id=input("enter book id")

    #check if book id already exists
    if book_id in library:
        print("book id already exists")
        continue

    #check if book id is alphanumeric
    elif not book_id.isalnum():
        print("invalid book id")
        continue

    #book_title
    book_title=input("enter book title")

    #check if book title is alphabetic
    if not book_title.replace(" ","").isalpha():
        print("invalid book title")
        continue

    #book_author
    book_author=input("enter book author")

    #check if book author is alphabetic
    if not book_author.replace(" ","").isalpha():
        print("invalid book author")
        continue

    #book_copies
    book_copies=int(input("enter book copies"))

    #validating book copies
    if book_copies<0:
        print("invalid book copies")
        continue


   #creating book dictionary structure
    library[book_id] = {
        "title": book_title,
        "author": book_author,
        "copies": book_copies
    }

    


# 1. Add a book.
new_book_id=input("enter book id")

#check if book id is alphanumeric
if not new_book_id.isalnum():
    print("invalid book id")
    exit()

#check if book id already exists
elif new_book_id in library:
    print("book id already exists")
    exit()

else:
    new_book_title=input("enter book title")

    #check if book title is alphabetic
    if not new_book_title.replace(" ","").isalpha():
        print("invalid book title")
        exit()

    new_book_author=input("enter book author")

    #check if book author is alphabetic
    if not new_book_author.replace(" ","").isalpha():
        print("invalid book author")
        exit()

    new_book_copies=int(input("enter book copies"))

    #validating book copies
    if new_book_copies<0:
        print("invalid book copies")
        exit()

    library[new_book_id] = {
        "title": new_book_title,
        "author": new_book_author,
        "copies": new_book_copies
    }



# 2. Remove a book.
remove_book_id=input("enter book id")

#check if book id is alphanumeric
if not remove_book_id.isalnum():
    print("invalid book id")
    exit()

#check if book id exists
elif remove_book_id not in library:
    print("book id does not exist")
    exit()

else:
    del library[remove_book_id]

    print("book removed successfully")


# 3. Search a book by ID.

search_book_id=input("enter book id")

#check if book id is alphanumeric
if not search_book_id.isalnum():
    print("invalid book id")
    exit()

#check if book id exists
elif search_book_id not in library:
    print("book id does not exist")
    exit()

else:
   print("book found")
   print(library[search_book_id])


# 4. Search by title.
search_title=input("enter book title")

#check if book title is alphabetic
if not search_title.replace(" ","").isalpha():
    print("invalid book title")
    exit()

else:
    #for checking book title is exists or not
    found = False

    for book_id,details in library.items():
        if details["title"].lower() == search_title.lower():
            found = True
        
          
            print("book found")
            print(f"Book ID: {book_id} ")
            print(f"Title: {details['title']} ")
            print(f"Author: {details['author']} ")
            print(f"Copies: {details['copies']} ")
            break
            
    if not found:
        print("book not found")
        
    

# 5. Update available copies.
upadte_book_id=input("enter book id")

#check if book id is alphanumeric
if not upadte_book_id.isalnum():
    print("invalid book id")
    exit()

#check if book id exists
elif upadte_book_id not in library:
    print("book id does not exist")
    exit()

else:
    update_book_copies=int(input("enter book copies"))

    #validating book copies
    if update_book_copies<0:
        print("invalid book copies")
        exit()

    else:    
        library[upadte_book_id]["copies"] = update_book_copies
        print("book copies updated successfully")

    


# 6. Issue a book.

issue_book_id=input("enter book id")

#check if book id is alphanumeric
if not issue_book_id.isalnum():
    print("invalid book id")
    exit()

#check if book id exists
elif issue_book_id not in library:
    print("book id does not exist")
    exit()

else:
    #check if book is available
    if library[issue_book_id]["copies"] == 0:
        print("book is not available")
        exit()
    
    else:
      
      #issue book
      library[issue_book_id]["copies"] -= 1
      print("book issued successfully")

# 7. Return a book.

return_book_id=input("enter book id")

#check if book id is alphanumeric
if not return_book_id.isalnum():
    print("invalid book id")
    exit()

#check if book id exists
elif return_book_id not in library:
    print("book id does not exist")
    exit()

else:

    #return book
    library[return_book_id]["copies"] += 1
    print("book returned successfully") 


# 8. Display books with fewer than 3 copies.

for book_id,details in library.items():
    if details["copies"] < 3:
        print(f"Book ID: {book_id} ")
        print(f"Title: {details['title']} ")
        print(f"Author: {details['author']} ")
        print(f"Copies: {details['copies']} ")
        print("-----"*3)


# 9. Display books that are unavailable.

for book_id,details in library.items():
    if details["copies"] == 0:
        print(f"Book ID: {book_id} ")
        print(f"Title: {details['title']} ")
        print(f"Author: {details['author']} ")
        print(f"Copies: {details['copies']} ")
        print("-----"*3)


# 10. Find the most available book. 

#check if library is empty
if len(library) == 0:
    print("no books available")
    exit()

#find most available book
max_copies_id=(list(library.keys()))[0]
for book_id,details in library.items():
    if details["copies"] > library[max_copies_id]["copies"]:
        max_copies_id=book_id
       

print(f"Book ID: {max_copies_id} ")
print(f"Title: {library[max_copies_id]['title']} ")
print(f"Author: {library[max_copies_id]['author']} ")
print(f"Copies: {library[max_copies_id]['copies']} ")
print("-----"*3)


# 11. Generate a restocking report.

for book_id,details in library.items():
    if details["copies"] < 3:
        print(f"Book ID: {book_id} ")
        print(f"Title: {details['title']} ")
        print(f"Author: {details['author']} ")
        print(f"Copies: {details['copies']} ")
        print("-----"*3)


# 12. Create a separate dictionary of books requiring immediate purchase.

immediate_purchase={}

for book_id,details in library.items():
    if details["copies"] == 0:
        immediate_purchase[book_id]={
            "title":details["title"],
            "author":details["author"],
            "copies":details["copies"]
        }

print("Books requiring immediate purchase:")


#display books requiring immediate purchase
for book_id,details in immediate_purchase.items():
    print(f"Book ID: {book_id} ")
    print(f"Title: {details['title']} ")
    print(f"Author: {details['author']} ")
    print(f"Copies: {details['copies']} ")
    print("-----"*3)