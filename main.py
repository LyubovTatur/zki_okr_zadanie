ALPHABET = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ',',','.')
def create_square(key):
    key = setter(key)
    temp_alphabet = list(ALPHABET)
    for char in key:
        if char in temp_alphabet:
            temp_alphabet.remove(char)
    temp_list = key+temp_alphabet
    square = list()
    for i in range(6):
        square.append(temp_list[i*6:(i+1)*6])
        print(square[i])
    print('________')
    return square
def setter(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n
def encode(text, key_1,key_2):
    range_val = len(text)
    result = ''
    square_1 = create_square(key_1)
    square_2 = create_square(key_2)

    if len(text) %2 != 0:
        range_val += 1
        text += ' '
    i = 0
    while i < range_val:
        letter_1 = text[i]
        letter_2 = text[i+1]
        i += 2
        x_1 = -1
        y_1 = -1
        x_2 = -1
        y_2 = -1
        for y in range(len(square_1)):
            for x in range(len(square_1[0])):
                if square_1[x][y] == letter_1:
                    x_1 = x
                    y_1 = y
                if square_2[x][y] == letter_2:
                    x_2 = x
                    y_2 = y
        if y_1 == y_2:
            if x_1 != 5:
                x_1+=1
            else:
                x_1=0
            if x_2!=5:
                x_2+=1
            else:
                x_2=0

        if x_1 == x_2:
            if y_1 != 5:
                y_1 += 1
            else:
                y_1 = 0
            if y_2 != 5:
                y_2 += 1
            else:
                y_2 = 0
        #print(str(x_1)+' '+str(y_1) + ' ' +letter_1  + ' | ' + str(x_1) + ' '+ str(y_2)+ ' ' + square_2[x_1][y_2] )
        #print(str(x_2)+' '+str(y_2) + ' ' +letter_2  + ' | ' + str(x_2) + ' '+ str(y_1)+ ' ' + square_1[x_2][y_1] )
        #print('________')
        #result = result+square_2[y_1][y_2]+square_1[x_2][x_1]
        #result = result+square_2[x_1][x_2]+square_1[y_2][y_1]
        result = result + square_2[x_1][y_2] + square_1[x_2][y_1]
        #result = result+square_2[y_2][y_1]+square_1[x_1][x_2]
        #result = result+square_2[x_2][x_1]+square_1[y_1][y_2]

    return result

def decode(text, key_1,key_2):
        range_val = len(text)
        result = ''
        square_1 = create_square(key_1)
        square_2 = create_square(key_2)

        if len(text) % 2 != 0:
            range_val += 1
            text += ' '
        i = 0
        while i < range_val:
            letter_1 = text[i]
            letter_2 = text[i + 1]
            i += 2
            x_1 = -1
            y_1 = -1
            x_2 = -1
            y_2 = -1
            for y in range(len(square_1)):
                for x in range(len(square_1[0])):
                    if square_1[x][y] == letter_1:
                        x_1 = x
                        y_1 = y\
                    if square_2[x][y] == letter_2:
                        x_2 = x
                        y_2 = y
            if y_1 == y_2:
                x_1 -= 1
                x_2 -= 1
            if x_1 == x_2:
                y_1 -= 1
                y_2 -= 1


            # print(str(x_1)+' '+str(y_1) + ' ' +letter_1  + ' | ' + str(x_1) + ' '+ str(y_2)+ ' ' + square_2[x_1][y_2] )
            # print(str(x_2)+' '+str(y_2) + ' ' +letter_2  + ' | ' + str(x_2) + ' '+ str(y_1)+ ' ' + square_1[x_2][y_1] )
            # print('________')
            # result = result+square_2[y_1][y_2]+square_1[x_2][x_1]
            # result = result+square_2[x_1][x_2]+square_1[y_2][y_1]
            result = result + square_2[x_1][y_2] + square_1[x_2][y_1]
            # result = result+square_2[y_2][y_1]+square_1[x_1][x_2]
            # result = result+square_2[x_2][x_1]+square_1[y_1][y_2]
            # ЗАДАНИЕ ОКР ПО ОКРУ ЗАДАНИЯ ЗАДАННОГО ОКРА РЯД СУММА РЯДА СЧИТАТЬ ФУПРШФПОФШРРПЖБИДВЗТТМРСНАЫЛМЛЛИЖ
            # ПИСЬКА И ПОПКА СИСЬКА И ПИСЬКА
            # ГОНЯХЧИК ПЛИЗКИ???
            # НЯХОВОЕ (НЯШЕНОЕ(НЯШЕЧНОВОЕ)) ОК ПОГНАЛОВОЕ)
            # КИНЬ ФОТКУ ЖОПЫ В ЮБКЕ ПЛИЗКИ??????????????????????
            # ОК АРТЕМ ЛЮБИМЫЙ СДЕЛАЕМ ВСЕСТЕ ок

        return result
text = input('введите сообщение')
key_1 = input('ведите первый ключ')
key_2 = input('введите второй ключ')
print('зашифрованное')
coded_text = encode(text, key_1,key_2)
print(coded_text)
print('расшифрованное')
print(decode(coded_text, key_2,key_1))