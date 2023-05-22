# Todo: here the flow is User logs in and
#  takes assessment and checks his personality review!!!!
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains,Keys

class NewUser1:

    def newuser1(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://test-talentplace.vercel.app/")
        # driver.maximize_window()

        # Login Button
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        pagedown = driver.find_element(By.TAG_NAME, value="body")

        # """ Login Page"""

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(
            "qazawej@mailinator.com.com")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        # Welcome page/get started/next/checkbox[start]/
        # Get started Button for Assessment Start Link
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/button"))).click()
        time.sleep(3)

        pagedown.send_keys(Keys.PAGE_DOWN)
        pagedown.send_keys(Keys.PAGE_DOWN)
        pagedown.send_keys(Keys.PAGE_DOWN)

        # Get started Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Get Started']"))).click()
        time.sleep(2)

        pagedown.send_keys(Keys.PAGE_DOWN)
        pagedown.send_keys(Keys.PAGE_DOWN)
        pagedown.send_keys(Keys.PAGE_DOWN)

        # next button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Next']"))).click()
        time.sleep(3)

        pagedown.send_keys(Keys.PAGE_DOWN)
        pagedown.send_keys(Keys.PAGE_DOWN)
        pagedown.send_keys(Keys.PAGE_DOWN)

        # Check box and Start test
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))).click()
        # try:
        #     check = driver.execute_script(" return document.getElementsByClassName('chakra-checkbox__input')")
        #     driver.execute_script("arguments[0].click();", check)
        #     time.sleep(2)
        #     WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']//button"))).click()
        #     time.sleep(2)
        # finally:
        #     driver.get("https://test-talentplace.vercel.app/assessment/details")
        #     time.sleep(3)

        # If user already Logged In.
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Take Assessment']"))).click()

        driver.get("https://test-talentplace.vercel.app/assessment/details")
        time.sleep(3)

        # Click on Answers
        for i in range(1, 10):
            for j in range(1, 6):
                WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@class='css-h2q039']/p[{j}]"))).click()
                time.sleep(1)
            time.sleep(1)

        # Click on submit
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Submit']"))).click()
        time.sleep(15)

        # Click on view Report
        pagedown.send_keys(Keys.PAGE_DOWN)
        pagedown.send_keys(Keys.PAGE_DOWN)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='View Report']"))).click()

# "Personality Assessment"
        # Click on Carrier Strength
        carrier_strength = driver.execute_script("return document.getElementsByTagName('a')[3];")
        driver.execute_script("arguments[0].click();", carrier_strength)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(2)

        for i in range(1, 7):
            WebDriverWait(driver, 20).until(
                ec.element_to_be_clickable((By.XPATH, f"//*[@role='tablist']//button[{i}]"))).click()
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
            time.sleep(2)

        # Click on Upgrade Button
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@tabindex='0' and @role='tabpanel' ]/div/div[3]//button"))).click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

        # Click on Carrier Options
        carrier_options = driver.execute_script("return document.getElementsByTagName('a')[4];")
        driver.execute_script("arguments[0].click();", carrier_options)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(2)

        # CLick on Resume Improvements
        resume_improvements = driver.execute_script("return document.getElementsByTagName('a')[5];")
        driver.execute_script("arguments[0].click();", resume_improvements)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(2)

        # CLick on Interview Questions
        interview_questions = driver.execute_script("return document.getElementsByTagName('a')[6];")
        driver.execute_script("arguments[0].click();", interview_questions)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(2)

        # CLick on Leadership Potential
        leadership_potential = driver.execute_script("return document.getElementsByTagName('a')[7];")
        driver.execute_script("arguments[0].click();", leadership_potential)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(2)

        # CLick on Self Development
        self_development = driver.execute_script("return document.getElementsByTagName('a')[8];")
        driver.execute_script("arguments[0].click();", self_development)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(2)

        # click on Overview
        overview = driver.execute_script("return document.getElementsByTagName('a')[2];")
        driver.execute_script("arguments[0].click();", overview)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
        time.sleep(2)


ref = NewUser1()
ref.newuser1()