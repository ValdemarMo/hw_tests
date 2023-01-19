# Задание 3
# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
print(f'\nЗадание 3\n')
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'торрент с зелёными листьями'
    ]
print(f'список запросов:\n')
for querie in queries:
    print(f'{querie}')

analysis = []
print(f'\nколичество слов в запросах:\n')
for querie in queries:
    amount = len(querie.split())
    analysis.append(amount)
    print(f'{amount} - {querie}')
print()

original_elements = list(set(analysis))

final_list = {}
for element in original_elements:
    final_list[element] = analysis.count(element)
# print(f'{final_list}\n')

elements_sum = sum(final_list.values())
for element in final_list:
    final_list[element] = analysis.count(element)
    print(f'запросов из {element} слов {final_list[element]} ({final_list[element]/elements_sum * 100} %)')

# Задание 4
# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
print(f'\nЗадание 4\n')

stats = {'facebook': 55, 'yandex': 10, 'vk': 315, 'google': 199, 'email': 242, 'ok': 98}
print('продажи\n')

for name, sales in stats.items():
    print(f'{name} - {sales}')

maximum = max(stats.values())  # вынес из цикла из соображений исключения лишнего пересчета каждый раз
for name, sales in stats.items():
    if sales == maximum:
        champion = name
        print(f'\nмаксимальные продажи \n\n{champion} - {sales}')