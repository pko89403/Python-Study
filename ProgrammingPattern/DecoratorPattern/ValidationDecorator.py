from urllib.parse import urljoin
import urllib3 
from urllib3.exceptions import HTTPError

def response_ok(func):
    def validate(*args, **kwargs):
        result = func(*args, **kwargs)
        if result.status != 200:
            raise HTTPError(f"Request Failed with status code {result.status}")
            return result 
        return validate 

@response_ok
def fetch(path):
    with urllib3.PoolManager() as http:
        return http.request('GET', path)

if __name__ == "__main__":
    api = 'http://httpbin.org'
    url = urljoin(api, 'ip') # 존재하는 URL. 200 Response
    wrong_url = urljoin(api, 'pi') # 존재하지 않는 URL. 404 Response
    fetch(url).data.decode()
    fetch(wrong_url).data.decode()