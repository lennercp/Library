def order(book, author, status, is_ord):
    c = 0
    crescente = True

    mid = int(len(book) / 2)
    point = mid
    while c == 0:
        trocas = 0
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
                        c = 1 
    output(book, author, status)