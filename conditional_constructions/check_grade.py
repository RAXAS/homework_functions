def check_grade(score):
    if 100 >= score >= 90:
        return "Отлично"
    elif 89 >= score >= 75:
        return "Хорошо"
    elif 74 >= score >= 50:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"


score = 90
grade = check_grade(score)
print(f"Оценка за {score} баллов: {grade}")
