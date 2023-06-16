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
titles = ["voluntaryroles1", "voluntaryroles2", "voluntaryroles3"]
issuers = ["Reva", "BMSIT", "ISCIT"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
associatedwith = ["cognizant", "dell", "ibm"]
descriptions = ["hiii i am writing description about my voluntaryroles 1", "hiii i am writing description about my voluntaryroles 2", "hiii i am writing description about my voluntaryroles 3"]

class HonorAwards():

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

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Honors & Awards']")))
        exp.click()
    def honorawards(self):
        for i in range(3):
            # Add voluntary_roles
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"))).click()
            time.sleep(1)
            """Voluntary_Roles"""
            # Title
            title = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]//input")
            title.send_keys(titles[i])

            # Issuer
            issuer = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]//input")))
            issuer.send_keys(issuers[i])

            duration_from = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//input")))
            duration_from.send_keys(startyear[i])
            duration_from.send_keys(Keys.TAB)
            duration_from.send_keys(startyear[i])

            # Associated With
            associated_with = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//input")))
            associated_with.send_keys(associatedwith[i])
            associated_with.send_keys(Keys.TAB)

            # Description
            description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]//p")))
            description.send_keys(descriptions[i])

            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button")))
            save.click()
            time.sleep(3)

            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()

            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)


ref = HonorAwards()
ref.login()
ref.honorawards()

