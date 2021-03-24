#declaration of variables
filename = 'livros.txt'
books = []
author = []
status = []

#funcion read
def read_file(file, ord, is_ord):
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
    
    
    if ord:
        ordenar(books, author, status, is_ord)
    else:
        output(books, author, status)

def ordenar(book, author, status, is_ord):
    c = 0
    crescente = True

    mid = int(len(book) / 2)
    point = mid
    while c == 0:
        trocas = 0
        certeza = 0
        if is_ord == '1':
            if crescente == True:
                if book[point] > book[point + 1]:
                    book[point], book[point + 1] = book[point + 1], book[point]
                    author[point], author[point + 1] = author[point + 1], author[point]
                    status[point], status[point + 1] = status[point + 1], status[point]
                    trocas += 1
                
                point += 1
                if point == len(book) - 1:
                    point -= 1
                    crescente = False
            else:
                if book[point] < book[point - 1]:
                    book[point], book[point - 1] = book[point - 1], book[point]
                    author[point], author[point - 1] = author[point - 1], author[point]
                    status[point], status[point - 1] = status[point - 1], status[point]
                    trocas += 1
                
                point -= 1
                if point == 0:
                    crescente = True
                
                    if trocas == 0:
                        c = 1
        elif is_ord == '2':
            if crescente == True:
                if author[point] > author[point + 1]:
                    author[point], author[point + 1] = author[point + 1], author[point]
                    book[point], book[point + 1] = book[point + 1], book[point]
                    status[point], status[point + 1] = status[point + 1], status[point]
                    trocas += 1
                
                point += 1
                if point == len(book) - 1:
                    point -= 1
                    crescente = False
            else:
                if author[point] < author[point - 1]:
                    author[point], author[point - 1] = author[point - 1], author[point]
                    book[point], book[point - 1] = book[point - 1], book[point]
                    status[point], status[point - 1] = status[point - 1], status[point]
                    trocas += 1
                
                point -= 1
                if point == 0:
                    crescente = True
                
                    if trocas == 0:
                        c = 1
        elif is_ord == '3':
            if crescente == True:
                if status[point] > status[point + 1]:
                    status[point], status[point + 1] = status[point + 1], status[point]
                    author[point], author[point + 1] = author[point + 1], author[point]
                    book[point], book[point + 1] = book[point + 1], book[point]
                    trocas += 1
                
                point += 1
                if point == len(book) - 1:
                    point -= 1
                    crescente = False
            else:
                if status[point] < status[point - 1]:
                    status[point], status[point - 1] = status[point - 1], status[point]
                    author[point], author[point - 1] = author[point - 1], author[point]
                    book[point], book[point - 1] = book[point - 1], book[point]
                    trocas += 1
                
                point -= 1
                if point == 0:
                    crescente = True
                
                    if trocas == 0:
                        point = 0
                        crescente = True

                 
    output(book, author, status)

def output(book, author, status):
    #finding the longest string
    max = ''
    for c in book:
        if len(c) > len(max):
            max = c
            max_book = len(c)
    
    max = ''
    for c in author:
        if len(c) > len(max):
            max = c
            max_author = len(c)

    max = ''
    for c in status:
        if len(c) > len(max):
            max = c
            max_status = len(c)
    
    #calculating the header space
    header_book = max_book - 5 + 2
    header_author = max_author - 4 + 2
    header_status = max_status - 5 + 2

    #header
    print('livros', ' '*header_book,'Autor', ' '*header_author,'Estado', ' '*header_status)
    #output
    for c in range(len(book)):
        #calculating the space of books, author and status
        space_book = max_book - len(book[c]) +3
        space_author = max_author - len(author[c]) +3
        space_status = max_status - len(status[c]) +3

        #print
        print(f'{book[c]}', ' '*space_book, f'{author[c]}',' '*space_author, f'{status[c]}', ' '*space_status)
        print()
        
#function write in the file
def write_file(file, book, author, status):
    arquivo = open(filename, 'a')
    if vazio:
        arquivo.write(f'{book.title()}|{author.title()}|{status.title()}')
    else:
        arquivo.write(f'\n{book.title()}|{author.title()}|{status.title()}')
    arquivo.close()

#Inicializing the file
try:
    file = open(filename,'x',encoding='latin1')
    file.close()
except FileExistsError:
    pass

#input 
while True:
    with open(filename, encoding='latin1') as file_object:
        file = file_object.read()

    choice = input('[1]Ler a lista de livros\n[2]Adicionar livro\n[3]Sair: ')

    if choice == '1':
        if file == '':
            print('Não existe nada no arquivo, adicione algum livro!')
            vazio = True
            continue
        choice2 = input('[1]Ler a lista normal\n[2]Ler a lista ordenada\n')
        if choice2 == '1':
            read_file(file, False, choice2)
        if choice2 == '2':
            choice3 = input('Ordenar por\n[1]Título\n[2]Autor\n[3]Status: ')
            read_file(file, True, choice3)

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