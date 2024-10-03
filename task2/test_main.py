import requests 
from config.config import TOKEN

class TestYandexDisk:
    def setup_method(self):
        self.headers = {'Authorization': TOKEN}

    
    def test_create_folder(self, param, value, status):
        params = {param:value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=self.headers, params=params)
        try:
            assert response.status_code == status
            print(f"Тест пройден успешно, статус ответа: {response.status_code}")
            if response.status_code == 201:
                print (f'Папка {value} успешно создана')
            elif response.status_code == 400:
                print ('Ошибка в параметрах запроса')
            elif response.status_code == 409:
                print ('Папка с таким именем уже существует')
        except AssertionError as e:
           print(f"Тест провален, статус ответа: {response.status_code}")
           if response.status_code == 409:
                print ('Папка с таким именем уже существует')
           elif response.status_code == 400:
                print ('Ошибка в параметрах запроса')

test1 = TestYandexDisk()
test1.setup_method()

test1.test_create_folder('path','Image',201)
test1.test_create_folder('pat','Image',201)    
test1.test_create_folder('path','Image',409)       