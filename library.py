import datetime

class library:

  def __init__(self, bookList):
    self.bookList = bookList

  # Method too add books to the library
  def addBookToLibrary(self, name, IBSN, price):
    self.bookList.append(Book(name, IBSN, price))


  # Method for telling the number of books in library with the same Name
  def countBookCopies(self, bookName):
    count = 0
    for book in self.bookList:
      if bookName == book.name:
        count += 1
    return count

  # Display the name of the books that repead only once
  def sortBooks(self):
    setSortedBookList = set()
    for book in self.bookList:
      setSortedBookList.add(book.name)
    return setSortedBookList

  # Display available book titles and the amount stored in library
  def showAvailableBooks(self):
    print("Available books in the library at the moment:")
    print("==============================================")
    for book in self.sortBooks():
      if self.countBookCopies(book) == 1:
        plural = ""
        print(f'"{book}" {self.countBookCopies(book)} book{plural}')
      else:
        plural = "s"
        print(f'"{book}" {self.countBookCopies(book)} book{plural}')

# Class Book for defining book object that is stored in library
class Book:
  def __init__(self, name, IBSN, price):
    self.name = name
    self.IBSN = IBSN
    self.price = price
  
class Person:
  def borrowBook(self):
    self.book=input("What's the name of the book you want to borrow: ")
    return self.book
    

  def returnBook(self):
    self.book=input("What's the name of the book you want to return: ")
    return self.book
    
def main():
  person = Person()

  book1 = Book("Atomic Habits", 123, 50)
  book2 = Book("Deep Work", 132, 70)
  book3 = Book("Can't hurt me", 213, 100)
  book4 = Book("Atomic Habits", 124, 50)


  myLibrary = library([book1, book2, book3, book4])

  # Test showAvailableBooks method
  # It also lists the amount of copies for every book title
  myLibrary.showAvailableBooks()

  # Test addBookToLibrary method
  myLibrary.addBookToLibrary("Deep Work", 144, 70)

  # Test if the Books was added
  myLibrary.showAvailableBooks()

main()
