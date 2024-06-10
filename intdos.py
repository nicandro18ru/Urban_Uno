# Присваиваем булевое значение для начала цикла выбора задания
seleccionar_una_tarea  = True


# Запускаем цикл выбора задания while
while seleccionar_una_tarea:
    print("Набор заданий:\n1. Подсчёт букв в слове\n2. Суммы и разности\n3. Среднее арифметическое из трёх чисел\n4. Простые строчки\n5. Сложная формула (a * b) + (a + c)\n0. Выйти")


    seleccionar_una_tarea = input('Введите номер задания для выполнения: ')

    if seleccionar_una_tarea == '1': # если вводим цифру 1, то выдаст первое задание. Здесь идёт условие "если/то" (if/else)

        # Создаём словарь для переменных. own_variables - это только название, можно обозвать по-другому. В скобках оставляем пустое место, или можно записать перменные ниже.
        own_variables = {}

        # Заполняем словарь этими переменными. Вызов переменной после знака равно.
        own_variables['determining_length_word'] = 'Uno'
        own_variables['determining_length_word_1'] = 'Uno_1'

        # Задаём значение переменной от своего слово. Спршивают о слове, вы пишете и одновременно задаёте значение.
        Uno = input('Давайте посчитаем, сколько в вашем слове букв. Напишите любое слово: ')

        # Используем вторую переменную. В данном случае от первой переменной вычисляем количество символов в вашем значении через функцию len() 
        Uno_1 = len(Uno)
        Uno_1 = print('\n' f'В вашем слове "{Uno}" - {Uno_1} букв.' '\n') # Выводит результат в ответе.

    elif seleccionar_una_tarea == '0': # вариация if, но в виде продолжения перебора, если первый результат if не совпал со значением 1. В данном случае он активируется, если ввести цифру 0.
        print("Спасибо, до скорых встреч!") # Прощальная записка :)
        seleccionar_una_tarea = False # булевое значение равняется "Неверно", а значит скрипт завершается.

    elif seleccionar_una_tarea == '2':
        own_variables = {}
        own_variables['sums_and_differences_1'] = 'Dos_first'
        own_variables['sums_and_differences_2'] = 'Dos_second'
        own_variables['sums_and_differences_3'] = 'Dos_diff'
        own_variables['sums_and_differences_4'] = 'Dos_summa'

        Dos_first = int(input('Введите первое число из двух для подсчёта суммы и разности\n'))
        Dos_second = int(input('Введите второе число для подсчёта суммы и разности\n'))
        Dos_diff = int(Dos_first - Dos_second)
        Dos_summa = int(Dos_first + Dos_second)
        print('\nРазность ваших чисел равна ', Dos_diff,'\nСумма ваших чисел равна ', Dos_summa, '\n')

    elif seleccionar_una_tarea == '3':
        own_variables = {}
        own_variables['arithmetic_mean_1'] = 'Dos_first'
        own_variables['arithmetic_mean_2'] = 'Dos_second'
        own_variables['arithmetic_mean_3'] = 'Dos_third'
        own_variables['arithmetic_mean_4'] = 'Dos_mean'

        Dos_first = int(input('Введите первое число\n'))
        Dos_second = int(input('Введите второе число\n'))
        Dos_third = int(input('Введите последнее третье число\n'))
        Dos_mean = int((Dos_first + Dos_second + Dos_third) // 3 )
        print('\nСреднее арифметическое ваших чисел - ', Dos_mean, '\n')

    elif seleccionar_una_tarea == '4':
        own_variables = {}
        own_variables['Weekday_1'] = 'Dos_first'
        own_variables['Weekday_2'] = 'Dos_second'
        Dos_first = str('Понедельник')
        Dos_second = str('Вторник')
        print('\nСегодня, в', Dos_first, 'мы изучали одну тему, а завтра, во', Dos_second, ' мы будем изучать другую тему\n')

    elif seleccionar_una_tarea == '5':
        own_variables = {}
        own_variables['A_complex_formula_1'] = 'Uno_a'
        own_variables['A_complex_formula_2'] = 'Uno_b'
        own_variables['A_complex_formula_3'] = 'Uno_c'
        own_variables['A_complex_formula_4'] = 'Uno_f'

        Uno_a = 'a'
        Uno_b = 'b'
        Uno_c = 'c'
        Uno_a = int(input(f'Перед вами представлена формула для подсчёта числа при следующем уравнении:\n({Uno_a} * {Uno_b}) + ({Uno_a} * {Uno_c}).\nЗаполните первое число "a": '))
        Uno_b = int(input(f'({Uno_a} * {Uno_b}) + ({Uno_a} * {Uno_c})\nЗаполните второе число "b": '))
        Uno_c = int(input(f'({Uno_a} * {Uno_b}) + ({Uno_a} * {Uno_c})\nЗаполните третье число "c": '))
        Uno_f = int((Uno_a * Uno_b) + (Uno_a + Uno_c))
        print(f'\nВычисляем ваш результат в этой формуле: ({Uno_a} * {Uno_b}) + ({Uno_a} * {Uno_c}) = {Uno_f}\n')

    
    else:               # Если ни одно значение не совпало
        print('\nНеккоректный ввод. Введите номер задания.\n')    # выводит сообщение и предлагает заного пойти по циклу.
