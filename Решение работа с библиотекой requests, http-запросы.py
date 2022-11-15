# # # Задание №1

import requests
heroes_list = ['Hulk', 'Captain America', 'Thanos']
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
characteristics_heroes = resp.json()

ig_list = []
for heroes_1 in characteristics_heroes:
    for heroes_2 in heroes_list:
        if heroes_2 == heroes_1['name']:
            ig_list.append(heroes_1['powerstats']['intelligence'])

for heroes_3 in characteristics_heroes:
    for heroes_4 in heroes_list:
        if heroes_4 == heroes_3['name']:
            if heroes_3['powerstats']['intelligence'] == max(ig_list):
                print(f"Cамый умный: {heroes_3['name']} с интеллектом {str(heroes_3['powerstats']['intelligence'])}")

# # # Задание №2
HTTPS_STATUS_CREATE:int = 201
TOKEN = "" #Вставьте токен
class YaUploader:
    URL_UPLOAD_LINK: str = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            "Content_Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }
    def get_upload_link(self, ya_disk_path:str):
        params = {"path": ya_disk_path, "overwrite": "true"}
        resource = requests.get(self.URL_UPLOAD_LINK, params=params, headers=self.header)
        upload_url = resource.json().get("href")
        return upload_url
    def upload_file(self, ya_disk_path:str , file_path:str):
        upload_link = self.get_upload_link(ya_disk_path)
        with open(file_path, "rb") as file_obj:
            responce = requests.put(upload_link, data=file_obj)
            if responce.status_code == HTTPS_STATUS_CREATE:
                print("\nЗагрузка файла на ЯндексДиск прошла успешно!!!\n")
        return responce.status_code

if __name__ == '__main__':
    instance = YaUploader(TOKEN)
    instance.upload_file('/1.txt', "1.txt")
