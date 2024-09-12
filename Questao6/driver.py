from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def Chrome() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-pipe")
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)


def Firefox() -> WebDriver:
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)
