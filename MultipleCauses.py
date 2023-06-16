import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
email = "sozolebur@mailinator.com"
password = "New@1234"
class Causes():

    def login(self):
        driver.get("https://www.talentplace.ai/login")

        # driver.get("https://test-talentplace.vercel.app/login")
        driver.maximize_window()
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        edit_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        edit_profile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Causes']")))
        exp.click()
    def causes(self):
        time.sleep(4)
        """Causes"""
        # Select The Causes Max[6]
        for i in range(1, 7):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div[{i}]//span[1]"))).click()
            time.sleep(1)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div/button")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)


ref = Causes()
ref.login()
ref.causes()

