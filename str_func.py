'''функция, которая переводит все символы строки
со ввода в верхний регистр'''
def upper_index(string):
    return str(string).upper()

'''функция, которая делает заглавными первые буквы слов в строке со ввода'''
def upper_first_letter(string):
    splitted_string = string.split(' ')

    list = []
    for word in splitted_string:
        new_word = (word[0].upper()+word[1:])
        list.append(new_word)
    return ' '.join(list)

