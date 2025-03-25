book_list = list()

#menu items
menu = """
1) Add book
2) Remove book
3) View book
4) Press E to Exit
"""
#add books
def add_book(booklist, book):
    booklist.append(book)
    print("Book added successfully")
#remove books
    def remove_book(booklist, book):
       if book in booklist:
              booklist.remove(book)
              print("Book removed successfully")
       else:
                print("Book not found in this list")

    #display all books results
    def display_list(booklist):
          if booklist:
                print("Added Books ->", ", ".join(booklist))
          else: 
                print("No books added yet")                


    #exit program
    def exit_program():
            print("Thank you for visiting the book library system")
            exit() 



    #main program loop
    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == "1":
            book_name = input("Enter the book name you want to add: ")
            add_book(book_list, book_name)
        elif choice == "2":
            book_name = input("Enter the book name to remove: ")
            remove_book(book_list, book_name)
        elif choice == "3":
            display_list(book_list)
        elif choice.lower == "e":
            exit_program()
        else:
            print("Invalid entry")
            input("press enter to return the main menu!")        


