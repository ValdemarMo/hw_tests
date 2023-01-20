def unical_id(set_x):
    geo_set = []
    for geo_user_set in set_x.values():
        geo_set += geo_user_set
    geo_set = set(geo_set)
    return geo_set

# def test1_2():
#
#     dx = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
#
#     rx = [98, 35, 15, 213, 54, 119]
#
#     assert list(unical_id(dx)) == rx
#
# if __name__ == '__main__':
#     test1_2()
