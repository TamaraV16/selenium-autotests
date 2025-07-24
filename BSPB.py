import string
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service())
#driver.set_window_size(1024,768)

print("C2210: Вход с валидными данными")
try:
    driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("demo")
    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys("demo")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "login-otp-button").click()
    if driver.find_element(By.ID, "logout-button"):
        print("\033[92m{}\033[0m".format("TestPASS"))
    driver.save_screenshot("sc_C2210.png")
except:
    driver.save_screenshot("error_cs_C2210.png")
    print("\033[31m{}\033[0m".format("TestFAIL"))

driver.quit()


