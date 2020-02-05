from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pytest import fixture


def pytest_addoption(parser):
	parser.addoption("--browser_name", action="store", default="chrome")


@fixture(scope='class')
def setup(request):
	browser_name = request.config.getoption('browser_name')

	if browser_name == 'chrome':
		browser = webdriver.Chrome(executable_path='/Users/ddinevich/dev/seleniumeasy/drivers/chromedriver')
	elif browser_name == 'firefox':
		browser = webdriver.Firefox(executable_path='/Users/ddinevich/dev/seleniumeasy/drivers/geckodriver')

	browser.get('https://www.rahulshettyacademy.com/angularpractice/')
	request.cls.browser = browser
	yield
	browser.close()
