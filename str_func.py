'''функция, которая переводит все символы строки
со ввода в верхний регистр'''
def upper_index(string):
    return str(string).upper()

'''функция, которая делает заглавными первые буквы слов в строке со ввода'''
def upper_first_letter(string):
    splitted_string = string.split(' ')

    new_list = []
    for word in splitted_string:
        new_word = (word[0].upper()+word[1:])
        new_list.append(new_word)
    return ' '.join(new_list)

