# from unittest import TestCase
# from selenium import webdriver
# from time import sleep

# class TestBeforeLogin(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.browser = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
#         cls.browser.get('http://35.225.243.133/admin/')
    
#     def test_login_url(self):
#         expected='http://35.225.243.133/admin/login/?next=/admin/'
#         actual = self.browser.current_url
#         assert expected == actual
    
#     def test_username_input(self):
#         assert self.browser.find_element_by_css_selector('#id_username')
    
#     def test_password_input(self):
#         assert self.browser.find_element_by_css_selector('#id_password')
    
#     def test_login_btn(self):
#         assert self.browser.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]')
    
#     def test_login_btn_text(self):
#         expected = 'Log in'
#         actual = self.browser.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').get_attribute('value')
#         assert expected == actual


#     @classmethod
#     def tearDownClass(cls):
#         sleep(3)
#         cls.browser.close()

    