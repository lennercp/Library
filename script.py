#declaration of variables
filename = 'livros.txt'
books = []
author = []
status = []
max_book = 0
max_author = 0
max_status = 0


#funcion read
def read_file(file):
    books = []
    author = []
    status = []
    lines = file.split('\n')

    #separating within the list
    for c in range(len(lines)):
        lines[c] = lines[c].split('|')

    #separating by book, author and status
    for c in range(len(lines)):
        for i in range(3):
            if i == 0:
                books.append(lines[c] [i])
            if i == 1:
                author.append(lines[c] [i])
            if i == 2:
                status.append(lines[c] [i])
    
    #finding the longest string
    max = ''
    for c in books:
        if len(c) > len(max):
            max = c
            max_book = len(c)

            print(c, max, max_book)
    
    max = ''
    for c in author:
        if c > max:
            max = c
            max_author = len(c)
            print(c, max_author)
    
    max = ''
    for c in status:
        if c > max:
            max = c
            max_status = len(c)
            print(c, max_status)
    
    #calculating the header space
    header_book = max_book - 5 + 2
    header_author = max_author - 4 + 2
    header_status = max_status - 5 + 2

    #header
    print('livros', ' '*header_book,'Autor', ' '*header_author,'Estado', ' '*header_status)

    #output
    for c in range(len(books)):
        #calculating the space of books, author and status
        space_book = max_book - len(books[c]) +3
        space_author = max_author - len(author[c]) +3
        space_status = max_status - len(status[c]) +3

        #print
        print(f'{books[c].capitalize()}', ' '*space_book, f'{author[c].title()}',' '*space_author, f'{status[c].title()}', ' '*space_status)
        print()
        
#function write in the file
def write_file(file, book, author, status):
    arquivo = open(filename, 'a')
    arquivo.write(f'\n{book}|{author}|{status}')
    arquivo.close()

#Inicializing the file
try:
    file = open(filename,'x')
except FileExistsError:
    with open(filename) as file_object:
        file = file_object.read()

#input 
while True:
    choice = input('[1]Ler a lista de livros\n[2]Adicionar livro\n[3]Sair: ')

    if choice == '1':
        file = open(filename)
        read_file(file.read())

    elif choice == '2':
        book = input('Digite o nome do livro: ')
        author = input('Digite o nome do autor: ')
        status = input('Digite o nome do estado do livro: ')

        write_file(file, book, author, status)

    elif choice == '3':
        print('Desligando...')
        break

    else:
        print('digite um valor válido')

    print()