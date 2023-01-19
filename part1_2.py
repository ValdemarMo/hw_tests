# Задание 2
#Выведите на экран все уникальные гео-ID из значений словаря ids.
#Т.е. список вида [213, 15, 54, 119, 98, 35]
print(f'\nЗадание 2\n')
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

print(f'список:\n')
for user, geo_user_set in ids.items():
        print (f'{user} : {geo_user_set}')

# вариант 1
geo_set = []
for geo_user_set in ids.values():
    geo_set += geo_user_set
geo_set = set(geo_set)

# вариант 2
# geo_set = set()
# for geo_user_set in ids.values():
#     geo_set = geo_set | set(geo_user_set)

print(f'\nуникальные гео-ID:\n\n{list(geo_set)}')
