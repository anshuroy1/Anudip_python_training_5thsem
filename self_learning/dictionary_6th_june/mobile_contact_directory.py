# • Display all contact names in alphabetical order.
# • Count the total number of contacts.
# • Search for a given contact name.
# • Create a list of contacts whose names start with a vowel.
# • Stop the search using break once the required contact is found.

# Mobile Contact Directory

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display names in alphabetical order
print("Contacts in Alphabetical Order:")

for name in sorted(contacts.keys()):
    print(name)

# Total contacts
print("\nTotal Contacts:", len(contacts))

# Search contact
search_name = input("\nEnter Contact Name: ")

found = False

for name, number in contacts.items():

    if name == search_name:
        print("Number:", number)
        found = True
        break

if found == False:
    print("Contact Not Found")

# Names starting with vowels
vowel_names = []

for name in contacts.keys():

    if name[0] in "AEIOUaeiou":
        vowel_names.append(name)

print("\nNames Starting With Vowel:")
print(vowel_names)