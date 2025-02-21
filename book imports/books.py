def main():
    books = []  
    while True:
        title = input("Enter book title or 'done' if there are none left. ")  
        if title.lower() == 'done':
            break
        try:
            pages = int(input(f"Enter the total number of pages for '{title}'. "))  
            books.append((title, pages))
        except ValueError:
            print("Please enter a valid number of pages. ") 
    return books  
