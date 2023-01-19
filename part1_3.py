def max_stats(dict_x):
    maximum = max(dict_x.values())
    for name, sales in dict_x.items():
        if sales == maximum:
            champion = name
    return champion

def test1_3():

    stats = {'facebook': 55, 'yandex': 10, 'vk': 315, 'google': 199, 'email': 242, 'ok': 98}
    cx = 'vk'

    assert max_stats(stats) == cx

if __name__ == '__main__':
    test1_3()