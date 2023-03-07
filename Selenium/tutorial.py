from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service("/home/cassius/Downloads/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(30)

for i in range(5000):
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")

    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1,-1,-1)]

    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()