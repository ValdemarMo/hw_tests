from unittest import TestCase
from part1_1 import country_filter
from part1_2 import unical_id
from part1_3 import max_stats

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