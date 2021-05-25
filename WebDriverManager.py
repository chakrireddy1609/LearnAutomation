import openpyxl
from openpyxl import Workbook

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(5)
driver.find_element(By.NAME,"q").send_keys("iphone 11")
driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//button[contains(text(),'✕')]").click()
driver.find_element(By.XPATH,"//div[text()='APPLE']").click()
phone_names = driver.find_elements(By.XPATH,"//div[@class='_4rR01T']")
phone_prices = driver.find_elements(By.XPATH,"//div[@class='_30jeq3 _1_WHN1']")
phone_name_list = []
phone_price_list = []
for phone_name in phone_names:
    phone_name_list.append(phone_name.text)
for phone_price in phone_prices:
    phone_price_list.append(phone_price.text)

data = zip(phone_name_list,phone_price_list)


wb = Workbook()
wb['Sheet'].title = "Learn"
sh1 = wb.active
sh1.append(["Name","Price"])

for res in list(data):
    sh1.append(res)

wb.save("Flipkart.xlsx")







