# from unittest import TestCase
# from selenium import webdriver
# from time import sleep

# class TestLogin(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.browser = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
#         cls.browser.get('http://35.225.243.133/admin/')

#     def test_login(self):
#         self.browser.find_element_by_css_selector('#id_username').send_keys('student_all')
#         self.browser.find_element_by_css_selector('#id_password').send_keys('qatester')
#         self.browser.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()
#         expected_link = 'http://35.225.243.133/admin/'
#         actual_link = self.browser.current_url
#         assert expected_link == actual_link
#         expected_title = 'Student Tasks Administration | Student Tasks Administration'
#         actual_title = self.browser.title 
#         assert expected_title == actual_title

#         expected_username = 'student_all'
#         actual_username = self.browser.find_element_by_css_selector('#user-tools > ul > li.user-tools-welcome-msg').text

#         assert expected_username == actual_username

#     @classmethod
#     def tearDownClass(cls):
#         sleep(3)
#         cls.browser.close()

    