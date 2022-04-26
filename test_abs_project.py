from selenium import webdriver
import time
import unittest
import pytest

class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)

            # Ваш код, который заполняет обязательные поля
        line_1 = browser.find_element_by_css_selector('input.first:required')
        line_1.send_keys('kek')
        line_2 = browser.find_element_by_css_selector('input.second:required')
        line_2.send_keys('kek')
        line_3 = browser.find_element_by_css_selector('input.third:required')
        line_3.send_keys('kek')
            # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
        time.sleep(1)

            # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == 'Congratulations! You have successfully registered!', 'test1'

            # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
            # закрываем браузер после всех манипуляций
        browser.quit()
    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)

            # Ваш код, который заполняет обязательные поля
        line_1 = browser.find_element_by_css_selector('input.first:required')
        line_1.send_keys('kek')
        line_2 = browser.find_element_by_css_selector('input.second:required')
        line_2.send_keys('kek')
        line_3 = browser.find_element_by_css_selector('input.third:required')
        line_3.send_keys('kek')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
        time.sleep(1)

            # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == 'Congratulations! You have successfully registered!', 'test2'

            # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
            # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    pytest.main()