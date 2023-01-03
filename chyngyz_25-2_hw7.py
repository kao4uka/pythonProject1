ten = list(range(1, 11))                   # создаем список
evens = list(filter(lambda ten : not ten % 2, map(int, ten)))       # оставляем только четные числа из списка ten
print(list(map(lambda evens: evens ** 2, evens)))       # выводим на экран квадраты четных чисел


def index_output(ten):          # создаем фунцкию
    while True:
        print("Введите число 0, чтобы завершить процесс")       # подсказка для завершения процесса
        try:
            index = int(input("Введите индеск: "))      #просим ввести индекс
            if index != 0:
                print(ten[index-1])
        except:
            print("Такого индекса нету! Индекс должен состоять только из целых чисел от 0 до 9")
            continue
        if index == 0:
            print("Процесс завершен!")
            break

print(index_output(ten))        # выводим результат
