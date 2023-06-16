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

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
page_down = driver.find_element(By.TAG_NAME, value="body")
k = 15
email = f"autotest{k}@g.co"
class NewUser1:

    def newuser1(self):

        driver.get("https://test-talentplace.vercel.app/login")
        driver.maximize_window()
        # Login Button
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()

        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
        WebDriverWait(driver, 20).until( ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        # # Welcome page/get started/next/checkbox[start]/
        # # Get started Button for Assessment Start Link
        # WebDriverWait(driver, 20).until(
        #     ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/button"))).click()
        # time.sleep(3)
        #
        # page_down.send_keys(Keys.PAGE_DOWN)
        # page_down.send_keys(Keys.PAGE_DOWN)
        # page_down.send_keys(Keys.PAGE_DOWN)
        #
        # # Get started Button
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Get Started']"))).click()
        # time.sleep(2)
        #
        # page_down.send_keys(Keys.PAGE_DOWN)
        # page_down.send_keys(Keys.PAGE_DOWN)
        # page_down.send_keys(Keys.PAGE_DOWN)
        #
        # # next button
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Next']"))).click()
        # time.sleep(3)
        #
        # page_down.send_keys(Keys.PAGE_DOWN)
        # page_down.send_keys(Keys.PAGE_DOWN)
        # page_down.send_keys(Keys.PAGE_DOWN)
        #
        # # Check box and Start test
        # # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))).click()
        # # try:
        # #     check = driver.execute_script(" return document.getElementsByClassName('chakra-checkbox__input')")
        # #     driver.execute_script("arguments[0].click();", check)
        # #     time.sleep(2)
        # #     WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']//button"))).click()
        # #     time.sleep(2)
        # # finally:
        # #     driver.get("https://test-talentplace.vercel.app/assessment/details")
        # #     time.sleep(3)

        # driver.get("https://test-talentplace.vercel.app/assessment/details")
        # time.sleep(3)
    def take_assesment(self):
        # If user already Logged In.
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Take Assessment']"))).click()
        time.sleep(2)
        # Click on check Box
        time.sleep(3)
        check_box = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]//span")))
        check_box.click()
        # Start Test
        start_test = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]/div[1]/div/div[3]//button")))
        start_test.click()
        # Answers
        for i in range(1, 10):
            for j in range(1, 6):
                answer = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@id='root']/div/div[2]/div[1]/div[2]/div[2]//p[{j}]")))
                answer.click()
        # Click on submit
        submit = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[3]//button[2]")))
        submit.click()
        time.sleep(15)
        # Click on view Report
        view_report = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]//button")))
        view_report.click()
        time.sleep(5)
    def personality_assesment(self):
        """Personality Assessment"""
        # Overview
        # page_down.send_keys(Keys.PAGE_DOWN)
        # page_down.send_keys(Keys.PAGE_DOWN)
        # time.sleep(3)
        # page_down.send_keys(Keys.PAGE_UP)
        # page_down.send_keys(Keys.PAGE_UP)
        time.sleep(2)
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
            tablist = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@role='tablist']//button[{i}]")))
            tablist.click()
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
            driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
            time.sleep(2)
        # Click on Upgrade Button[//*[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div[{6}]/div/div[{3}]
        # //button]{1,6} for tabs and {3,4} for inside tabs change
        # Next and Previous
        # next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div[3]/a[2]//button")))
        # next_.click()
        # back_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div[3]/a[1]//button")))
        # back_.click()
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div[6]/div/div[3]//button"))).click()
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
ref.take_assesment()
ref.personality_assesment()