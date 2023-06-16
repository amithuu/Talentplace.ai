import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
email = "autotest64@g.co"
password = "New@1234"

class CarrierSummary:

    def login(self):
        driver.get("https://test-talentplace.vercel.app/login")
        driver.maximize_window()
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        edit_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        edit_profile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Cognitive Skills']")))
        exp.click()
    def carrier_summary(self):
        """ADD CARRIER SUMMARY"""
        # Generate Summary
        driver.set_window_size(1200, 1400)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        generate_suggestion = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[text()='Generate Suggestions']")))
        generate_suggestion.click()
        time.sleep(12)
        for a in range(1, 4):
            driver.find_element(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div{a}//button").click()
            time.sleep(1)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(4)


ref = CarrierSummary()
ref.carrier_summary()
