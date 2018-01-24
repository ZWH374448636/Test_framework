"""项目需要的浏览器和网址的类统一封装在一起"""

import time,os
from selenium import webdriver
from utils.config import DRIVER_PATH,REPORT_PATH

#各浏览器的驱动路径，可根据项目需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
FIREFOXDRIVER_PATH = DRIVER_PATH+ '\geckodriver.exe'

#各浏览器类型

