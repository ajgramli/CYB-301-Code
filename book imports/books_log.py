import books  

book_list = books.main() #creates the book list to be evaluated

#Display books  
print("\nBooks Read:") 
for title, pages in book_list: 
    print(f"{title} - {pages} pages") #produces the title and pages for each book and page count entered  

#Calculate and display average pages 
if book_list: 
    avg_pages = sum(pages for title, pages in book_list) / len(book_list) #gets the average number of pages read per book 
    print(f"\nAverage pages per book: {avg_pages:.0f}")
else:
    print("\nNo books entered. ") 
