#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=opts)