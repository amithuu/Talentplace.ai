import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:


    def loginpage(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://test-talentplace.vercel.app/")

        # Pop-up of WorkShop CLose 'X' mark.
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//button[@aria-label='Close']"))).click()

        # Login Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()

        # Login Page
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys("amithkulkarni98@gmail.com")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)


ref = LoginPage()
ref.loginpage()


