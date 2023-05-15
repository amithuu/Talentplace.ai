import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from LoginPage_auto import LoginPage
class PersonalDetails(LoginPage):
    def personaldetails(self):

        # first name change
        self.driver.find_element(By.ID, "first-name").clear()
        self.driver.find_element(By.ID, "first-name").send_keys("Kulkarni")
        # time.sleep(2)

        # Second  name change
        self.driver.find_element(By.NAME, "lastName").clear()
        self.driver.find_element(By.NAME, "lastName").send_keys("Amith")
        time.sleep(2)
        self.driver.find_element(By.NAME, "lastName").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "lastName").send_keys(Keys.TAB)

        # Gender
        gender = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class=' css-19bb58m']/input")))
        gender.send_keys("Male")
        gender.send_keys(Keys.TAB)
        gender.send_keys(Keys.TAB)
        time.sleep(5)  # to add gender normally

        # Date of Birth
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("25")
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("03")
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("1999")
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(Keys.TAB)
        time.sleep(2)

        # Currency Drop-Down
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                (By.XPATH, "//*[@class='chakra-stack css-11i9qz7']/div[3]/div//input"))).send_keys("INR")
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(Keys.TAB)
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(Keys.TAB)

        # Experience
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            "02")
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            Keys.TAB)
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            "2020")
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            Keys.TAB)
        time.sleep(2)

        # Check box
        # driver.find_element(By.CSS_SELECTOR, ".chakra-checkbox__control.css-exc098").click()
        # time.sleep(4)

        # Auto suggestion// Place
        place = self.driver.find_element(By.XPATH, "//input[contains(@name,'loca')]")
        place.clear()
        place.send_keys("Bengaluru, Karnataka, India")
        place.send_keys(Keys.TAB)

        # Headline
        self.driver.find_element(By.NAME, "headline").clear()
        self.driver.find_element(By.NAME, "headline").send_keys("Python automation  Tester")
        time.sleep(2)

        # Add social media
        add = self.driver.find_element(By.NAME, "socialMedia.linkedin")
        add.clear()
        add.send_keys("https://www.linkedin.com/in/amith-kulkarni-1326241b4")
        time.sleep(2)

        # Save
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(2)

        # next button
        self.driver.find_element(By.XPATH, "//p[@class='chakra-text css-0']").click()
        time.sleep(2)


ref = PersonalDetails()
ref.personaldetails()
