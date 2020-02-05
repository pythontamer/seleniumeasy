from pageobjects.home_page import HomePage
from pageobjects.checkout_page import CheckoutPage
from utilities.baseclass import BaseClass


class NewTest(BaseClass):
	def test_ete(self):
		home_page = HomePage(self.browser)
		home_page.shop_items().click()

		checkout_page = CheckoutPage(self.browser)
		cards = checkout_page.get_card_titles()
		i = -1
		for card in cards:
			i = i + 1
			card_text = card.text
			print(card_text)
			if card_text == 'Blackberry':
				checkout_page.get_card_footers()[i].click()

