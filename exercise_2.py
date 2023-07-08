import requests
from xxx import Token

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        '''Метод загружает файлы по списку file_list на яндекс диск'''
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Accept': 'application/json', 'Authorization': token}
        params = {'path': file_path}
        url_uploader = requests.get(url, headers=headers, params=params).json()['href']
        response = requests.put(url_uploader, data=open(file_path, 'rb'))
        print(response.status_code)
      
        
if __name__ == '__main__':
    path_to_file = 'crow.jpg'
    token = Token()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)