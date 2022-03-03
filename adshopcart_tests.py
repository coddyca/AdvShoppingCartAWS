import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdvantageShoppingAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_main_advantage_shopping():
        methods.setUp()
        methods.sign_up()
        methods.checks_full_name()
        methods.check_orders()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.delete_test_account()
        methods.tearDown()