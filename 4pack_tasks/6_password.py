def check_password_level(letter):
    if len(letter) < 6:
        exit('Недопустимый пароль')
    elif letter.isdigit() or (letter.isalpha() and letter.islower()) or (letter.isalpha() and letter.isupper()):
        exit('Ненадежный пароль')
    elif letter.isalpha() or (letter.isalnum() and letter.islower()) or (letter.isalnum() and letter.isupper()):
        exit('Слабый пароль')
    else:
        print('Надежный пароль')


password = input()
check_password_level(password)
