from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:

    def __init__(self) -> None:
        self._options = ChromeOptions() 
        self.headers()
        self.driver: WebDriver = Chrome(options=self._options) 

    def headers(self) -> None:
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        self._options.headless = True
        self._options.add_argument(f'user-agent={self.user_agent}')
        self._options.add_argument("--window-size=1920,1080")
        self._options.add_argument('--ignore-certificate-errors')
        self._options.add_argument('--allow-running-insecure-content')
        self._options.add_argument("--disable-extensions")
        self._options.add_argument("--proxy-server='direct://'")
        self._options.add_argument("--proxy-bypass-list=*")
        self._options.add_argument("--start-maximized")
        self._options.add_argument('--disable-gpu')
        self._options.add_argument('--disable-dev-shm-usage')
        self._options.add_argument('--no-sandbox')    