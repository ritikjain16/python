class Library():
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    
    def displayAllBooks(self):
        print("\nList of books is : ")
        for books in self.books:
            print(f" * {books}")
    
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} book. Please keep it safe.")
            self.books.remove(bookname)
        else:
            print("Sorry book is not available in the library or someone had already issued book.")
    
    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book. Hope you enjoyed it.")
        
          
            

class Student():
    def requestBook(self):
        self.book=input("Enter the name of the book you want to borrow : ")
        return self.book
    
    def returnBook(self):
        self.book=input("Enter the name of the book you want to return or add in library : ")
        return self.book

if __name__ == "__main__":
 lib=Library(["Python","Java","C#","Kotlin","HTML/CSS","Javascript"])
 stu=Student()

 while(True):
     print('''\n***** Welcome to Central Library *****
     1. List of books
     2. Borrow a book
     3. Add/Return a book
     4. Exit
     ''')
     a=int(input("Enter your choice : "))
     if a==1:
         lib.displayAllBooks()
     elif a==2:
         lib.borrowBook(stu.requestBook())
     elif a==3:
         lib.returnBook(stu.returnBook())
     elif a==4:
         print("Thanks for using this Library!")
         exit()
     else:
         print("Invalid Choice")
    

     
 