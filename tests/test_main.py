from unittest import TestCase
from part1_1 import country_filter
from part1_2 import unical_id
from part1_3 import max_stats
from libX1.y import token
from part2 import YaUploader

class TestCountryFilter(TestCase):
    def test_country_filter(self):

        dx = [
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

        f = "Россия"

        rx = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        res = country_filter(dx, f)
        self.assertEqual(res,rx)

class TestUnicalId(TestCase):
    def test_unical_id(self):

        dx = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

        rx = [98, 35, 15, 213, 54, 119]

        res = list(unical_id(dx))
        self.assertEqual(res, rx)

class TestMaxStats(TestCase):
    def test_max_stats(self):

        stats = {'facebook': 55, 'yandex': 10, 'vk': 315, 'google': 199, 'email': 242, 'ok': 98}
        cx = 'vk'

        res = max_stats(stats)
        self.assertEqual(res, cx)

class TestYaFolder(unittest.TestCase):

    # def setUp(self):
    #     print("method setUp")
    #
    # def tearDown(self):
    #     print("method tearDown")

    def test_create_folder(self):
        folder = 'test_x'
        yadisk = YaUploader(token)
        res = yadisk.create_folder(folder)
        self.assertEqual(res, 201)
        print(f'папка {folder} создана')

    @unittest.skip('негативный аналог на повторное создание есть ниже')
    def test_create_twice(self):
        folder = 'test_x'
        yadisk = YaUploader(token)
        res = yadisk.create_folder(folder)
        self.assertEqual(res, 409)
        print(f'папка {folder} повторно не создается (создалась ранее)')

    def test_create_twice_not(self):
        folder = 'test_x'
        yadisk = YaUploader(token)
        res = yadisk.create_folder(folder)
        self.assertNotEqual(res, 201)
        print(f'папка {folder} повторно не создается (создалась ранее)')

    @unittest.expectedFailure
    def test_create_digital_name(self):
        folder = 43
        yadisk = YaUploader(token)
        res = yadisk.create_folder(folder)
        print(f'название папки {folder} - в цифровом формате')
        self.assertEqual(res, 201)

    def test_request_folder(self):
        folder = 'test_x'
        yadisk = YaUploader(token)
        res = yadisk.request_folder(folder)
        self.assertEqual(res, 200)
        print(f'папка {folder} существует')
        res = yadisk.del_folder(folder)
        if res == 202:
            print(f'папка не пустая {folder} поставлена в очередь на удаление')
        if res == 204:
            print(f'папка {folder} удалена')