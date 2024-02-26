from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverSetup:
    def __init__(self, proxy):
        options = webdriver.ChromeOptions()
        options.add_argument(f"--proxy-server={proxy.proxy}")
        options.add_argument("--ignore-certificate-errors")
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        return self.driver

    def quit(self):
        self.driver.quit()