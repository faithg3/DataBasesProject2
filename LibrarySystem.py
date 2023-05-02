from tkinter import *
from tkinter import ttk
import sqlite3

#######################################################################################################################
#                                                FRAME INTERFACES
#######################################################################################################################
#                                            0.  HOME FRAME INTERFACE
def homeInterface():
    #create text boxes
    info = Label(homeFrame, text = 'Welcome to Our Library Management System!',font=("Arial", 25))
    info.grid(row = 0, column = 1, pady = 20)

    creators = Label(homeFrame, text = 'Created by: \nMuhammad Muawiz Farooqi \nTahera Fatima\n and Faith Gutierrez', font=("Arial", 15))
    creators.grid(row = 1, column = 1, pady = 20)


#                                        1.  CHECK OUT BOOK FRAME INTERFACE
def CheckOutBookInterface():
    #create text boxes
    info = Label(checkOutBookFrame, text = 'Enter the Book ID, Branch ID, and Library Card to check out a book!')
    info.grid(row = 0, column = 1, pady = 20)

    book_id = Entry(checkOutBookFrame, width = 30)
    book_id.grid(row = 1, column = 1, padx = 20)

    branch_id = Entry(checkOutBookFrame, width = 30)
    branch_id.grid(row = 2, column = 1)

    card_no= Entry(checkOutBookFrame, width = 30)
    card_no.grid(row = 3, column = 1)


    #create labels
    book_id_label = Label(checkOutBookFrame, text = 'Book ID: ')
    book_id_label.grid(row =1, column = 0)

    branch_id_label = Label(checkOutBookFrame, text = 'Branch ID: ')
    branch_id_label.grid(row =2, column = 0)

    card_no_label = Label(checkOutBookFrame, text = 'Card #: ')
    card_no_label.grid(row =3, column = 0)

    # create buttons
    checkout_btn = Button(checkOutBookFrame, text ='Checkout Book ', command=lambda: bookCheckoutQuery(book_id, branch_id, card_no))
    checkout_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


#                                2.  GET LIBRARY CARD FRAME INTERFACE  (ADD NEW BORROWER)
def GetLibraryCardInterface():
    # create text boxes and labels
    info = Label(getLibraryCardFrame, text = 'Enter Name, Address, and Phone # to get a new library card!')
    info.grid(row = 0, column = 1, pady = 20)
    name = Entry(getLibraryCardFrame, width = 30)
    name.grid(row = 1, column = 1)
    name_label = Label(getLibraryCardFrame, text = 'Name: ')
    name_label.grid(row =1, column = 0)

    address = Entry(getLibraryCardFrame, width = 30)
    address.grid(row = 2, column = 1)
    address_label = Label(getLibraryCardFrame, text = 'Address: ')
    address_label.grid(row =2, column = 0)

    phone = Entry(getLibraryCardFrame, width = 30)
    phone.grid(row = 3, column = 1)
    phone_label = Label(getLibraryCardFrame, text = 'Phone #: ')
    phone_label.grid(row =3, column = 0)

    # create buttons
    getLibCard_btn = Button(getLibraryCardFrame, text ='Get Library Card ', command=lambda: newLibraryCardQuery(name, address, phone))
    getLibCard_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


#                                         3.  ADD NEW BOOK FRAME INTERFACE
def AddNewBookInterface():
    info = Label(addNewBookFrame, text='Enter the Book Title and Publisher to add new book to each branch!')
    info.grid(row=0, column=1, pady=20)

    title = Entry(addNewBookFrame, width = 30)
    title.grid(row = 1, column = 1, padx = 20)
    title_label = Label(addNewBookFrame, text = 'Book Title: ')
    title_label.grid(row =1, column = 0)

    publisher = Entry(addNewBookFrame, width = 30)
    publisher.grid(row = 2, column = 1)
    publisher_label = Label(addNewBookFrame, text = 'Publisher: ')
    publisher_label.grid(row =2, column = 0)

    author = Entry(addNewBookFrame, width = 30)
    author.grid(row = 3, column = 1)
    author_label = Label(addNewBookFrame, text = 'Author: ')
    author_label.grid(row =3, column = 0)

    # create buttons
    addNewBook_btn = Button(addNewBookFrame, text ='Add Book ', command=lambda: addNewBookQuery(title.get(), publisher.get(), author.get()))
    addNewBook_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



#                                    4.  CHECK BOOK AVALIABLITY FRAME INTERFACE
def CheckBookAvaliabilityInterface():
    info = Label(checkBookAvaliabilityFrame, text='Enter the Book Title to see its avaliability!')
    info.grid(row=0, column=1, pady=20)

    title = Entry(checkBookAvaliabilityFrame, width = 30)
    title.grid(row = 1, column = 1, padx = 20)
    title_label = Label(checkBookAvaliabilityFrame, text = 'Book Title: ')
    title_label.grid(row =1, column = 0)

    checkBookAvailablity_btn = Button(checkBookAvaliabilityFrame, text ='Check Avaliability ',  command=lambda:copies_loaned_out_query(title.get()))
    checkBookAvailablity_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



#                                       5.   CHECK LATE BOOKS FRAME INTERFACE
def CheckLateBooksInterface():
    info = Label(checkLateBooksFrame, text='Enter a date range to see which books were returned late!')
    info.grid(row=0, column=1, pady=20)

    date_start = Entry(checkLateBooksFrame, width=30)
    date_start.grid(row=1, column=1, padx=20)
    date_start_label = Label(checkLateBooksFrame, text='Start Date: ')
    date_start_label.grid(row=1, column=0)

    date_end = Entry(checkLateBooksFrame, width=30)
    date_end.grid(row=2, column=1, padx=20)
    date_end_label = Label(checkLateBooksFrame, text='End Date: ')
    date_end_label.grid(row=2, column=0)

    results_box = Listbox(checkLateBooksFrame, width=100)
    results_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def show_results():
        results_box.delete(0, END)
        results = lateBooksQuery(date_start.get(), date_end.get())
        for row in results:
            row = str('Book Title: ' + row[0].ljust(40, ' ') + 'Days Late: ' + str(int(row[1])))
            results_box.insert(END, row)

    checkLateBooks_btn = Button(checkLateBooksFrame, text='View Late Books', command=show_results)
    checkLateBooks_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

#                                       6.a. LIST BORROWER FRAME INTERFACE
def listBorrowerInterface():
    # create text boxes and labels
    infoLabelText = 'Search Borrowers\' late fees!\nEnter a borrower\'s ID or name to filter search results.'
    info = Label(listBorrowerFrame, text = infoLabelText)
    info.grid(row = 0, column = 1, pady = 20)

    borrower_id = Entry(listBorrowerFrame, width = 30)
    borrower_id.grid(row = 1, column = 1)
    borrower_id_label = Label(listBorrowerFrame, text = 'Borrower ID: ')
    borrower_id_label.grid(row =1, column = 0)

    name = Entry(listBorrowerFrame, width = 30)
    name.grid(row = 2, column = 1)
    name_label = Label(listBorrowerFrame, text = 'Name: ')
    name_label.grid(row =2, column = 0)

    # create buttons
    listBorrowers_btn = Button(listBorrowerFrame, text ='View Borrowers ', command=lambda:borrowerInfoQuery(borrower_id.get(), name.get()))
    listBorrowers_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


#                                        6.b. LIST BOOK FRAME INTERFACE
def listBookInterface():
    # create text boxes and labels
    infoLabelText = 'Search Book Information!\nEnter the Book ID, Book Title or part of Book Title to filter search results.'
    info = Label(listBookFrame, text=infoLabelText)
    info.grid(row=0, column=1, pady=20)

    book_id = Entry(listBookFrame, width=30)
    book_id.grid(row=1, column=1)
    book_id_label = Label(listBookFrame, text='Book ID:')
    book_id_label.grid(row=1, column=0)

    title = Entry(listBookFrame, width=30)
    title.grid(row=2, column=1)
    title_label = Label(listBookFrame, text='Book Title:')
    title_label.grid(row=2, column=0)

    results_box = Listbox(listBookFrame, width=100)
    results_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def show_results():
        results_box.delete(0, END)
        results = bookInfoQuery(book_id.get(), title.get())
        for row in results:
            results_box.insert(END, f"Book ID: {row[0]}, Title: {row[1]}, Late Fee: {row[2]}, Author Name: {row[3]}, Publisher Name: {row[4]}")

    # create buttons
    listBorrowers_btn = Button(listBookFrame, text='Search Book Information', command=show_results)
    listBorrowers_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=140)


#######################################################################################################################





#######################################################################################################################
#                                                  BUTTON FUNCTIONS
#######################################################################################################################

#                                              1.  CHECK OUT BOOK BUTTON
def bookCheckoutQuery(Book_Id, Branch_Id, Card_No):
    # create connection and cursor to the DB
    bcq_connect = sqlite3.connect('LMS.sqlite')
    bcq_cursor = bcq_connect.cursor()

    # Check if enough copies of book available
    sql_check_copies = 'SELECT IIF(No_of_Copies>0, 1, 0) FROM Book_Copies WHERE Book_Id=? and Branch_Id=?;'
    val_check_copies = (Book_Id.get(), Branch_Id.get(),)
    bcq_cursor.execute(sql_check_copies, val_check_copies)

    valid_copies = bcq_cursor.fetchone()
    print_record = ''

    # Print message if not enough copies available
    if valid_copies is None or valid_copies[0] == 0:
        print_record += str('Not enough copies of Book ID {} available at Branch {}\n'.format(Book_Id.get(), Branch_Id.get()))
    
    else:
        # Check if unique information entered
        sql_check_unique = 'SELECT EXISTS (SELECT 1 FROM Book_Loans WHERE Book_Id=? and Branch_Id=? and Card_No=?);'
        val_check_unique = (Book_Id.get(), Branch_Id.get(), Card_No.get(),)
        bcq_cursor.execute(sql_check_unique, val_check_unique)

        info_exists = bcq_cursor.fetchone()
        info_exists = info_exists[0]

        # Print message if duplicate information entered
        if info_exists == 1:
            print_record += str('You have already checked out a copy of book {} from branch {}\n'.format(Book_Id.get(), Branch_Id.get()))

        # Update DB if unique information entered
        else:
            # Insert book into Book_Loans
            sql_insert = "INSERT INTO Book_Loans(Book_Id, Branch_Id, Card_No, Date_Out) VALUES (?, ?, ?, DATE('now'))"
            val_insert = (Book_Id.get(), Branch_Id.get(), Card_No.get(),)
            bcq_cursor.execute(sql_insert, val_insert)

            # Update Book_Copies with new No_Of_Copies
            sql_update = "UPDATE Book_Copies SET No_Of_Copies = No_Of_Copies - 1 WHERE Book_Id=? AND Branch_Id=?"
            val_update = (Book_Id.get(), Branch_Id.get(),)
            bcq_cursor.execute(sql_update, val_update)

            #commit changes
            bcq_connect.commit()

            # Get updated No_Of_Copies from Book_Copies
            sql_output = "SELECT * FROM Book_Copies WHERE Book_Id=? AND Branch_Id=?"
            val_output = (Book_Id.get(), Branch_Id.get(),)
            bcq_cursor.execute(sql_output, val_output)

            output_records = bcq_cursor.fetchall()

            print_record += str('Checkout successful!\n')

            # Output updates onto interface
            for output_record in output_records:
                print_record += str('There are {} copies of book ID #{} remaining at branch {}.\n'.format(output_record[2], output_record[0], output_record[1]))

    # Output updates onto interface
    bcq_label = Label(checkOutBookFrame, text = print_record)
    bcq_label.grid(row = 9, column = 0, columnspan = 2)

    # Message disappears after 7 seconds
    bcq_label.after(7000, bcq_label.destroy)

	#commit changes
    bcq_connect.commit()

	#close the DB connection
    bcq_connect.close()


#                                          2.  NEW LIBRARY CARD BUTTON
def newLibraryCardQuery(Name, Address, Phone):
    # create connection and cursor to the DB
    nlcq_connect = sqlite3.connect('LMS.sqlite')
    nlcq_cursor = nlcq_connect.cursor()

    # Insert Borrower into BORROWER
    sql_insert = "INSERT INTO Borrower(Name, Address, Phone) VALUES (?, ?, ?);"
    val_insert = (Name.get(), Address.get(), Phone.get(),)
    nlcq_cursor.execute(sql_insert, val_insert)

    #commit changes
    nlcq_connect.commit()

    # Get new Card_No from Borrower
    sql_output = "SELECT Card_No FROM Borrower WHERE Name=? AND Address=? AND Phone=?;"
    val_output = (Name.get(), Address.get(), Phone.get(),)
    nlcq_cursor.execute(sql_output, val_output)

    output_records = nlcq_cursor.fetchall()

    # Output updates onto interface
    print_record = ''

    for output_record in output_records:
        print_record = str("Your new Library Card Number is " + str(output_record[0]) + '!\n')

    nlcq_label = Label(getLibraryCardFrame, text = print_record)
    nlcq_label.grid(row = 9, column = 0, columnspan = 2)

	#commit changes
    nlcq_connect.commit()

	#close the DB connection
    nlcq_connect.close()


#                                            3.  ADD NEW BOOK BUTTON
def addNewBookQuery(title, publisher, author):
    # create connection and cursor to the DB
    nbq_connect = sqlite3.connect('LMS.sqlite')
    nbq_cursor = nbq_connect.cursor()

    # Check if new publisher entered
    sql_check_publisher = "SELECT EXISTS (SELECT 1 FROM PUBLISHER WHERE Publisher_Name=? COLLATE NOCASE);"
    val_check_publisher = (publisher,)
    nbq_cursor.execute(sql_check_publisher, val_check_publisher)

    publisher_exists = nbq_cursor.fetchone()
    publisher_exists = publisher_exists[0]
    print_record = ''

    if publisher_exists == 1:
        # update publisher with correct case
        sql_get_publisher = "SELECT Publisher_Name FROM PUBLISHER WHERE Publisher_Name=? COLLATE NOCASE;"
        val_get_publisher = (publisher,)
        nbq_cursor.execute(sql_get_publisher, val_get_publisher)

        publisher_name = nbq_cursor.fetchone()
        publisher = publisher_name[0]
    
    # Add book information to BOOK
    sql_add_book = "INSERT INTO BOOK(Title, Publisher_Name) VALUES (?, ?);"
    val_add_book = (title, publisher,)
    nbq_cursor.execute(sql_add_book, val_add_book)

    # Get Book ID of new book
    sql_get_book_id = "SELECT Book_Id FROM BOOK WHERE Title=? and Publisher_Name=?;"
    val_get_book_id = (title, publisher,)
    nbq_cursor.execute(sql_get_book_id, val_get_book_id)

    book_id = nbq_cursor.fetchone()
    book_id = book_id[0]

    # Check if book info already added in database
    sql_check_author = "SELECT EXISTS(SELECT 1 FROM Book_Authors WHERE Book_Id=? AND Author_Name=?);"
    val_check_author = (book_id, author,)
    nbq_cursor.execute(sql_check_author, val_check_author)

    author_exists = nbq_cursor.fetchone()
    author_exists = author_exists[0]

    # Print error message if duplicate addition
    if author_exists == 1:
        print_record += str('{} by {} has already been added in the database!\n'.format(title, author))

    # Add data to DB if new information entered
    else:
        print_record += str('Added a new book \"{}\" with ID# = {}!\n'.format(title, book_id))

        # Add Author info to Book_Authors
        sql_add_author = "INSERT INTO Book_Authors VALUES (?, ?);"
        val_add_author = (book_id, author,)
        nbq_cursor.execute(sql_add_author, val_add_author)
        print_record += str('Added {} as an author of \"{}\"!\n'.format(author, title))

        # Add 5 copies of the book into each branch in Book_Copies
        sql_add_copies = "INSERT INTO Book_Copies VALUES (?, 1, 5), (?, 2, 5), (?, 3, 5);"
        val_add_copies = (book_id, book_id, book_id, )
        nbq_cursor.execute(sql_add_copies, val_add_copies)
        print_record += str('Added 5 copies of \"{}\" to each branch!\n'.format(title))

    # Output updates onto interface
    nbq_label = Label(addNewBookFrame, text = print_record)
    nbq_label.grid(row = 9, column = 0, columnspan = 2)

    # Message disappears after 10 seconds
    nbq_label.after(10000, nbq_label.destroy)

	#commit changes
    nbq_connect.commit()

	#close the DB connection
    nbq_connect.close()


#                                            4.  COPIES LOANED OUT BUTTON
def copies_loaned_out_query(book_title):
    conn = sqlite3.connect('LMS.sqlite')
    cur = conn.cursor()

    # Get the book id for the given book title (case insensitive)
    sql_book_id = "SELECT Book_Id FROM BOOK WHERE Title = ? COLLATE NOCASE"
    val_book_id = (book_title,)
    cur.execute(sql_book_id, val_book_id)
    book_id = cur.fetchone()

    print_record = ''

    if book_id is None:
        print_record += str("Book not found in the database\n")

    else:
        book_id = book_id[0]

        # Get the number of copies loaned out per branch
        sql_output = "SELECT Branch_Id, COUNT(*) AS Copies_Loaned_Out FROM BOOK_LOANS WHERE Book_Id = ?"
        val_output = (book_id,)
        cur.execute(sql_output, val_output)

        output_records = cur.fetchall()

        # Print the number of copies loaned out per branch
        print_record += str("Number of copies loaned out per branch for book '{}':\n".format(book_title))
        for output_record in output_records:
            print_record += str("Branch {}: {}\n".format(output_record[0], output_record[1]))

    # Output updates onto interface
    label = Label(checkBookAvaliabilityFrame, text = print_record)
    label.grid(row = 9, column = 0, columnspan = 2)

    # Message disappears after 7 seconds
    label.after(7000, label.destroy)

    # Close the connection
    conn.close()


#                                             5.  LATE BOOKS BUTTON
def lateBooksQuery(date_start, date_end):
    conn = sqlite3.connect('LMS.sqlite')
    c = conn.cursor()

    sql_input_lbq = 'SELECT b.title, julianday(bl.Returned_Date) - julianday(bl.due_date) AS days_late '\
                    'FROM BOOK_LOANS AS bl NATURAL JOIN BOOK AS b WHERE bl.Returned_Date > bl.due_date AND bl.due_date >= ? AND bl.due_date <= ?;'
    val_input_lbq = (date_start, date_end)
    c.execute(sql_input_lbq, val_input_lbq)

    result = c.fetchall()

    conn.close()
    return result


#                                             6.a. BORROWER INFO BUTTON
def borrowerInfoQuery(borrower_id, name):
    # create connection and cursor to the DB
    conn = sqlite3.connect('LMS.sqlite')
    cur = conn.cursor()
    # sql statments
    sql_search_by_id = "SELECT Card_No, Borrower_Name, LateFeeBalance FROM vBookLoanInfo WHERE Card_No = ?;"
    sql_search_by_name = "SELECT Card_No, Borrower_Name, LateFeeBalance FROM vBookLoanInfo WHERE Borrower_Name LIKE ? COLLATE NOCASE ORDER BY LateFeeBalance DESC;"
    sql_search_all = "SELECT Card_No, Borrower_Name, LateFeeBalance FROM vBookLoanInfo ORDER BY LateFeeBalance DESC;"

    print_record = ''
    # display all records if nothing is entered in either text boxes
    if (len(borrower_id) == 0) and (len(name) == 0):
        cur.execute(sql_search_all)
        all_output = cur.fetchone()
        if (all_output is None):
            print_record += str("No Records Found! \n")
        else:
            print_record += str("Displaying all borrower info: \n\n")
            while all_output is not None:
                if (all_output[2] == 0):
                    print_record += str("ID: {}    Name: {}    Late Fee Balance: ${}.00\n".format(all_output[0], all_output[1], all_output[2]))
                else:
                    print_record += str("ID: {}    Name: {}    Late Fee Balance: ${}0\n".format(all_output[0], all_output[1], all_output[2]))
                all_output = cur.fetchone()
    # search by name if something is entered in the name text box and nothing in the borrower_id
    elif (len(borrower_id) == 0) and (len(name) != 0):
        string_name = ("%" + name + "%")
        val_output = (string_name,)
        cur.execute(sql_search_by_name, val_output)
        name_output = cur.fetchone()
        if (name_output is None):
            print_record += str("No Records Found with Name: {}!\n".format(name))
        else:
            print_record += str("Displaying all borrower info containing the name {} \n\n".format(name))
            while name_output is not None:
                if (name_output[2] == 0):
                    print_record += str("ID: {}    Name: {}    Late Fee Balance: ${}.00\n".format(name_output[0], name_output[1], name_output[2]))
                else:
                    print_record += str("ID: {}    Name: {}    Late Fee Balance: ${}0\n".format(name_output[0], name_output[1], name_output[2]))
                name_output = cur.fetchone()
    # search by id if something is in the id text box
    elif((len(borrower_id) != 0) and (len(name) == 0)) or ((len(borrower_id) != 0) and (len(name) != 0)):
        val_output = (borrower_id,)
        cur.execute(sql_search_by_id, val_output)
        id_output = cur.fetchone()
        if (id_output is None):
            print_record += str("No Records Found with ID Number: {}!\n".format(borrower_id))
        else:
            print_record += str("Displaying borrower with ID number: {}\n\n".format(borrower_id))
            if (id_output[2] == 0):
                print_record += str("ID: {}    Name: {}    Late Fee Balance: ${}.00\n".format(id_output[0], id_output[1], id_output[2]))
            else:
                print_record += str("ID: {}    Name: {}    Late Fee Balance: ${}0\n".format(id_output[0], id_output[1], id_output[2]))

    # Output updates onto interface
    label = Label(listBorrowerFrame, text = print_record)
    label.grid(row = 9, column = 0, columnspan = 2)

    # Message disappears after 7 seconds
    label.after(7000, label.destroy)

    # Close the connection
    conn.close()


#                                              6.b.BOOK INFO BUTTON
def bookInfoQuery(book_id, title):
    # get user input
    search_criteria = "%" + title + "%"
    params = (book_id, search_criteria, search_criteria)

    # execute SQL query
    conn = sqlite3.connect('LMS.sqlite')
    c = conn.cursor()
    c.execute("""
        SELECT
    book.book_id AS "Book ID",
    book.title AS "Title",
    CASE
        WHEN book_loans.Returned_Date IS NULL THEN (julianday('now') - julianday(book_loans.due_date)) * 0.25
        ELSE 0
    END AS "Late Fee",
    book_authors.author_name AS "Author Name",
    publisher.publisher_name AS "Publisher Name"
FROM book
LEFT JOIN BOOK_AUTHORS ON book.book_id = BOOK_AUTHORS.book_id
LEFT JOIN book_loans ON book.book_id = book_loans.book_id
LEFT JOIN publisher ON book.publisher_name = publisher.publisher_name
WHERE book.book_id LIKE ? OR book.title LIKE ? OR book.title LIKE ?
ORDER BY "Late Fee" DESC NULLS LAST

    """, params)
    results = c.fetchall()

    # close database connection
    conn.close()

    # format results
    formatted_results = []
    for row in results:
        late_fee = row[2]
        if late_fee is None:
            late_fee = "Non-Applicable"
        else:
            late_fee = "${:.2f}".format(late_fee)
        formatted_results.append((row[0], row[1], late_fee, row[3], row[4]))

    return formatted_results

#######################################################################################################################





#######################################################################################################################
#                                                        MAIN
#######################################################################################################################
# create tkinter window
root = Tk()
root.title('LibrarySystem')
root.geometry("700x600")

library_system_connect = sqlite3.connect('LMS.sqlite')
library_system_cur = library_system_connect.cursor()

# create notebook
lbdb_notebook = ttk.Notebook(root)
lbdb_notebook.pack(pady=15)

# creating frames
homeFrame = Frame(lbdb_notebook, width=500, height=500)
checkOutBookFrame = Frame(lbdb_notebook, width=500, height=500)
getLibraryCardFrame = Frame(lbdb_notebook, width=500)
addNewBookFrame = Frame(lbdb_notebook, width=500, height=500)
checkBookAvaliabilityFrame = Frame(lbdb_notebook, width=500, height=500)
checkLateBooksFrame = Frame(lbdb_notebook, width=500, height=500)
listBorrowerFrame = Frame(lbdb_notebook, width=500, height=500)
listBookFrame = Frame(lbdb_notebook, width=500, height=500)

# packing frames
homeFrame.pack(fill="both", expand=1)
checkOutBookFrame.pack(fill="both", expand=1)
getLibraryCardFrame.pack(fill="both", expand=1)
addNewBookFrame.pack(fill="both", expand=1)
checkBookAvaliabilityFrame.pack(fill="both", expand=1)
checkLateBooksFrame.pack(fill="both", expand=1)
listBorrowerFrame.pack(fill="both", expand=1)
listBookFrame.pack(fill="both", expand=1)

# adding frames to notebook
lbdb_notebook.add(homeFrame, text = "Home")
lbdb_notebook.add(checkOutBookFrame, text = "Check Out Book")
lbdb_notebook.add(getLibraryCardFrame, text = "Get Library Card")
lbdb_notebook.add(addNewBookFrame, text = "Add New Book")
lbdb_notebook.add(checkBookAvaliabilityFrame, text = "Book Avaliablity")
lbdb_notebook.add(checkLateBooksFrame, text = "Late Book Search")
lbdb_notebook.add(listBorrowerFrame, text = "Borrower Search")
lbdb_notebook.add(listBookFrame, text = "Book Search")

# Frame Interfaces
homeInterface()
CheckOutBookInterface()
GetLibraryCardInterface()
AddNewBookInterface()
CheckBookAvaliabilityInterface()
CheckLateBooksInterface()
listBorrowerInterface()
listBookInterface()

#executes tinker components
root.mainloop()


#######################################################################################################################
