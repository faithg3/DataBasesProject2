from tkinter import *
from tkinter import ttk
import sqlite3

#######################################################################################################################
#                                                FRAME INTERFACES
#######################################################################################################################

#                                          CHECK OUT BOOK FRAME INTERFACE
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


#                                 GET LIBRARY CARD FRAME INTERFACE  (ADD NEW BORROWER)
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


#                                          ADD NEW BOOK FRAME INTERFACE
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

    # create buttons
    addNewBook_btn = Button(addNewBookFrame, text ='Add Book ')
    addNewBook_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



#                                      CHECK BOOK AVALIABLITY FRAME INTERFACE
def CheckBookAvaliabilityInterface():
    info = Label(checkBookAvaliabilityFrame, text='Enter the Book Title to see its avaliability!')
    info.grid(row=0, column=1, pady=20)

    title = Entry(checkBookAvaliabilityFrame, width = 30)
    title.grid(row = 1, column = 1, padx = 20)
    title_label = Label(checkBookAvaliabilityFrame, text = 'Book Title: ')
    title_label.grid(row =1, column = 0)

    checkBookAvailablity_btn = Button(checkBookAvaliabilityFrame, text ='Check Avaliability ',  command=lambda:copies_loaned_out_query(title.get()))
    checkBookAvailablity_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



#                                          CHECK LATE BOOKS FRAME INTERFACE
def CheckLateBooksInterface():
    info = Label(checkLateBooksFrame, text='Enter a date range to see which books were returned late!')
    info.grid(row=0, column=1, pady=20)

    date_start = Entry(checkLateBooksFrame, width = 30)
    date_start.grid(row = 1, column = 1, padx = 20)
    date_start_label = Label(checkLateBooksFrame, text = 'Start Date: ')
    date_start_label.grid(row =1, column = 0)

    date_end = Entry(checkLateBooksFrame, width = 30)
    date_end.grid(row = 2, column = 1, padx = 20)
    date_end_label = Label(checkLateBooksFrame, text = 'Start End: ')
    date_end_label.grid(row =2, column = 0)

    checkLateBooks_btn = Button(checkLateBooksFrame, text ='View Late Books ')
    checkLateBooks_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

#                                           LIST BORROWER FRAME INTERFACE
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
    listBorrowers_btn = Button(listBorrowerFrame, text ='View Borrowers ')
    listBorrowers_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


#                                             LIST BOOK FRAME INTERFACE
def listBookInterface():
    # create text boxes and labels
    infoLabelText = 'Search Book Information!\nEnter the Book ID, Book Title to filter search results.'
    info = Label(listBookFrame, text = infoLabelText)
    info.grid(row = 0, column = 1, pady = 20)

    book_id = Entry(listBookFrame, width = 30)
    book_id.grid(row = 1, column = 1)
    book_id_label = Label(listBookFrame, text = 'Borrower ID: ')
    book_id_label.grid(row =1, column = 0)

    title = Entry(listBookFrame, width = 30)
    title.grid(row = 2, column = 1)
    title_label = Label(listBookFrame, text = 'Book Title: ')
    title_label.grid(row =2, column = 0)

    # create buttons
    listBorrowers_btn = Button(listBookFrame, text ='Search Book Information ')
    listBorrowers_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


#######################################################################################################################





#######################################################################################################################
#                                                  BUTTON FUNCTIONS
#######################################################################################################################

#                                                CHECK OUT BOOK BUTTON
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
    if not valid_copies:
        print_record += str('Not enough copies of Book ID {} available at Branch {}\n'.format(Book_Id.get(), Branch_Id.get()))
    
    else:
        # Check if unique information entered
        sql_check_unique = 'SELECT EXISTS (SELECT 1 FROM Book_Loans WHERE Book_Id=? and Branch_Id=? and Card_No=?);'
        val_check_unique = (Book_Id.get(), Branch_Id.get(), Card_No.get(),)
        bcq_cursor.execute(sql_check_unique, val_check_unique)

        info_exists = bcq_cursor.fetchone()
        info_exists = info_exists[0]

        print('info exists : {}'.format(info_exists))

        # Print message if duplicate information entered
        if info_exists == 1:
            print_record += str('You have already checked out book {} from branch {}\n'.format(Book_Id.get(), Branch_Id.get()))

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

            # Output updates onto interface
            for output_record in output_records:
                print_record += str("Book_ID:      " + str(output_record[0]) + '\n')
                print_record += str("Branch_ID:    " + str(output_record[1]) + '\n')
                print_record += str("No_Of_Copies: " + str(output_record[2]) + '\n')

    # Output updates onto interface
    bcq_label = Label(checkOutBookFrame, text = print_record)
    bcq_label.grid(row = 9, column = 0, columnspan = 2)

    # Message disappears after 5 seconds
    bcq_label.after(5000, bcq_label.destroy)

	#commit changes
    bcq_connect.commit()

	#close the DB connection
    bcq_connect.close()


#                                               NEW LIBRARY CARD BUTTON
def newLibraryCardQuery(Name, Address, Phone):
    # create connection and cursor to the DB
    nlcq_connect = sqlite3.connect('LMS.sqlite')
    nlcq_cursor = nlcq_connect.cursor()

    # Insert Borrower into BORROWER
    sql_insert = "INSERT INTO Borrower(Name, Address, Phone) VALUES (?, ?, ?)"
    val_insert = (Name.get(), Address.get(), Phone.get(),)
    nlcq_cursor.execute(sql_insert, val_insert)

    #commit changes
    nlcq_connect.commit()

    # Get new Card_No from Borrower
    sql_output = "SELECT Card_No FROM Borrower WHERE Name=? AND Address=? AND Phone=?"
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


#                                                                            COPIES LOANED OUT BUTTON
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

    label.after(5000, label.destroy)

    # Close the connection
    conn.close()









#######################################################################################################################





#######################################################################################################################
#                                                        MAIN
#######################################################################################################################
# create tkinter window
root = Tk()
root.title('LibrarySystem')
root.geometry("700x500")

library_system_connect = sqlite3.connect('LMS.sqlite')
library_system_cur = library_system_connect.cursor()

# create notebook
lbdb_notebook = ttk.Notebook(root)
lbdb_notebook.pack(pady=15)

# creating frames
checkOutBookFrame = Frame(lbdb_notebook, width=500, height=500)
getLibraryCardFrame = Frame(lbdb_notebook, width=500)
addNewBookFrame = Frame(lbdb_notebook, width=500, height=500)
checkBookAvaliabilityFrame = Frame(lbdb_notebook, width=500, height=500)
checkLateBooksFrame = Frame(lbdb_notebook, width=500, height=500)
listBorrowerFrame = Frame(lbdb_notebook, width=500, height=500)
listBookFrame = Frame(lbdb_notebook, width=500, height=500)

# packing frames
checkOutBookFrame.pack(fill="both", expand=1)
getLibraryCardFrame.pack(fill="both", expand=1)
addNewBookFrame.pack(fill="both", expand=1)
checkBookAvaliabilityFrame.pack(fill="both", expand=1)
checkLateBooksFrame.pack(fill="both", expand=1)
listBorrowerFrame.pack(fill="both", expand=1)
listBookFrame.pack(fill="both", expand=1)

# adding frames to notebook
lbdb_notebook.add(checkOutBookFrame, text = "Check Out Book")
lbdb_notebook.add(getLibraryCardFrame, text = "Get Library Card")
lbdb_notebook.add(addNewBookFrame, text = "Add New Book")
lbdb_notebook.add(checkBookAvaliabilityFrame, text = "Book Avaliablity")
lbdb_notebook.add(checkLateBooksFrame, text = "Late Book Search")
lbdb_notebook.add(listBorrowerFrame, text = "Borrower Search")
lbdb_notebook.add(listBookFrame, text = "Book Search")

# Frame Interfaces
CheckOutBookInterface()
GetLibraryCardInterface()
AddNewBookInterface()
CheckBookAvaliabilityInterface()
CheckLateBooksInterface()
listBorrowerInterface()
listBookInterface()





# address_book_cur.execute('''CREATE TABLE addresses(
# 							first_name text,
# 							last_name text,
# 							street text,
# 							city text,
# 							state text,
# 							zipcode integer)''')


# def submit():
# 	submit_conn = sqlite3.connect('address_book.db')
#
# 	submit_cur = submit_conn.cursor()
#
# 	submit_cur.execute("INSERT INTO ADDRESSES VALUES (:fname, :lname, :street, :city, :state, :zcode) ",
# 		{
# 			'fname': f_name.get(),
# 			'lname': l_name.get(),
# 			'street': street.get(),
# 			'city': city.get(),
# 			'state': state.get(),
# 			'zcode': zipcode.get()
# 		})
#
# 	#commit changes
#
# 	submit_conn.commit()
# 	#close the DB connection
# 	submit_conn.close()



# def input_query():
#
# 	iq_conn = sqlite3.connect('address_book.db')
#
# 	iq_cur = iq_conn.cursor()
#
# 	iq_cur.execute("SELECT first_name, last_name FROM ADDRESSES WHERE state = ? AND city = ?",
# 						(state.get(), city.get(),))
#
# 	output_records = iq_cur.fetchall()
#
# 	print_record = ''
#
# 	for output_record in output_records:
# 		print_record += str(output_record[0]+ " " + output_record[1]+"\n")
#
# 	iq_label = Label(root, text = print_record)
#
# 	iq_label.grid(row = 9, column = 0, columnspan = 2)
#
# 	#commit changes
#
# 	iq_conn.commit()
# 	#close the DB connection
# 	iq_conn.close()


#building the gui components
	# pack place grid

	# create text boxes

# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)
#
#
# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column = 1)
#
# street= Entry(root, width = 30)
# street.grid(row = 2, column = 1)
#
# city = Entry(root, width = 30)
# city.grid(row = 3, column = 1)
#
# state = Entry(root, width = 30)
# state.grid(row = 4, column = 1)
#
# zipcode= Entry(root, width = 30)
# zipcode.grid(row = 5, column = 1)
#
# 	#create label
#
# f_name_label = Label(root, text = 'First Name: ')
# f_name_label.grid(row =0, column = 0)
#
# l_name_label = Label(root, text = 'Last Name: ')
# l_name_label.grid(row =1, column = 0)
#
# street_label = Label(root, text = 'Street: ')
# street_label.grid(row =2, column = 0)
#
# city_label = Label(root, text = 'City: ')
# city_label.grid(row =3, column = 0)
#
# state_label = Label(root, text = 'State: ')
# state_label.grid(row =4, column = 0)
#
# zcode_label = Label(root, text = 'Zipcode: ')
# zcode_label.grid(row =5, column = 0)
#
#
# submit_btn = Button(root, text ='Add Contact ', command = submit)
# submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)
#
# input_qry_btn = Button(root, text = 'Output Names', command = input_query)
# input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)




#executes tinker components
root.mainloop()


#######################################################################################################################
