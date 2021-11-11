#declaration of variables
from dbconnection import connectDb

con = connectDb()
cur = con.cursor()

class Books:
    def __init__(self):
        self.conn = connectDb()
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        self.conn.commit()
        self.conn.close()
        self.cur.close()
        print('fechou')

    def addBook(self, title, author, status):
        try:
            self.cur.execute(f"INSERT INTO table_books (title, author, status) VALUES ('{title.capitalize()}', '{author.title()}', '{status.capitalize()}')")
        except Exception as e:
            print('deu erro', e)

    def findBook(self, title):
        try:
            self.cur.execute(f"SELECT * FROM table_books WHERE title='{title}'")
            return (self.cur.fetchall())
        except Exception as e:
            print('deu erro', e)
    
    def orderBooks(self, table, order):
        if table.lower() not in ['id','title', 'author', 'status']:
            return -1
        elif order.upper() not in ['ASC', 'DESC']:
            return -1
        else:
            self.cur.execute(f"SELECT * FROM table_books ORDER BY {table.lower()} {order.upper()}")
            return (self.cur.fetchall())

    def deleteBook(self, id):
        try:
            self.cur.execute(f"DELETE FROM table_books WHERE id = {id}")
        except Exception as e:
            print('deu erro', e)
# with Books() as b:
    # b.addBook('codIgo da vinci', 'DAn BRown', 'LiDo')
    # b.addBook('Chronos', 'Rysa walker', 'LiDo')
    # b.addBook('feminismo: subversão', 'ana campagnolo', 'pretendo')
    # b.findBook('Chronos')
    # b.orderBooks('id', 'Desc')

def central(operation, *params):
    operations = {'insert': 'b.addBook(', 'find': 'b.findBook(', 'order':'b.orderBooks(', 'delete': 'b.deleteBook('}
    if operation in operations.keys():
        with Books() as b:
            try:
                value = eval(f'{operations[operation]} *params)')
                if value is not None:
                    print(value)
            except Exception as e:
                print('deu erro', e)

# central('insert', 'diario de um banana', 'jeff kinney', 'lido')
# central('delete', '5')
central('order', 'id', 'ASC')

#funcion read
# def read_file(file, ord, is_ord):
#     books = []
#     author = []
#     status = []
#     lines = file.split('\n')

#     #separating within the list
#     for c in range(len(lines)):
#         lines[c] = lines[c].split('|')

#     #separating by book, author and status
#     for c in range(len(lines)):
#         for i in range(3):
#             if i == 0:
#                 books.append(lines[c] [i])
#             if i == 1:
#                 author.append(lines[c] [i])
#             if i == 2:
#                 status.append(lines[c] [i])
    

# def output(book, author, status):
#     #finding the longest string
#     max = ''
#     for c in book:
#         if len(c) > len(max):
#             max = c
#             max_book = len(c)
    
#     max = ''
#     for c in author:
#         if len(c) > len(max):
#             max = c
#             max_author = len(c)

#     max = ''
#     for c in status:
#         if len(c) > len(max):
#             max = c
#             max_status = len(c)
    
#     #calculating the header space
#     header_book = max_book - 5 + 2
#     header_author = max_author - 4 + 2
#     header_status = max_status - 5 + 2

#     #header
#     print('livros', ' '*header_book,'Autor', ' '*header_author,'Estado', ' '*header_status)
#     #output
#     for c in range(len(book)):
#         #calculating the space of books, author and status
#         space_book = max_book - len(book[c]) +3
#         space_author = max_author - len(author[c]) +3
#         space_status = max_status - len(status[c]) +3

#         #print
#         print(f'{book[c]}', ' '*space_book, f'{author[c]}',' '*space_author, f'{status[c]}', ' '*space_status)
#         print()
        
# #function write in the file
# def write_file(file, book, author, status):
#     arquivo = open(filename, 'a')
#     if vazio:
#         arquivo.write(f'{book.title()}|{author.title()}|{status.title()}')
#     else:
#         arquivo.write(f'\n{book.title()}|{author.title()}|{status.title()}')
#     arquivo.close()

# #Inicializing the file
# try:
#     file = open(filename,'x',encoding='latin1')
#     file.close()
# except FileExistsError:
#     pass

# #input 
# while True:
#     with open(filename, encoding='latin1') as file_object:
#         file = file_object.read()

#     choice = input('[1]Ler a lista de livros\n[2]Adicionar livro\n[3]Sair: ')

#     if choice == '1':
#         if file == '':
#             print('Não existe nada no arquivo, adicione algum livro!')
#             vazio = True
#             continue
#         choice2 = input('[1]Ler a lista normal\n[2]Ler a lista ordenada\n')
#         if choice2 == '1':
#             read_file(file, False, choice2)
#         if choice2 == '2':
#             choice3 = input('Ordenar por\n[1]Título\n[2]Autor\n[3]Status: ')
#             read_file(file, True, choice3)

#     elif choice == '2':
#         book = input('Digite o nome do livro: ')
#         author = input('Digite o nome do autor: ')
#         status = input('Digite o nome do estado do livro: ')

#         write_file(file, book, author, status)

#     elif choice == '3':
#         print('Desligando...')
#         break

#     else:
#         print('digite um valor válido')

#     print()    