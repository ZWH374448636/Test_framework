import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger
from utils.mail import Email
import time,os


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get(self.URL)

    def sub_setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)

    def test_search_0(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data = d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

    def test_search_1(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

    # def test_search_1(self):
    #     self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)

    # def tearDown(self):
    #     self.driver.quit()

    def sub_tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    now = time.strftime("%Y%m%d%H%M%S")
    filename = now + 'report.html'
    report = REPORT_PATH + '\\'+ filename   #拼接测试报告路径，加上生成测试报告时间
    # report = REPORT_PATH + '\\report.html'
    print(report)
    print(REPORT_PATH)
    with open(report,'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='文海测试学习报告')
        runner.run(TestBaiDu('test_search_0'))
    e = Email(server='smtp.126.com', sender='zwh2537@126.com', password='abc19891969', receiver='374448636@qq.com',
                  title='百度搜索测试报告-Chrome浏览器', message='zengwenhai',
              path=report)
    e.send()
    # unittest.main(verbosity=2)
    #
