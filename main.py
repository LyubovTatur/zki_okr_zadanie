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
    return square
def setter(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n
def encode(text, square1,square2):
    for pair_letters in range(len(text)):

create_square('соска')

