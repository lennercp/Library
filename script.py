#declaration of variables
filename = 'livros.txt'
books = []
author = []
state = []

#funcion read
def read_file(file):
    books = []
    author = []
    state = []
    lines = file.split('\n')

    #separando dentro da lista
    for c in range(len(lines)):
        lines[c] = lines[c].split('|')

    #separando por livro, autor e estado
    for c in range(len(lines)):
        for i in range(3):
            if i == 0:
                books.append(lines[c] [i])
            if i == 1:
                author.append(lines[c] [i])
            if i == 2:
                state.append(lines[c] [i])
    
    print('livros:')
    for c in range(len(books)):
        print(f'{books[c]}, {author[c]}, {state[c]}')
        
def write_file(file, book, author, state):
    arquivo = open(filename, 'a')
    arquivo.write(f'\n{book}|{author}|{state}')
    arquivo.close()

try:
    file = open(filename,'x')
except FileExistsError:
    with open(filename) as file_object:
        file = file_object.read()

while True:
    choice = input('[1]Ler a lista de livros\n[2]Adicionar livro\n[3]Sair: ')

    if choice == '1':
        file = open(filename)
        read_file(file.read())
    elif choice == '2':
        book = input('Digite o nome do livro: ')
        author = input('Digite o nome do autor: ')
        state = input('Digite o nome do estado do livro: ')

        write_file(file, book, author, state)
    elif choice == '3':
        print('Desligando...')
        break
    else:
        print('digite um valor')
    print('-'*15)