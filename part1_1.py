# Задание 1
# Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
print(f'\nЗадание 1\n')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

print(f'список:\n')
for visits in geo_logs:
    print(visits)

country_filter = input(f'\nвведите страну: ').lower()

filtered_logs = []
for visits in geo_logs:
    for city, country in visits.values():
        if country.lower() == country_filter:
            filtered_logs.append(visits)

print(f'\nобновленный список:\n')
for visits in filtered_logs:
    print(visits)
