from unittest import TestCase
from selenium import webdriver
from time import sleep

class TestLogin(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
        cls.browser.get('http://35.225.243.133/admin/')

    def test_login(self):
        self.browser.find_element_by_css_selector('#id_username').send_keys('student_all')
        self.browser.find_element_by_css_selector('#id_password').send_keys('qatester')
        self.browser.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()
        expected_link = 'http://35.225.243.133/admin/'
        actual_link = self.browser.current_url
        assert expected_link == actual_link
        expected_title = 'Student Tasks Administration | Student Tasks Administration'
        actual_title = self.browser.title 
        assert expected_title == actual_title

        expected_username = 'student_all'
        actual_username = self.browser.find_element_by_css_selector('#user-tools > ul > li.user-tools-welcome-msg').text

        assert expected_username == actual_username

    def test_product_column_name(self):
        expected_name = 'products'
        actual_name = self.browser.find_element_by_css_selector('#content > div.dashboard-container.columns_3.cf > div:nth-child(2) > div > div:nth-child(1) > div.dashboard-item-content > ul > li.contrast > a').text

        assert expected_name == actual_name.lower()

    def test_product_row_name(self):
        expected_name = 'Products'
        actual_name = self.browser.find_element_by_css_selector('#content > div.dashboard-container.columns_3.cf > div:nth-child(2) > div > div:nth-child(1) > div.dashboard-item-content > ul > li:nth-child(2) > a').text

        assert expected_name == actual_name

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()

    