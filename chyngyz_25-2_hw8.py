user_input = int(input("Загадайте число от 0 до 100: "))


half = 100
count = 0
half2 = 1
tries = []
while True:
    try:
        current = (half + half2) // 2
        is_right = input(f'Ваше число:{current}?(да, больше, меньше): ')
        if current == user_input:
            print('Я угадал ваше число!')
            break
        elif current < user_input:
            half2 = current + 1
        else:
            half = current - 1
        tries.append(current)
        count += 1
    except:
        print("Вводите только: (да, больше, меньше)")


with open('results.txt', 'w', encoding="utf-8") as file:
    file.write(
        f'Количество попыток: {count}'
        f'\nСписок попыток: {tries}'
        f'\nЗагаданное число: {user_input}'
    )