from unittest import TestCase
from selenium import webdriver

class TestLogin(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
        cls.browser.get('http://35.225.243.133/admin/')
        cls.browser.find_element_by_css_selector('#id_username').send_keys('student_all')
        cls.browser.find_element_by_css_selector('#id_password').send_keys('qatester')
        cls.browser.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()
        

    def test_product_click(self):
        self.browser.find_element_by_css_selector('#content > div.dashboard-container.columns_3.cf > div:nth-child(2) > div > div:nth-child(1) > div.dashboard-item-content > ul > li:nth-child(2) > a').click()
        expected_link = 'http://35.225.243.133/admin/products/product/'
        actual_link = self.browser.current_url
        assert expected_link == actual_link
        

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()

    