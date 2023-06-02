import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec\


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
email = "autotest64@g.co"
password = "New@1234"
certificate_title= ["My Certificate 1", "My Certificate 2", "My Certificate 3"]
institutions = ["Reva", "Isam", "Revam"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
endmonth = ["feb", "april", "jan"]
endyear = ["2019", "2020", "2021"]
skilladd = ["java", "python", "c prog"]
projects = ["hiii i am writing description about my Certificate 1", "hiii i am writing description about my Certificate 2", "hiii i am writing description about my Certificate 3"]
class Certificate():

    def login(self):
        driver.get("https://test-talentplace.vercel.app/login")
        driver.maximize_window()
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        editprofile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        editprofile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Certification']")))
        exp.click()
    def certificate(self):
        for i in range(3):
            """Certificate"""
            # Add Certificate
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button[1]"))).click()
            time.sleep(1)
            # Title
            title = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]//input")))
            title.send_keys(certificate_title[i])
            # Institution
            institution = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]//input")
            institution.send_keys(institutions[i])
            # Duration from
            duration_from = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//input")
            duration_from.send_keys(startmonth[i])
            duration_from.send_keys(Keys.TAB)
            duration_from.send_keys(startyear[i])
            # Duration to
            duration_to = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//input")
            duration_to.send_keys(endmonth[i])
            duration_to.send_keys(Keys.TAB)
            duration_to.send_keys(endyear[i])
            # Skill add
            skill = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]//input")))
            skill.send_keys(skilladd[i])
            skill.send_keys(Keys.TAB)
            # Add Skill '+' Button
            driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]//button").click()

            # Projects Description
            project_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]//p")))
            project_description.send_keys(" This is certification description ")
            time.sleep(1)
            # # Upload Certificate
            # upload_certificate = driver.execute_script(f"return document.getElementsByTagName('u')[{i}];")
            # driver.execute_script("arguments[0].click();", upload_certificate)
            # time.sleep(5)
            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button")))
            save.click()
            time.sleep(4)

            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()
            time.sleep(2)

            # # Discard
            # discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
            # discard.click()
            # time.sleep(2)

            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)


ref = Certificate()
ref.login()
ref.certificate()