from unittest import TestCase
from selenium import webdriver
from time import sleep

class TestAddProduct(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
        cls.browser.get('http://35.225.243.133/admin/')
        cls.browser.find_element_by_css_selector('#id_username').send_keys('student_all')
        cls.browser.find_element_by_css_selector('#id_password').send_keys('qatester')
        cls.browser.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]').click()
        cls.browser.get('http://35.225.243.133/admin/products/product/')
    
    def test_add_product_click(self):
        self.browser.find_element_by_css_selector('#content-main > ul > li > a').click()
        expected_link = 'http://35.225.243.133/admin/products/product/add/'
        actual_link = self.browser.current_url
        assert expected_link == actual_link

    def test_save(self):
        self.select_owner()
        self.browser.find_element_by_css_selector('#id_title').send_keys('Product title')
        self.select_category()
        self.browser.find_element_by_css_selector('#id_description').send_keys('product desc')
        self.browser.find_element_by_css_selector('#id_price').send_keys('10.00')
        self.browser.find_element_by_css_selector('#id_discount_price').send_keys('1')
        self.browser.find_element_by_css_selector('#id_amount_by_unit').send_keys('1')
        self.browser.find_element_by_css_selector('#id_unit').send_keys('kq')
        self.browser.find_element_by_css_selector('#id_main_image').send_keys('/home/idris/PythonProjects/selenium_advanced/image/python.png')
        self.browser.find_element_by_css_selector('#product_form > div > div > input.default').click()


    def select_category(self):
        self.browser.find_element_by_css_selector('#select2-id_category-container').click()
        self.browser.find_element_by_css_selector('#select2-id_category-results>li:nth-child(2)').click()
    # def select_owner(self):
    #     self.browser.find_element_by_css_selector('#select2-id_owner-container').click()
    #     self.browser.find_element_by_xpath('//*[@id="select2-id_owner-results"]/*[contains(text(), "Aqil")]').click()

    def select_owner(self):
        self.browser.find_element_by_css_selector('#select2-id_owner-container').click()
        self.browser.find_element_by_css_selector('#select2-id_owner-results>li:nth-child(2)').click()


    # def select_owner(self):
    #     self.browser.find_element_by_css_selector('#select2-id_owner-container').click()
    #     options = self.browser.find_elements_by_class_name('select2-results__option')

    #     for option in options:
    #         if option.text == 'Aqil':
    #             option.click()
    #             break

    @classmethod
    def tearDownClass(cls):
        sleep(4)
        cls.browser.close()