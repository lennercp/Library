import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER
from tkinter.messagebox import showinfo
from books import Books

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200+200+100')

frameOptions = tk.Frame(root)
frameOptions.pack()



frameTree = tk.Frame(root)
frameTree.pack()
#global variables
order = 'Desc'

def DeleteAllRows():
    for row in tree.get_children():
        tree.delete(row)

def ShowBooks(heading='title'):
    DeleteAllRows()

    global order

    with Books() as b:
        books = b.orderBooks(heading, order)
    
    if order == 'Desc':
        order = 'Asc' 
    else:
        order = 'Desc'

    for book in books:
        tree.insert(parent='', index='end',text='', values=(book[1], book[2], book[3]))

# define columns
columns = ('Titulo', 'Autor', 'Status')

tree = ttk.Treeview(frameTree, columns=columns, show='headings')

#configure columns
tree.column(columns[0], anchor=CENTER)
tree.column(columns[1], anchor=CENTER)
tree.column(columns[2], anchor=CENTER)

# define headings
tree.heading(columns[0], text=columns[0], command=lambda: ShowBooks('title'))
tree.heading(columns[1], text=columns[1], command=lambda: ShowBooks('author'))
tree.heading(columns[2], text=columns[2], command=lambda: ShowBooks('status'))

ShowBooks()


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(frameTree, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()