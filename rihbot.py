import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    def loginpage(self):
        self.driver.get("https://rigbot.com/")

        # # Pop-up of WorkShop CLose 'X' mark.
        # # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//button[@aria-label='Close']"))).click()
        # main = self.driver.current_window_handle
        # Login Button
        # WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        log =self.driver.execute_script("return document.getElementsByTagName('a')[11];")
        self.driver.execute_script("arguments[0].click();", log)
        time.sleep(10)

        # wind = self.driver.current_window_handle
        # if self.driver.current_window_handle != main:
        #     self.driver.switch_to.window(wind)
        # Login Page
        self.driver.find_element(By.NAME, 'username').send_keys("amith")
        self.driver.find_element(By.NAME, 'password').send_keys("kulkarni")
        self.driver.find_element(By.XPATH, "//button[text()='Log In']").click()
        time.sleep(3)


ref = LoginPage()
ref.loginpage()