import sys
import os

# Get the directory of the current script
current_path = os.path.dirname(os.path.abspath(__file__))

# Construct the path of the target directory that needs to be added to sys.path
# Assuming 'my_selenium_project' is the directory name of the target project
my_selenium_project_path = os.path.join(current_path, '..', 'my_selenium_project')

# Add to sys.path
sys.path.append(my_selenium_project_path)

from helpers.proxy_handler import ProxyHandler
from helpers.webdriver_setup import WebDriverSetup
from helpers.har_handler import HarHandler
from src.data.data_class import headers_to_set
from src.data.data_class import the_path_to_browsermob_proxy

class dataHandler:
    def __init__(self, test_page):
        # Set the path to the BrowserMob proxy binary
        path_to_browsermob_proxy = the_path_to_browsermob_proxy

        # Initialize the ProxyHandler
        self.proxy_handler = ProxyHandler(path_to_browsermob_proxy)

        # Set the header to the BrowserMob proxy binary
        headers = headers_to_set

        # Initialize the ProxyHandler
        self.proxy_handler.set_request_interceptor(headers)

        # Start capturing HAR data
        target_url = "https://api.segment.io/v1/t" 
        self.proxy_handler.start_har_capture()

        # Initialize the WebDriverSetup with the proxy from ProxyHandler
        webdriver_setup = WebDriverSetup(self.proxy_handler.proxy)

        # Get the WebDriver instance
        self.driver = webdriver_setup.get_driver()

        # Navigate to the page you want to test
        self.driver.get(test_page)  

        # Wait for the specific request to be captured using HarHandler
        timeout_sec = 10  # Set your timeout in seconds
        self.har_data = HarHandler.poll_har_data(self.proxy_handler.proxy, target_url, timeout_sec)

    def get_har_data(self):
        return self.har_data
    
    def close_driver(self):
        self.driver.quit()
    
    def close_proxy(self):
        self.proxy_handler.stop()