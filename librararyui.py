from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from management_userda import *

# Function to display information in the table


def view_click():
    infolist = show_data()  # Fetch data from the database
    show_tbl(infolist)  # Display data in the table

# Function to add new information to the database


def add_click():
    name = entry_name.get()  # Get name
    book = entry_book.get()  # Get book name
    price = entry_price.get()  # Get price
    count = entry_count.get()  # Get count
    type_book = var.get()  # Get book type (print or ebook)
    gener = entry_gener.get()  # Get genre
    sum_data = calculation(float(price), float(count))  # Calculate total price
    insert_data(name, book, price, count, type_book, gener,
                sum_data)  # Insert data into the database
    showinfo('save', 'Saved data')  # Show success message
    view_click()  # Update the table
    clear()  # Clear the input fields

# Function to edit existing information in the database


def edit_click():
    name = entry_name.get()  # Get name
    book = entry_book.get()  # Get book name
    price = entry_price.get()  # Get price
    count = entry_count.get()  # Get count
    type_book = var.get()  # Get book type (print or ebook)
    gener = entry_gener.get()  # Get genre
    sum_data = calculation(float(price), float(count))  # Calculate total price
    edit_data(book, price, count, type_book, gener,
              sum_data, name)  # Edit data in the database
    showinfo('edit', 'Edited data')  # Show success message
    view_click()  # Update the table
    clear()  # Clear the input fields

# Function to delete information from the database


def delete_click():
    name = entry_name.get()  # Get name
    if name == '':
        # Show error message if name is empty
        showerror('error', 'Please enter name')
        return
    delete_data(name)  # Delete data from the database
    showinfo('delete', 'Deleted data')  # Show success message
    view_click()  # Update the table
    clear()  # Clear the input fields

# Function to sort data using bubble sort algorithm


def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j][6] > data[j + 1][6]:  # Compare total price
                data[j], data[j + 1] = data[j + 1], data[j]  # Swap data

# Function to sort and display data


def sort_click():
    data = show_data()  # Fetch data from the database
    bubble_sort(data)  # Sort data
    show_tbl(data)  # Display data in the table

# Function to search and display data


def search_click():
    name = entry_name.get()  # Get name
    book = entry_book.get()  # Get book name
    price = entry_price.get()  # Get price
    count = entry_count.get()  # Get count
    type_book = var.get()  # Get book type (print or ebook)
    gener = entry_gener.get()  # Get genre
    sum_data = entry_sum.get()  # Get total price
    # Search data in the database
    infolist = search_data(name, book, price, count,
                           type_book, gener, sum_data)
    show_tbl(infolist)  # Display searched data in the table
    clear()  # Clear the input fields

# Function to clear all data from the database


def clear_all_click():
    for i in show_data():
        delete_data(i[0])  # Delete each data from the database
    showinfo('clear', 'Successfully cleared all data!')  # Show success message
    view_click()  # Update the table

# Function to close the main window


def close_click():
    if askyesno('exit', 'Are you sure?'):  # Confirm exit
        root.destroy()  # Close the main window

# Function to clear the input fields


def clear():
    entry_name.delete(0, END)
    entry_book.delete(0, END)
    entry_price.delete(0, END)
    entry_count.delete(0, END)
    var.set(None)
    entry_gener.delete(0, END)
    entry_sum.delete(0, END)

# Function to select an item from the table and display it in the input fields


def select_item(event):
    selected = table_main.focus()
    value_select = table_main.item(selected)['values']
    clear()  # Clear the input fields
    entry_name.insert(0, value_select[0])
    entry_book.insert(0, value_select[1])
    entry_price.insert(0, value_select[2])
    entry_count.insert(0, value_select[3])
    var.set(value_select[4])
    entry_gener.set(value_select[5])
    entry_sum.insert(0, value_select[6])

# Function to display data in the table


def show_tbl(items):
    table_main.delete(*table_main.get_children())
    for item in items:
        table_main.insert('', END, values=item)

# Function to calculate total price


def calculation(price, count):
    return price * count


# Main window setup
root = Tk()
root.title('Library Management')
root.geometry('1165x503')
var = StringVar()

# Style
style = Style()
style.theme_use('clam')

# Colors
bg_color = '#e6f7ff'
btn_color = '#80d4ff'
btn_hover_color = '#4db8ff'
frame_color = '#b3e0ff'

# Configure root window background color
root.configure(bg=bg_color)

# Frame for form
frame_form = Frame(root, padding=10, style='My.TFrame')
frame_form.grid(row=0, column=0, padx=10, pady=10)

style.configure('TLabel', background=bg_color, font=('Arial', 12))
style.configure('TEntry', padding=5)
style.configure('TCombobox', padding=5)
style.configure('TRadiobutton', background=bg_color, font=('Arial', 12))
style.configure('TButton', font=('Arial', 12), background=btn_color)
style.map('TButton', background=[('active', btn_hover_color)])

# Form labels and entries
lbl_name = Label(frame_form, text='Name')
lbl_name.grid(row=0, column=0, sticky=W, pady=5)
entry_name = Entry(frame_form)
entry_name.grid(row=0, column=1, pady=5)

lbl_book = Label(frame_form, text='Book')
lbl_book.grid(row=1, column=0, sticky=W, pady=5)
entry_book = Entry(frame_form)
entry_book.grid(row=1, column=1, pady=5)

lbl_price = Label(frame_form, text='Price')
lbl_price.grid(row=0, column=2, sticky=W, pady=5, padx=10)
entry_price = Entry(frame_form)
entry_price.grid(row=0, column=3, pady=5)

lbl_count = Label(frame_form, text='Count')
lbl_count.grid(row=1, column=2, sticky=W, pady=5, padx=10)
entry_count = Entry(frame_form)
entry_count.grid(row=1, column=3, pady=5)

lbl_gener = Label(frame_form, text='Gener')
lbl_gener.grid(row=0, column=4, sticky=W, pady=5, padx=10)
entry_gener = Combobox(frame_form)
entry_gener['values'] = ('Romance', 'Science fiction', 'Fantasy', 'Thriller')
entry_gener.grid(row=0, column=5, pady=5)

lbl_sum = Label(frame_form, text='Sum')
lbl_sum.grid(row=1, column=4, sticky=W, pady=5, padx=10)
entry_sum = Entry(frame_form)
entry_sum.grid(row=1, column=5, pady=5)

Radiobutton(frame_form, text='Book', variable=var, value='book').grid(
    row=2, column=0, sticky=W, pady=5)
Radiobutton(frame_form, text='Ebook', variable=var, value='ebook').grid(
    row=2, column=1, sticky=W, pady=5)

# Creating a frame for the table and configuring its layout
frame_table = Frame(root, padding=10, style='My.TFrame')
frame_table.grid(row=2, column=0, padx=10, pady=10)

# Creating a Treeview widget for displaying tabular data
table_main = Treeview(frame_table, columns=(
    1, 2, 3, 4, 5, 6, 7), show='headings')
table_main.pack(side=LEFT, fill=BOTH, expand=True)

# Creating a vertical scrollbar for the table
sc = Scrollbar(frame_table, orient=VERTICAL, command=table_main.yview)
sc.pack(side=RIGHT, fill=Y)
table_main.configure(yscroll=sc.set)

# Configuring column widths for the table
table_main.column(1, width=100)
table_main.column(2, width=100)
table_main.column(3, width=100)
table_main.column(4, width=100)
table_main.column(5, width=100)
table_main.column(6, width=100)
table_main.column(7, width=100)

# Configuring column headings for the table
table_main.heading(1, text='Name')
table_main.heading(2, text='Book')
table_main.heading(3, text='Price')
table_main.heading(4, text='Count')
table_main.heading(5, text='Type')
table_main.heading(6, text='Gener')
table_main.heading(7, text='Sum')

# Binding a function to the release of a mouse button on the table (for selecting items)
table_main.bind('<ButtonRelease>', select_item)

# Creating a frame for buttons and configuring its layout
frame_buttons = Frame(root, padding=10, style='My.TFrame')
frame_buttons.grid(row=3, column=0, padx=10, pady=10, sticky=EW)

# Creating buttons and associating them with respective commands
buttons = [
    ('View', view_click),
    ('Add', add_click),
    ('Edit', edit_click),
    ('Delete', delete_click),
    ('Sort', sort_click),
    ('Search', search_click),
    ('Clear', clear),
    ('Clear All Data', clear_all_click),
    ('Close', close_click)
]

# Adding buttons to the frame using grid layout
for idx, (text, command) in enumerate(buttons):
    btn = Button(frame_buttons, text=text, command=command, style='TButton')
    btn.grid(row=0, column=idx, pady=5, padx=5)


root.mainloop()
