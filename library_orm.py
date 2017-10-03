from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Add code to create a database engine that stores data in the local directory's library.db
engine = create_engine('sqlite:///library.db')
Base=declarative_base()

# Here we define columns for the table BOOK
# Notice that each column is also a normal Python instance attribute.
# Add columns: id (INT primary key) as INT
#              title, author, year, genre as TEXT
# Note, columns title and author cannot be NULL
class Book(Base):   
    # Student Task: Complete the defintion of the class BOOK
    __tablename__ = 'BOOK'    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    year = Column(String(250))
    genre = Column(String(250))

class Library(object):
    # Student Task: Complete the code to create all tables in the database.
    def create_table(self):
        try:
            Base.metadata.create_all(engine)
        except:
            print("Table already there.")

    def insert_book(self, id,title, author, year, genre):
        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        # Create a DBsession() instance to establish all conversations with the database
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Student Task: Provide code to insert books into the table BOOK
        #Insert records to the Person and Addresses table
        
        new_book = Book(id=id,title=title, author=author, year=year, genre=genre)
        session.add(new_book)        
        session.commit()

    def search_book(self,title):
        print("\nSearch for book: " + title + "...")
        
        # Student Task:
        # Add the code to bind the engine to the metadata of the Base Class and
        # create a new DBSession().  Refer to the example in insert_book() method

        # Student Task: Build a query to search a book by Title
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        books = session.query(Book).filter(Book.title.contains(title)).all()
        for book in books:
            print(book.title)
        session.close()

    def search_author(self,author):
        print("\nSearch for author: " + author + "...")

        # Student Task:
        # Add the code to bind the engine to the metadata of the Base Class and
        # create a new DBSession().  Refer to the example in insert_book() method

        # Student Task: Build a query to search a book by Author
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        books = session.query(Book).filter(Book.author==author).all()
        for book in books:
            print(book.title)
        session.close()
        
                
#Create a new instance of library
library = Library()
#Create the tables in the databse
library.create_table()

#Insert records into the table
library.insert_book('001', 'Agile Design', 'Tom', '1997', 'textbook')
library.insert_book('002', 'Cooking', 'Jack', '1998', 'cookbook')
library.insert_book('003', 'Solid Principle', 'Tom', '2002', 'cookbook')
library.insert_book('004', 'Agile Principle', 'Tom', '2002', 'cookbook')

#Search the tables in the database
library.search_book('Agile')
library.search_author('Tom')
