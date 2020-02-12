from selenium.webdriver.common.by import By
from pageobjects.confirm_page import ConfirmPage


class CheckoutPage:
	def __init__(self, browser):
		self.browser = browser

	card_title = (By.CSS_SELECTOR, '.card-title a')
	card_footer = (By.CSS_SELECTOR, '.card-footer button')
	checkout = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')

	def get_card_titles(self):
		return self.browser.find_elements(*CheckoutPage.card_title)

	def get_card_footers(self):
		return self.browser.find_elements(*CheckoutPage.card_footer)

	def get_checkout_items(self):
		self.browser.find_element(*CheckoutPage.checkout)
		confirm_page = ConfirmPage(self.browser)
		return confirm_page

