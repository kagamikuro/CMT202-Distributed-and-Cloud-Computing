import Pyro4
from book import Book

@Pyro4.expose
class Library(object):

    def __init__(self):
        #a list to store book data
        self.bookList = []     
    
    #return all seven pieces of information relating to the set of books currently stored.
    def return_books(self):
        print("return_books called")
        results = ""
        for book in self.bookList:
            results = results + book.__repr__() + "\n"
        message = "all books information:\n"
        return message+results
 
    #add a book to the set of books currently stored
    #return book unique ID and its title
    def add_book(self, author, title, ISBN, year):
        print("add_book called")

        book = Book(author,title,ISBN,year)
        id = len(self.bookList)+1
        book.setID(id)
        self.bookList.append(book)
        
        return "book "+title+"(id = "+str(id)+") has been added successfully\n"
    
    #return all information relating to the subset of books currently stored which have a publication date within a specified inclusive year range
    def select_by_year(self, start_year, end_year):
        print("select_by_year called")        
        if start_year>end_year:
            return "please input correct year!\n"
        results = ""
        for book in self.bookList:
            year = book.getYear()
            if year>start_year and year<end_year:
                results = results + book.__repr__() + "\n"
        message = "the subset of books information from year "+str(start_year)+" to year "+str(end_year)+":\n"
        return message+results     

    #set the status of all books with a specified title to on loan
    #return success message if the book has been set on loan successfully
    def set_on_loan(self, title):
        print("set_on_loan called")
        isExecuted = False
        for book in self.bookList:
            if book.getTitle() == title:
                if book.getStatus() == True:
                    return "book "+title+" had already been set on loan!!\n"
                book.setStatus(True)
                book.setNumberOfTimes(book.getNumberOfTimes()+1)
                isExecuted = True

        if isExecuted:
            return "book "+title+" has been set on loan successfully\n" 
        else:
            return "book "+title+" not found\n" 
    
    #set the status of all books with a specified title to not on loan
    #return success message if the book has been set not on loan successfully
    def set_not_loan(self, title):
        print("set_not_loan called")
        isExecuted = False
        for book in self.bookList:
            if book.getTitle() == title:
                if book.getStatus() == False:
                    return "book "+title+" had already been set not on loan!!\n"
                book.setStatus(False)
                isExecuted = True

        if isExecuted:
            return "book "+title+" has been set not on loan successfully\n" 
        else:
            return "book "+title+" not found\n" 
        
    #return all information relating to the set of books currently stored sorted in descending order by year of publication
    def return_books_sorted(self):
        print("return_books_sorted called")
        booksTupleList = []
        
        for book in self.bookList:
            booksTupleList.append((book.getYear(), book))

        sortedBooks = sorted(booksTupleList,key=lambda item:item[0], reverse = True)

        results = ""
        for item in sortedBooks:
            book = item[1]
            results = results + book.__repr__() + "\n"
        message = "all books information relating to descending order by year:\n"
        return message+results
        
    #return all information relating to the subset of books currently stored where the corresponding ISBN contains a specified Integer value
    def return_books_ISBN(self, intValue):
        print("return_books_ISBN called")
        results = ""
        for book in self.bookList:
            isbn = book.getISBN()
            values = isbn.split('-')
            for value in values:
                if int(value) == intValue:
                    results = results + book.__repr__() + "\n"
        message = "all book information relating to ISBN contains a specified Integer:"+str(intValue)+"\n"
        return message+results   
            

        
def main():
    
    library = Library()
    #start a Pyro daemon server for the library object
    Pyro4.Daemon.serveSimple(
        {
            library: "Coursework2.library"
        },
        ns=True)


if __name__ == "__main__":
    main()
