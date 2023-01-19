# from unittest import TestCase
from part1_2 import unical_id

def test_equal_unical_id(self):
    set_id = {
        'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}
    ok_id = [98, 35, 15, 213, 54, 139]
    res = unical_id(set_id)
    assert res == ok_id


