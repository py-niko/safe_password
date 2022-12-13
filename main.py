from random import *

while True:
    print('Привет я генератор паролей, давай помогу тебе создать пароль(ли)!')
    # количество паролей
    def count():
        q = input('Введите количество паролей: ').strip()
        if q.isdigit() == True:
            print(f'Вы задали {q} паролей')
            return int(q)
        else:
            count()
            print('введите пожалуйста число!')


    # длинна пароля
    def lenght():
        l = input('Введите длинну пароля: ').strip()
        if l.isdigit() == True:
            print(f'Вы задали длинну паролей {l}')
            return int(l)
        else:
            lenght()
            print('введите пожалуйста число!')


    # включать цифры или нет
    def lowdigit():
        question_lowdg = input('включать ли цифры в пароль? Ответ:').strip()
        y = ['lf', 'да', 'l', 'д', 'yes', 'нуы']
        if question_lowdg.lower() in y:
            print('цифры включены в пароль')
            return True
        else:
            ('цифры исключены из пароля')
            return False


    def bigdg():
        question_bigdg = input('включать ли большие буквы в пароль? Ответ: ').strip()
        y = ['lf', 'да', 'l', 'д', 'yes', 'нуы']
        if question_bigdg.lower() in y:
            print('большие буквы включены в пароль')
            return True
        else:
            print('большие цифры исключены из пароля')
            return False


    def smalldg():
        question_smalldg = input('включать ли маленькие буквы в пароль? Ответ: ').strip()
        y = ['lf', 'да', 'l', 'д', 'yes', 'нуы']
        if question_smalldg.lower() in y:
            print('маленькие буквы включены в пароль')
            return True
        else:
            print('маленькие цифры исключены из пароля')
            return False


    def punct():
        question_punct = input('включать ли знаки пунктуации пароль? Ответ: ').strip()
        y = ['lf', 'да', 'l', 'д', 'yes', 'нуы']
        if question_punct.lower() in y:
            print('маленькие буквы включены в пароль')
            return True
        else:
            print('маленькие цифры исключены из пароля')
            return False


    def ignor():
        question_znak = input('исключаем двоякие знаки? Ответ: ').strip()
        y = ['lf', 'да', 'l', 'д', 'yes', 'нуы']
        if question_znak.lower() in y:
            print('знаки включенны в пароль')
            return True
        else:
            print('неоднозначности исключены')
            return False


    def spisok(s):
        if lowdigit() == True:
            s += digits
        if bigdg() == True:
            s += lowercase_letters
        if smalldg() == True:
            s += uppercase_letters
        if punct() == True:
            s += punctuation
        if ignor() == True:
            for i in ignor_simbol:
                s = s.replace(i, '')
        return s


    def generated_pass(n, k, chars):
        for i in range(n):
            password = []
            for j in range(k):
                password.append(choice(chars))
            print(''.join(password))


    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    ignor_simbol = 'il1Lo0O'
    chars = ''

    n = count()
    k = lenght()
    chars = spisok(chars)

    generated_pass(n, k, chars)

