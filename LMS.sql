-- Create LMS SQLite database file
.open LMS.sqlite


-- Create tables for database
CREATE TABLE PUBLISHER (
	Publisher_Name VARCHAR(40) NOT NULL,
	Phone INTEGER NOT NULL,
	Address VARCHAR(70) NOT NULL,
	PRIMARY KEY (Publisher_Name)
);

CREATE TABLE LIBRARY_BRANCH (
	Branch_Id INTEGER NOT NULL,
	Branch_Name VARCHAR(15) NOT NULL,
	Branch_Address VARCHAR(70) NOT NULL,
	PRIMARY KEY (Branch_Id)
);

CREATE TABLE BORROWER (
	Card_No INTEGER NOT NULL,
	Name VARCHAR(25) NOT NULL,
	Address VARCHAR(70) NOT NULL,
	Phone CHAR(12) NOT NULL,
	PRIMARY KEY (Card_No)
);

CREATE TABLE BOOK (
	Book_Id INTEGER NOT NULL,
    Title VARCHAR(70) NOT NULL,
	Publisher_Name VARCHAR(40) NOT NULL,
	PRIMARY KEY(Book_Id),
	FOREIGN KEY (Publisher_Name) REFERENCES PUBLISHER(Publisher_Name)
);

CREATE TABLE BOOK_LOANS(
    Book_Id INTEGER NOT NULL,
	Branch_Id INTEGER NOT NULL,
	Card_No INTEGER NOT NULL,
	Date_Out DATE,
	Due_Date DATE,
	Returned_Date DATE,
	PRIMARY KEY (Book_Id, Branch_Id, Card_No),
	FOREIGN KEY(Book_Id) REFERENCES BOOK(Book_Id),
	FOREIGN KEY(Branch_Id) REFERENCES LIBRARY_BRANCH(Branch_Id),
	FOREIGN KEY(Card_No) REFERENCES BORROWER(Card_No)
);

CREATE TABLE BOOK_COPIES(
	Book_Id INTEGER NOT NULL,
	Branch_Id INTEGER NOT NULL,
	No_Of_Copies INTEGER NOT NULL,
	PRIMARY KEY (Book_Id, Branch_Id),
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id),
    FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id)
);

CREATE TABLE BOOK_AUTHORS(
    Book_Id INTEGER NOT NULL,
    Author_Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (Book_Id, Author_Name),
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id)
);


-- Import data from csv files
.mode csv
.import Publisher.csv PUBLISHER
.import Library_Branch.csv LIBRARY_BRANCH
.import Borrower.csv BORROWER
.import Book.csv BOOK
.import Book_Loans.csv BOOK_LOANS
.import Book_Copies.csv BOOK_COPIES
.import Book_Authors.csv BOOK_AUTHORS

-- Delete table headers from database
DELETE FROM PUBLISHER WHERE rowid=1;
DELETE FROM BOOK_LOANS WHERE rowid=1;
DELETE FROM BOOK_COPIES WHERE rowid=1;
DELETE FROM BOOK_AUTHORS WHERE rowid=1;


-- Improve readability
.mode columns
.headers on