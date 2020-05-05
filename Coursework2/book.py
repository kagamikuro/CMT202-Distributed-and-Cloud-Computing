#define a book class
class Book(object):
    def __init__(self, author = None, title = None, ISBN = None, year= None):
        self.ID = -1
        self.author = author
        self.ISBN = ISBN
        self.title = title
        self.year = year
        self.status = False
        self.numberOfTimes = 0

    def getID(self):
        return self.ID

    def setID(self,ID):
        self.ID = ID 

    def getAuthor(self):
        return self.author
    
    def setAuthor(self, Author):
        self.author = Author

    def getISBN(self):
        return self.ISBN  

    def setISBN(self,ISBN):
        self.ISBN = ISBN
    
    def getTitle(self):
        return self.title
    
    def setTitle(self, Title):
        self.title = Title

    def getYear(self):
        return self.year
    
    def setYear(self, Year):
        self.year = Year

    def getStatus(self):
        return self.status
    
    def setStatus(self, Status):
        self.status = Status

    def getNumberOfTimes(self):
        return self.numberOfTimes

    def setNumberOfTimes(self, NumberOfTimes):
        self.numberOfTimes = NumberOfTimes
        
    def __repr__(self):
        return "Book{" + "ID=" + str(self.ID) +",Author=" + self.author +  ",ISBN=" + self.ISBN +  ",Title=" + self.title +  ",Year=" + str(self.year) + ",Status=" + str(self.status) + ",Number of times the book has been loaned=" + str(self.numberOfTimes) +"}"
