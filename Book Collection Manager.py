import json

# Load existing books or create empty list
try:
    with open("books.json", "r") as f:
        books = json.load(f)
except FileNotFoundError:
    books = []

while True:
    print("\n--- Book Collection Manager ---")
    print("1. Add a book")
    print("2. View books")
    print("3. Remove a book")
    print("4. Stats")
    print("5. Search books")
    print("6. Sort books")
    print("7. Export books")
    print("8. Import books")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":  # Add
        title = input("Enter book title: ")
        pages_input = input("Enter number of pages: ")

        if pages_input.replace(".", "", 1).isdigit():
            pages = float(pages_input)
            if pages <= 0:
                print("Pages must be greater than 0.")
            else:
                books.append({"title": title, "pages": pages})
                print(f"{title} added with {pages} pages.")
                with open("books.json", "w") as f:
                    json.dump(books, f, indent=4)
        else:
            print("Pages must be a number.")

    elif choice == "2":  # View
        if not books:
            print("No books to view.")
        else:
            print("Your books:")
            for number, book in enumerate(books, start=1):
                print(f"{number}. {book['title']} with {book['pages']} pages.")

    elif choice == "3":  # Remove
        if not books:
            print("No books to remove.")
        else:
            print("Your books:")
            for number, book in enumerate(books, start=1):
                print(f"{number}. {book['title']} with {book['pages']} pages.")
            try:
                remove_index = int(input("Which book do you want to remove? "))
                if 1 <= remove_index <= len(books):
                    removed_book = books.pop(remove_index - 1)
                    print(f"{removed_book['title']} has been removed.")
                    with open("books.json", "w") as f:
                        json.dump(books, f, indent=4)
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":  # Stats
        if not books:
            print("No books to calculate stats.")
        else:
            total_books = len(books)
            total_pages = sum(book["pages"] for book in books)
            avg_pages = total_pages / total_books
            print(f"You have {total_books} book(s) with {total_pages} pages in total.")
            print(f"Average pages per book: {avg_pages:.1f}")

    elif choice == "5":  # Search
        keyword = input("Enter keyword to search: ").lower()
        found = [book for book in books if keyword in book["title"].lower()]
        if found:
            print("Books found:")
            for number, book in enumerate(found, start=1):
                print(f"{number}. {book['title']} with {book['pages']} pages.")
        else:
            print("No matching books found.")

    elif choice == "6":  # Sort
        if not books:
            print("No books to sort.")
        else:
            print("Sort by pages:")
            print("1. Ascending (lowest → highest)")
            print("2. Descending (highest → lowest)")
            try:
                sort_choice = int(input("Enter your choice (1 or 2): "))
                if sort_choice == 1:
                    sorted_books = sorted(books, key=lambda b: b["pages"])
                elif sort_choice == 2:
                    sorted_books = sorted(books, key=lambda b: b["pages"], reverse=True)
                else:
                    print("Invalid choice.")
                    continue

                print("\nSorted books:")
                for number, book in enumerate(sorted_books, start=1):
                    print(f"{number}. {book['title']} - {book['pages']} pages")
            except ValueError:
                print("Please enter 1 or 2.")

    elif choice == "7":  # Export
        if not books:
            print("No books to export.")
        else:
            filename = input("Enter filename to export (e.g. backup.json): ")
            with open(filename, "w") as f:
                json.dump(books, f, indent=4)
            print(f"Books exported to {filename} successfully!")

    elif choice == "8":  # Import
        filename = input("Enter filename to import (e.g. backup.json): ")
        try:
            with open(filename, "r") as f:
                imported_books = json.load(f)
                books.extend(imported_books)
            print(f"Books imported from {filename} successfully!")
        except FileNotFoundError:
            print("File not found! Please check the name and try again.")
        except json.JSONDecodeError:
            print("File is not a valid JSON!")

    elif choice == "9":  # Exit
        print("Exiting Book Manager. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
