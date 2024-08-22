from collections import namedtuple

# Определение структуры данных для хранения оценок
Grade = namedtuple('Grade', ['name', 'grades'])

# Создание экземпляров Grade для каждого ученика
grades = [
    Grade('Aaron', [5, 3, 3, 5, 4]),
    Grade('Bilbo', [2, 2, 2, 3]),
    Grade('Johnny', [4, 5, 5, 2]),
    Grade('Khendrik', [4, 4, 3]),
    Grade('Steve', [5, 5, 5, 4, 5])
]

# Словарь для хранения результатов
results = {}

# Перебор всех оценок
for grade in grades:
    # Получение имени ученика
    name = grade.name
    # Получение оценок ученика
    scores = grade.grades
    # Вычисление среднего балла
    average = sum(scores) / len(scores)
    # Добавление результата в словарь
    results[name] = average

# Вывод результатов
for name, average in results.items():
    print(f"{name}: {average}")
