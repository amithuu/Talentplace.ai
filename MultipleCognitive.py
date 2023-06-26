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

class Cognitive:

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
    def cognitive(self):
        time.sleep(4)
        """Cognitive skills"""
        for s in range(1, 7):
            driver.find_element(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[{s}]//span[1]").click()
            slid = driver.find_element(By.XPATH,f"//*//*[@id='root']/div[2]/div[2]/div/div/div/div/div[{s}]//div[@role='slider']")
            ActionChains(driver).move_to_element(slid).pause(1).click_and_hold(slid).move_by_offset((35 * s), 0).release().perform()
            time.sleep(1)

        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(2)
        # Back
        next = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next.click()


ref = Cognitive()
ref.login()
ref.cognitive()
