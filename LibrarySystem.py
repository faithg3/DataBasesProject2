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
    checkout_btn = Button(checkOutBookFrame, text ='Checkout Book ')
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
    getLibCard_btn = Button(getLibraryCardFrame, text ='Get Library Card ')
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
    getLibCard_btn = Button(addNewBookFrame, text ='Add Book ')
    getLibCard_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


#                                      CHECK BOOK AVALIABLITY FRAME INTERFACE
def CheckBookAvaliabilityInterface():
    info = Label(checkBookAvaliabilityFrame, text='Enter the Book Title to see its avaliability!')
    info.grid(row=0, column=1, pady=20)

    title = Entry(checkBookAvaliabilityFrame, width = 30)
    title.grid(row = 1, column = 1, padx = 20)
    title_label = Label(checkBookAvaliabilityFrame, text = 'Book Title: ')
    title_label.grid(row =1, column = 0)

    getLibCard_btn = Button(checkBookAvaliabilityFrame, text ='Check Avaliability ')
    getLibCard_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


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

    getLibCard_btn = Button(checkLateBooksFrame, text ='View Late Books ')
    getLibCard_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

#                                           LIST BORROWER FRAME INTERFACE
#def listBorrowerInterface():


#                                             LIST BOOK FRAME INTERFACE
#def listBookInterface():


#######################################################################################################################





#######################################################################################################################
#                                                  BUTTON FUNCTIONS
#######################################################################################################################



# button function here



#######################################################################################################################





#######################################################################################################################
#                                                        MAIN
#######################################################################################################################
# create tkinter window
root = Tk()
root.title('LibrarySystem')
root.geometry("700x500")

library_system_connect = sqlite3.connect('librarysystem.db')
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
#listBorrowerInterface()
#listBookInterface()





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