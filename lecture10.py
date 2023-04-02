# 1. Открыть страницу http://google.com/ncr
# 2. Выполнить поиск слова “selenide”
# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
# 4. Перейти в раздел поиска изображений
# 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
# 6. Вернуться в раздел поиска Все
# 7. Проверить, что первый результат такой же, как и на шаге 3.

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')

    def test_search(self):
        # 1. Открыть страницу http://google.com/ncr
        self.drv.get('http://google.com/ncr')
        time.sleep(3)
        assert 'Google' in self.drv.title

        # 2. Выполнить поиск слова “selenide”
        elm = self.drv.find_element(By.NAME, 'q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        time.sleep(1)

        # 3. Проверить, что первый результат – ссылка на сайт selenide.org.
        all_results = self.drv.find_elements(By.XPATH,
                                             '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite')
        for result in all_results:
            print(f"All, First component: {result.text}")
            assert "selenide.org" in result.text

        # 4. Перейти в раздел поиска изображений
        self.drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        time.sleep(1)

        # 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        image_result = self.drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]/div/div')
        print(f"Images, First component: {image_result.text}")
        assert "selenide.org" in image_result.text

        # 6. Вернуться в раздел поиска Все
        self.drv.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
        time.sleep(5)

        # 7. Проверить, что первый результат такой же, как и на шаге 3.
        all_results = self.drv.find_elements(By.XPATH,
                                             '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite')
        for result in all_results:
            print(f"All, First component: {result.text}")
            assert "selenide.org" in result.text

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
