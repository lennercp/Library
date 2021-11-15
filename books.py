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
        # print('fechou')

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
# central('order', 'id', 'ASC')
