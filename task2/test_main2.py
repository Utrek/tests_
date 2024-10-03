import pytest
import requests 

class TestYandexDisk:
    def setup_method(self):
        self.headers = {'Authorization':'OAuth y0_AgAAAAAqeAwuAADLWwAAAAD0Wukw2aj3ttNZQk2NBLxrFcmwRs8bDno'}

    @pytest.mark.parametrize ('param,value,status',
                              (['path','Image',201],
                               ['patn','Image',400],
                               ['path','Image',409]))
    def test_create_folder(self, param, value, status):
        params = {param:value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=self.headers, params=params)
        assert response.status_code == status
            