import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
email = "prod2@g.co"
password = "New@1234"
degreequalification = ["Mca", "BCA", "Mtech"]
universitys = ["REVA UNI", "seshadri", "presid"]
locations = ["Bangalore", "delhi", "american"]
Cgpas= ["8.98", "7.65", "5.09"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
endmonth = ["feb", "april", "jan"]
endyear = ["2019", "2020", "2021"]
skilladd = ["java", "python", "c prog"]
extraactivities = ["!!!!!!!!!!I love playing Cricket!!!!!!!!", "!!!!!!!!!!!!!I love Watching Cricket!!!!!!!", "!!!!!!!!!!!I love Cricket that it!!!!!!!!"]
class Education:

    def login(self):
        # driver.get("https://test-talentplace.vercel.app/login")
        driver.get("https://talentplace.ai/login")
        driver.maximize_window()

        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        edit_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        edit_profile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Education']")))
        exp.click()

    def education(self):
        for i in range(3):
            # Add Education
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button[1]"))).click()
            time.sleep(2)
            """ADD EDUCATION"""
            # Degree
            degree = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[1]//input")))
            degree.send_keys(degreequalification[i])
            degree.send_keys(Keys.TAB)
            # University
            university = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input")))
            university.send_keys(universitys[i])
            university.send_keys(Keys.TAB)
            # Location
            loc = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input")))
            loc.send_keys(Keys.CONTROL + "a")
            loc.send_keys(locations[i])
            loc.send_keys(Keys.BACK_SPACE)
            time.sleep(5)
            # CGPA
            cgpa = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input")))
            cgpa.send_keys(Cgpas[i])
            # Duration from
            duration_from = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]//input")
            duration_from.send_keys(startmonth[i])
            duration_from.send_keys(Keys.TAB)
            duration_from.send_keys(startyear[i])
            # Duration to
            duration_to = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[2]//input")
            duration_to.send_keys(endmonth[i])
            duration_to.send_keys(Keys.TAB)
            duration_to.send_keys(endyear[i])
            # Currently Pursuing
            # currently_pursuing = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/label//span")))
            # currently_pursuing.click()
            # time.sleep(3)
            # Project Description
            project_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p")))
            project_description.send_keys(f" This is my Project in {universitys[i]} ")
            time.sleep(1)
            # Extra Circular Activities
            extra_circular_activities = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]//p")))
            extra_circular_activities.send_keys(extraactivities[i])
            time.sleep(1)
            # # Click to Upload Image
            click_upload_image = driver.execute_script("return document.getElementsByTagName('u')[0]")
            driver.execute_script("arguments[0].click();", click_upload_image)
            time.sleep(5)

            # Save
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/button"))).click()
            time.sleep(5)

            # Back
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            next_.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            # # Discard
            # discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
            # discard.click()
            # time.sleep(2)


ref = Education()
ref.login()
ref.education()