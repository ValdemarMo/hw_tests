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

c_filter = 'Россия'
def country_filter(self, geo_logs, filter):
    filtered_logs = []
    for visits in geo_logs:
        for city, country in visits.values():
            if country == filter:
                filtered_logs.append(visits)

print(country_filter(geo_logs, c_filter))

print(f'\nобновленный список:\n')
for visits in country_filter(geo_logs, filter):
    print(visits)

