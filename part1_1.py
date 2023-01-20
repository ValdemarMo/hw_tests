def country_filter(logs, filter):
    filtered_logs = []
    for visits in logs:
        for city, country in visits.values():
            if country == filter:
                filtered_logs.append(visits)
    return filtered_logs

# def test1_1():
#     dx = [
#         {'visit1': ['Москва', 'Россия']},
#         {'visit2': ['Дели', 'Индия']},
#         {'visit3': ['Владимир', 'Россия']},
#         {'visit4': ['Лиссабон', 'Португалия']},
#         {'visit5': ['Париж', 'Франция']},
#         {'visit6': ['Лиссабон', 'Португалия']},
#         {'visit7': ['Тула', 'Россия']},
#         {'visit8': ['Тула', 'Россия']},
#         {'visit9': ['Курск', 'Россия']},
#         {'visit10': ['Архангельск', 'Россия']}
#     ]
#
#     f = "Россия"
#
#     rx = [
#         {'visit1': ['Москва', 'Россия']},
#         {'visit3': ['Владимир', 'Россия']},
#         {'visit7': ['Тула', 'Россия']},
#         {'visit8': ['Тула', 'Россия']},
#         {'visit9': ['Курск', 'Россия']},
#         {'visit10': ['Архангельск', 'Россия']}
#     ]
#
#     assert country_filter(dx, f) == rx
#
# if __name__ == '__main__':
#     test1_1()
