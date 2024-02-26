from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def main(): 
    PROXY = "http://localhost:8080" # Mitmproxy运行的地址和端口

    options = webdriver.ChromeOptions()
    options.add_argument(f"--proxy-server={PROXY}")
    options.add_argument("--ignore-certificate-errors")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://qa-www.thebump.com")
    driver.quit()

if __name__ == "__main__":
    main()