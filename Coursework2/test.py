#a simple file for testing all seven tasks
import Pyro4

library = Pyro4.Proxy('PYRONAME:Coursework2.library')


print(library.add_book('Allen Hatcher','Algebraic Topology','978-05210-79-5401',2019))
print(library.add_book('Allen Hatcher','Algebraic Topology','978-05210-79-5401',2019))
print(library.add_book('Allen Hatcher','Algebraic Topology','978-05210-79-5401',2019))

print(library.add_book('George Orwell','1984','978-05210-27-1984',1984))
print(library.add_book('George Orwell','1984','978-05210-27-1984',1984))

print(library.add_book('Roald Dahl','Charlie and the Chocolate Factory','978-0520-18-9685',2021))
print(library.add_book('Roald Dahl','Charlie and the Chocolate Factory','978-0520-18-9685',2021))


print(library.return_books())

print(library.select_by_year(2035, 2020))
print(library.select_by_year(1980, 2020))
print(library.select_by_year(2015, 2020))

print(library.set_on_loan('Algebraic Topology'))
print(library.set_on_loan('Algebraic Topology'))
print(library.set_on_loan('Algebraic Topolog'))

print(library.return_books())

print(library.set_not_loan('Algebraic Topology'))
print(library.set_not_loan('Algebraic Topology'))

print(library.return_books())

print(library.return_books_sorted())

print(library.return_books_ISBN(5401))

print(library.return_books_ISBN(27))
