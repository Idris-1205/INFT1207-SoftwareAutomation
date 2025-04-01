"""
Lab2_AidressQadeer.py
Group: Lab2_Group19

Authors: Aidress Qadeer
Date: 2025-03-27
Description: 
This program manages a user's reading list. Users can add books by entering the title, 
author, and publication year, list all books stored in the CSV file, and search for a specific book.
All book data is stored in the CSV file "books.csv".
"""

import csv
import os

CSV_FILE = 'books.csv'

def add_book():
    """Adds a new book entry to the CSV file."""
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    year = input("Enter the year of publication: ")

    # Append the new book to the CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])
    print("Book added successfully.\n")

def list_books():
    """Reads and displays all book entries from the CSV file."""
    if not os.path.exists(CSV_FILE):
        print("No books found. The CSV file does not exist.\n")
        return
    
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        books = list(reader)
        
        if not books:
            print("No books found in the reading list.\n")
            return

        print("\n=== Reading List ===")
        # Print header row if available
        print("{:<30} {:<25} {:<5}".format("Title", "Author", "Year"))
        print("-" * 65)
        for row in books:
            if len(row) == 3:
                print("{:<30} {:<25} {:<5}".format(row[0], row[1], row[2]))
        print()

def search_book():
    """Searches for a book by title in the CSV file."""
    if not os.path.exists(CSV_FILE):
        print("No books found. The CSV file does not exist.\n")
        return
    
    search_title = input("Enter the book title to search: ").lower()
    found = False
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        books = list(reader)
        print("\n=== Search Results ===")
        for row in books:
            if search_title in row[0].lower():
                print("{:<30} {:<25} {:<5}".format(row[0], row[1], row[2]))
                found = True
        if not found:
            print("Book not found.")
        print()

def display_menu():
    """Displays the main menu."""
    print("=== Reading List Application ===")
    print("1. Add Book")
    print("2. List All Books")
    print("3. Search for a Book")
    print("4. Quit")

def main():
    """Main function to run the application menu loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
