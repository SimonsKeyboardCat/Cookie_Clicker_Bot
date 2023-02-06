from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# cookie clicker using selenium
chrome_driver_path = "C:\Development\chromedriver.exe" # Your chromedriver path
url = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

cookie = driver.find_element(by=By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

game_timeout = time.time() + 10*60
upgrade_timeout = time.time() + 5

while True:
    cookie.click()

    if time.time() > upgrade_timeout:
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, _id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = _id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        upgrade_timeout = time.time() + 5

    if time.time() > game_timeout:
        cookie_per_sec = driver.find_element(by=id, value="cps").text
        print(cookie_per_sec)




