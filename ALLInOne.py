import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class All():

    def all(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://test-talentplace.vercel.app/")

        # Login Button
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()

        # Login Page
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(
            "amithkulkarni98@gmail.com")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        # PERSONAL DETAILS

        # first name change
        driver.find_element(By.ID, "first-name").clear()
        driver.find_element(By.ID, "first-name").send_keys("Kulkarni")
        # time.sleep(2)

        # Second  name change
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys("Amith")
        time.sleep(2)
        driver.find_element(By.NAME, "lastName").send_keys(Keys.TAB)
        driver.find_element(By.NAME, "lastName").send_keys(Keys.TAB)

        # Gender
        gender = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class=' css-19bb58m']/input")))
        gender.send_keys("Male")
        gender.send_keys(Keys.TAB)
        gender.send_keys(Keys.TAB)
        time.sleep(5)  # to add gender normally

        # Date of Birth
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("25")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("03")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(
            "1999")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(
            Keys.TAB)
        time.sleep(2)

        # Currency Drop-Down
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable(
                (By.XPATH, "//*[@class='chakra-stack css-11i9qz7']/div[3]/div//input"))).send_keys("INR")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(
            Keys.TAB)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(
            Keys.TAB)

        # Experience
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            "02")
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            Keys.TAB)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            "2020")
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(
            Keys.TAB)
        time.sleep(2)

        # Check box
        # driver.find_element(By.CSS_SELECTOR, ".chakra-checkbox__control.css-exc098").click()
        # time.sleep(4)

        # Auto suggestion// Place
        place = driver.find_element(By.XPATH, "//input[contains(@name,'loca')]")
        place.clear()
        place.send_keys("Bengaluru, Karnataka, India")
        place.send_keys(Keys.TAB)

        # Headline
        driver.find_element(By.NAME, "headline").clear()
        driver.find_element(By.NAME, "headline").send_keys("Python automation  Tester")
        time.sleep(2)

        # Add social media
        add = driver.find_element(By.NAME, "socialMedia.linkedin")
        add.clear()
        add.send_keys("https://www.linkedin.com/in/amith-kulkarni-1326241b4")
        time.sleep(2)

        # Save
        driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(2)

        # next button
        driver.find_element(By.XPATH, "//p[@class='chakra-text css-0']").click()
        time.sleep(2)

        for i in range(1, 11):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='css-anpdgu'][2]//div[1]//button"))).click()
            time.sleep(2)

        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)

        # ADD COMPANY
        #  Company Name
        company = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='custom-select__input']")))
        company.send_keys("Cognizant")
        company.send_keys(Keys.TAB)
        time.sleep(2)

        # Job Type
        job = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[2]/div[1]//input")))
        job.send_keys("Full time")
        job.send_keys(Keys.TAB)
        time.sleep(2)

        # Industry Experience
        exp = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[2]/div[2]//input")))
        exp.send_keys("Software engineering")
        exp.send_keys(Keys.TAB)
        time.sleep(2)

        # Organization Type
        org = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[3]/div[1]//input")))
        org.send_keys("MNC")
        org.send_keys(Keys.TAB)
        time.sleep(2)

        # Product Based??
        prd = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[3]/div[2]//input")))
        prd.send_keys("Product")
        prd.send_keys(Keys.TAB)
        time.sleep(2)

        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)

        # Add Job Role Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Add Job Role']"))).click()

        # Designation
        des = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[1]/div[1]//input")))
        des.send_keys("Python developer")
        des.send_keys(Keys.TAB)
        time.sleep(2)

        # Management Level
        manag = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[1]/div[2]//input")))
        manag.send_keys("Junior")
        manag.send_keys(Keys.TAB)
        time.sleep(2)

        # Location
        loc = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[2]/div[1]//input")))
        loc.clear()
        loc.send_keys("Bengaluru, Karnataka, India")
        loc.send_keys(Keys.TAB)

        # Development
        dev = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[2]/div[2]//input")))
        dev.send_keys("Development")
        dev.send_keys(Keys.TAB)
        time.sleep(2)

        # Skill
        skil = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class ='chakra-stack css-vtn7ly']/div[3]//div[2]/div[1]//input")))
        skil.send_keys("Python")
        skil.send_keys(Keys.TAB)
        time.sleep(2)

        # Expertise
        expert = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class ='chakra-stack css-vtn7ly']/div[3]//div[2]/div[2]//input")))
        expert.send_keys("skilful")
        expert.send_keys(Keys.TAB)
        time.sleep(2)

        # Add skill Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[3]/div[2]//button"))).click()

        # Start date and End date
        start = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[4]/div[1]//input")))
        start.send_keys("December")
        start.send_keys(Keys.TAB)
        start.send_keys("2007")
        time.sleep(2)

        end = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[4]/div[2]//input")))
        end.send_keys("April")
        end.send_keys(Keys.TAB)
        end.send_keys("2011")
        time.sleep(2)

        # If user is Still working in same Company
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
        #     (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[4]/div[2]/label/input"))).click()

        # Salary Start and End
        # Start
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[5]/div[1]/input"))).send_keys("10000")
        # End
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[5]/div[2]/input"))).send_keys("25000")

        # Roles and Responsibility
        # generate Responsibility
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, "//*[@class='chakra-stack css-vtn7ly']/div[6]/div/div[2]//button"))).click()

        # Click on Some Points
        for i in range(1, 4):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,
                                                                        f"//*[@class='chakra-stack css-vtn7ly']/div[6]/div/div[2]/div//div[1]/div[{i}]/button"))).click()

        # Click on Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)

        # back to Companies Button
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-button css-13zvu4r']"))).click()

        # Click on Next
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()

        # ADD EDUCATION




