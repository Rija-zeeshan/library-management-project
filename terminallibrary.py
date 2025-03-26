# Book list
book_list = list()

# Menu options
menu = """
1) Add book
2) Remove book
3) View books
4) Press E to Exit
"""

# Add book
def add_book(booklist, book):
    booklist.append(book)
    print("📚 Book added successfully!")

# Remove book
def remove_book(booklist, book):
    if book in booklist:
        booklist.remove(book)
        print("❌ Book removed successfully!")
    else:
        print("⚠️ Book not found in the list.")

# Display all books
def display_list(booklist):
    if booklist:
        print("📖 Added Books:", ", ".join(booklist))
    else:
        print("📭 No books added yet.")

# Exit program
def exit_program():
    print("🙏 Thank you for using the book library system!")
    exit()

# Main loop
while True:
    print(menu)
    choice = input("Enter your choice: ")

    if choice == "1":
        book_name = input("📌 Enter the book name you want to add: ")
        add_book(book_list, book_name)
    elif choice == "2":
        book_name = input("🗑️ Enter the book name to remove: ")
        remove_book(book_list, book_name)
    elif choice == "3":
        display_list(book_list)
    elif choice.lower() == "e":  # ✅ Fixed: .lower() method issue
        exit_program()
    else:
        print("⚠️ Invalid entry! Please choose a valid option.")
        input("🔄 Press Enter to return to the main menu!")
1
