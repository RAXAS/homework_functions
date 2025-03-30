def check_user_age(birth_year):
    if birth_year < 1900 or birth_year > 2025:
        print("Ошибка. Введите корректный год рождения!")
    else:
        user_age = 2025 - birth_year
        if 66 > user_age > 18:
            print("Отличный возраст для карьерного роста!")
        elif user_age > 65:
            print("Пора наслаждаться заслуженным отдыхом!")
        else:
            print("Вы еще молоды, учеба — ваш путь!")


user_birth_year = int(input("Введите год вашего рождения: "))
check_user_age(user_birth_year)
