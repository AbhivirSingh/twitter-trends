from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import uuid
from datetime import datetime
import config

# MongoDB setup
client = MongoClient(config.mongo)
db = client["twitter_trends"]
collection = db["trends"]

def fetch_twitter_trends(i):
    PROXYMESH_URL = f"http://{config.proxy_username}:{config.proxy_password}@{config.ips[i%len(config.ips)]}"
    options = webdriver.ChromeOptions()
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = PROXYMESH_URL
    proxy.ssl_proxy = PROXYMESH_URL

    options.add_argument('--proxy-server=%s' % PROXYMESH_URL)

    driver = webdriver.Chrome(service=Service(config.path), options=options)

    try:
        driver.get("https://x.com/i/flow/login")
        driver.maximize_window()
        WebDriverWait(driver,30).until(
            EC.presence_of_element_located((By.XPATH, '//input[@dir="auto"]'))
        )
        elem = driver.find_element(By.TAG_NAME, "input")
        elem.send_keys(config.mailId)
        elem.send_keys(Keys.RETURN)
        WebDriverWait(driver,60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.r-homxoj"))
        )



        # Use the below section, only if you have signed multiple times and now twitter.com is asking for username

        # elem = driver.find_element(By.CSS_SELECTOR, "input.r-homxoj")
        # elem.send_keys(config.twitter_username)
        # elem.send_keys(Keys.RETURN)
        # WebDriverWait(driver,10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "input.r-homxoj"))
        # )

        
        elem = driver.find_element(By.CSS_SELECTOR, "input.r-homxoj")
        elem.send_keys(config.twitter_password)
        elem.send_keys(Keys.RETURN)
        WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="trend"]'))
        )
        elems = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
        trend_names = []
        for i in range(len(elems)):
            elem = elems[i].find_elements(By.CSS_SELECTOR, "span.css-1jxf684")
            k = []
            for j in elem:
                k.append(j.text)
            trend_names.append(k)

        driver.get('https://api.ipify.org?format=json')
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.TAG_NAME,'pre'))
        )
        

        # Retrieve and print the IP address
        ip_address = eval(driver.find_element(By.TAG_NAME,'pre').text)['ip']


        # Generate unique ID and fetch IP
        unique_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to MongoDB
        data = {
            "unique_id": unique_id,
            "trend1": trend_names[0] if len(trend_names) > 0 else None,
            "trend2": trend_names[1] if len(trend_names) > 1 else None,
            "trend3": trend_names[2] if len(trend_names) > 2 else None,
            "trend4": trend_names[3] if len(trend_names) > 3 else None,
            "trend5": trend_names[4] if len(trend_names) > 4 else None,
            "ip_address": ip_address,
            "timestamp": timestamp
        }
        collection.insert_one(data)
        return data
    finally:
        driver.quit()