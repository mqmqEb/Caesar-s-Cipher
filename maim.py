def encrypt(direction, language, step, text):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(text)):
        if language == 'rus':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        elif language == 'eng':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            elif text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            if direction == 'влево':
                index = (place - int(step)) % alphas
            elif direction == 'вправо':
                index = (place + int(step)) % alphas

            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            elif text[i] == text[i].upper():
                print(upp_alphabet[index], end='')

        else:
            print(text[i], end = '')

def decrypt(direction, language, step, text):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(text)):
        if language == 'rus':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        elif language == 'eng':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            elif text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            if direction == 'влево':
                index = (place + int(step)) % alphas
            elif direction == 'вправо':
                index = (place - int(step)) % alphas

            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            elif text[i] == text[i].upper():
                print(upp_alphabet[index], end='')

        else:
            print(text[i], end = '')


whats_crypt =input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
while whats_crypt != 'шифровать' and whats_crypt != 'дешифровать':
    whats_direction = input('Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n').lower()

whats_direction = input('В какую сторону происходит шаг в шифре? "влево" или "вправо" \n').lower()
while whats_direction != 'влево' and whats_direction != 'вправо':
    whats_direction = input('Что-то не то ты ввёл. Напиши "влево" либо "вправо". \n').lower()

whats_language = input('Какой нужен язык: rus или eng? \n').lower()
while whats_language != 'rus' and whats_language != 'eng':
    whats_language = input('Что-то не то ты ввёл. Напиши "rus" либо "eng". \n').lower()

whats_step = input('На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n')
while whats_step.isdigit() != True:
    whats_step = input('Что-то не то ты ввёл. Напиши число \n')

whats_text = input('Какой текст нужно использовать сейчас? \n')
while whats_text.isspace() == True:
    whats_text = input('Что-то не то ты ввёл. Введи текст. \n')


if whats_crypt == 'шифровать':
    encrypt(whats_direction, whats_language, whats_step, whats_text)
elif whats_crypt == 'дешифровать':
    decrypt(whats_direction, whats_language, whats_step, whats_text)