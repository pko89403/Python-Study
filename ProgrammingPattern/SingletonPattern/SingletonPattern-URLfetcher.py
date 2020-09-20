import urllib.parse
import urllib.request

class SingletonType(type):
    _instance = {}
    # 함수를 호출하는 것처럼 클래스의 객체도 호출할 수 있게 만들어주는 매직 메소드가 __call__ 이다.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class URLFetcher(metaclass= SingletonType):
    def __init__(self):
        self.urls = [] 
    
    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)

                urls = self.urls
                urls.append(url)
                self.urls  = urls 
    
    def dump_url_registry(self):
        return ', '.join(self.urls)

def main():
    MY_URLS = ['http://www.voidspace.org.uk', 
               'http://google.com', 
               'http://python.org',
               'https://www.python.org/error',
               ]

    print(URLFetcher() is URLFetcher())

    fetcher = URLFetcher()
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)

    print('-------')
    done_urls = fetcher.dump_url_registry()
    print(f"Done URLs : {done_urls}")    

if __name__ == "__main__":
    main()