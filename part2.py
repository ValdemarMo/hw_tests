# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты,
# проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и
# возможные отрицательные тесты на ответы с ошибкой
# Пример положительных тестов:
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

import json
import vk_c
import yadisk_c

with open('token_vk.txt', 'r') as file_object:
    token_vk = file_object.read().strip()
with open('token_y.txt', 'r') as file_object:
    token_y = file_object.read().strip()

vk = vk_c.VkUser(token_vk)
target_user = 'none'

while target_user != True:
    target_user = input(f'\nвведите id или screen_name пользователя vk: ')
    target_user = vk.get_user_id(target_user)
    if target_user: break
    print(f'\nпопробуйте ещё раз')

target_album = 'profile'  # варианты: profile , saved, wall
# target_album = input(f'\nвыберите фото-альбом (profile , saved, wall): ')
count_photos = int(input(f'\nвыберите количество фотографий: '))

folder_name = 'VK' + str(target_user)
data_file_name = 'info.json'
file_path = '/' + folder_name + '/' + data_file_name

vk_plist = vk.get_photo_list(target_album, count_photos, target_user)

yadisk = yadisk_c.YaDisk(token_y)
print(f'создаем на Yandex Диске \nпапку для хранения фотографий\
    \n[{folder_name}] \n')
yadisk.create_folder(folder_name)

info_list = []
for n in vk_plist:
    id_n = n['photo_id']
    likes_n = n['likes']
    size_n = n['size']
    url_n = n['url']
    name_n = 'id' + str(id_n) + '_(' + str(likes_n) + '-likes)' + '.jpg'
    path_n = '/' + folder_name + '/' + name_n
    print('сохраняем фото', name_n)
    yadisk.upload_url_to_disk(path_n, url_n)
    info_list.append({'file_name': name_n, 'size': str(size_n)})

print(f'\nформируем файл отчета', data_file_name)
with open(data_file_name, "w") as info_x:
    info_x.write(json.dumps(info_list))
    info_x.close()

print(f'\nдобавляем файл на Yandex Диск')
yadisk.upload_file_to_disk(file_path, data_file_name)
print(f'\nвсе файлы записаны')


from lib2to3.pgen2 import token
import requests
from pprint import pprint
import os.path
import json

with open('access_token.txt', 'r') as file_object:
    token = file_object.read().strip()


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_photos(self, vk_id):
        # Получение фотографии с профиля с использованием метода photos.get

        photos_get_url = self.url + 'photos.get'

        params = {
            'owner_id': vk_id,
            'album_id': 'profile',
            'rev': 0,
            'extended': 1,
            'photo_sizes': 0,
            'count': 20
        }
        res = requests.get(photos_get_url, params={**self.params, **params}).json()
        profile_list = res['response']['items']
        for i in profile_list:
            dict = (i['sizes'][-1])
            photo_url = (dict['url'])
            file_name = i['likes']['count']
            download_photo = requests.get(photo_url)
            with open(os.path.join('fotos', f'{file_name}.jpg'), 'wb') as file:
                file.write(download_photo.content)
        return "Фото скачены"


class YaUploader:
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, path):
        """Создание папки. \n path: Путь к создаваемой папке."""
        requests.put(f'{self.URL}?path={path}', headers=self.get_headers())

    def upload_file(self, loadfile, savefile, replace=False):
        """Загрузка файла.
        savefile: Путь к файлу на Диске
        loadfile: Путь к загружаемому файлу
        replace: true or false Замена файла на Диске"""
        res = requests.get(f'{self.URL}/upload?path={savefile}&overwrite={replace}', headers=self.get_headers()).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)

    def upload_photo(self, list_photo, path):

        logs_list = []

        for photo in list_photo:
            params = {'path': f'{path}/{photo}'}
            get_upload_url = requests.get(self.URL, headers=self.get_headers(), params=params).json()
            file_upload = requests.put(get_upload_url['href'], data=open(f'{path}/{photo}', 'rb'),
                                       headers=self.get_headers())
            status = file_upload.status_code

            download_log = {'file_name': photo}
            logs_list.append(download_log)

        with open('log.json', 'a') as file:
            json.dump(logs_list, file, indent=2)

        if 500 > status != 400:
            print('Фотографии успешно загружены!')
        else:
            print('Ошибка при загрузке фотографий')


def create_folder(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)


def get_photos_from_folder(folder) -> list:
    file_list = os.listdir(folder)
    return file_list


if __name__ == '__main__':
    create_folder('fotos')
    vk_client = VkUser(token, '5.131')
    pprint(vk_client.get_photos('552934290'))
    file_list = get_photos_from_folder('fotos')
    token = ''
    yadisk = YaUploader(token)
    yadisk.create_folder('fotos')
    # yadisk.upload_file(r'fotos\\10.jpg', 'foto