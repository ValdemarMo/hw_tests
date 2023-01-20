from libX1.y import token
import requests

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

    def request_folder(self, path):
        request_f = requests.get(f'{self.URL}?path={path}', headers=self.get_headers())
        status = request_f.status_code
        print(status)
        return status


    def create_folder(self, path):
        create_f = requests.put(f'{self.URL}?path={path}', headers=self.get_headers())
        status = create_f.status_code
        print(status)
        return status

    def del_folder(self, path):
        del_f = requests.delete(f'{self.URL}?path={path}', headers=self.get_headers())
        status = del_f.status_code
        print(status)
        return status


# if __name__ == '__main__':
#     yadisk = YaUploader(token)
#     yadisk.create_folder('xxxxxxxxx')