from unittest import TestCase
from selenium import webdriver

class TestProductList(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
        cls.browser.get('http://35.225.243.133/admin/')
        cls.browser.find_element_by_css_selector('#id_username').send_keys('student_all')
        cls.browser.find_element_by_css_selector('#id_password').send_keys('qatester')
        cls.browser.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()
        cls.browser.get('http://35.225.243.133/admin/products/product/')
    
    def test_product_column_text(self):
        expected_text = 'PRODUCT'
        actual_text = self.browser.find_element_by_css_selector('#result_list > thead > tr > th.column-__str__ > div.text > span').text
        assert expected_text == actual_text

    def test_add_product_text(self):
        expected_text = 'Add product'
        actual_text = self.browser.find_element_by_css_selector('#content-main > ul > li > a').text
        assert expected_text == actual_text

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()