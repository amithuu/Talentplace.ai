import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
i = 10
name = "Autotest"
email = f"autotest{i}@g.co"
password = "New@1234"
location = "Bengaluru, Karnataka, India"
phone_number = f"+1 1{i}3449771"
company_name = "cognizant"
# cancel = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Cancel']")))
class Automation:
    # Sign =-Up Page
    def signup(self):

        driver.get("https://test-talentplace.vercel.app/sign-up")

        """Sign up button !! WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//button[text()='Sign Up']"))).click()"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='firstName']"))).send_keys(name)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='lastName']"))).send_keys(name)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='email']"))).send_keys(email)

        element = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='form-control telephone-input']")))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(phone_number)

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("25")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("03")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("1999")

        gen = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='gender']")))
        gen.send_keys("male")
        gen.send_keys(Keys.TAB)

        loc = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-14uartk']/div[5]//input")))
        loc.send_keys(Keys.CONTROL + "a")
        loc.send_keys("Bangalore, Karnataka, India")
        time.sleep(5)

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='password']"))).send_keys("New@1234")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='confirmPassword']"))).send_keys("New@1234")

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Sign Up']"))).click()
        time.sleep(5)

    def login(self):
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

    def welcome_page(self):
        """Welcome, Page"""
        # Get Started Button for Carrier Profile
        get_started = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Get Started']")))
        get_started.click()
        time.sleep(5)

    def personal_details(self):
        """PERSONAL DETAILS"""
        # First name
        driver.find_element(By.ID, "first-name").clear()
        driver.find_element(By.ID, "first-name").send_keys(name)
        # Second name
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys(name)
        driver.find_element(By.NAME, "lastName").send_keys(Keys.TAB)
        driver.find_element(By.NAME, "lastName").send_keys(Keys.TAB)
        # Gender
        gender = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class=' css-19bb58m']/input")))
        gender.send_keys("Male")
        gender.send_keys(Keys.TAB)
        gender.send_keys(Keys.TAB)
        # Date of Birth
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("25")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("03")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("1999")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(Keys.TAB)
        time.sleep(2)
        # Currency Drop-Down
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-11i9qz7']/div[3]/div//input"))).send_keys("INR")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-11i9qz7']/div[3]/div//input"))).send_keys(Keys.TAB)
        # Experience
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys("02")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(Keys.TAB)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys("2020")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(Keys.TAB)
        time.sleep(2)
        # Check box
        # driver.find_element(By.CSS_SELECTOR, ".chakra-checkbox__control.css-exc098").click()
        # Auto suggestion !! Place
        place = driver.find_element(By.XPATH, "//input[contains(@name,'loca')]")
        place.send_keys(Keys.CONTROL + "a")
        place.send_keys(location)
        time.sleep(5)
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
        save = driver.find_element(By.XPATH, "//button[text()='Save']")
        # Discard
        discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
        discard.click()
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()
    def nextback(self):
        # Next button
        back_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[1]"))).click()  # this is next here
        # Save and Next Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Save and Next']"))).click()
        time.sleep(2)
        # next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        # next_.click()

    def experience(self):
        """ADD COMPANY"""
        # Company Name
        company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[1]//input")))
        company.send_keys(company_name)
        company.send_keys(Keys.TAB)
        time.sleep(1)
        # Job Type
        job_type = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[2]/div[1]//input")))
        job_type.send_keys("Full time")
        job_type.send_keys(Keys.TAB)
        time.sleep(1)
        # Industry Experience
        experience = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[2]/div[2]//input")))
        experience.send_keys("Software engineering")
        experience.send_keys(Keys.TAB)
        time.sleep(1)
        # Organization Type
        organization = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[3]/div[1]//input")))
        organization.send_keys("MNC")
        organization.send_keys(Keys.TAB)
        time.sleep(1)
        # Product Based??
        which_based = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[3]/div[2]//input")))
        which_based.send_keys("Product")
        which_based.send_keys(Keys.TAB)
        time.sleep(1)
        # Save Button
        save = driver.find_element(By.XPATH, "//button[text()='Save']")
        save.click()

        """!! ADD JOB ROLES !!"""
        # Add Job Role Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Add Job Role']"))).click()
        # Designation
        designation = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[1]//input")))
        designation.send_keys("Python developer")
        designation.send_keys(Keys.TAB)
        time.sleep(2)
        # Management Level
        management_level = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[2]//input")))
        management_level.send_keys("Junior")
        management_level.send_keys(Keys.TAB)
        time.sleep(5)
        # Location
        loc = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")))
        loc.send_keys(Keys.CONTROL + "a")
        loc.send_keys(location)
        loc.send_keys(Keys.TAB)
        # Functional Area
        functional_area = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[2]//input")))
        functional_area.send_keys("Development")
        functional_area.send_keys(Keys.TAB)
        time.sleep(2)
        # Skill
        skill = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[1]//input")))
        skill.send_keys("Python")
        skill.send_keys(Keys.TAB)
        time.sleep(2)
        # Expertise
        expertise = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[2]//input")))
        expertise.send_keys("skilful")
        expertise.send_keys(Keys.TAB)
        time.sleep(2)
        # Add Skill Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[2]//button"))).click()
        # Start Date and End date
        start_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]/div[1]//input")))
        start_date.send_keys("December")
        start_date.send_keys(Keys.TAB)
        start_date.send_keys("2007")
        time.sleep(2)
        end_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]/div[2]//input")))
        end_date.send_keys("April")
        end_date.send_keys(Keys.TAB)
        end_date.send_keys("2011")
        time.sleep(2)
        # If user is Still working in same Company
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]/div[2]/label//input"))).click()
        # Salary Start and End
        start_salary = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[5]/div[1]/input")))
        start_salary.send_keys("10000")
        end_salary = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[5]/div[2]/input")))
        end_salary.send_keys("25000")
        # Roles and Responsibility
        generate_suggestions = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[6]/div/div[2]//button")))
        generate_suggestions.click()
        time.sleep(10)
        # Click on Some Points
        for j in range(1, 4):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@role='region']/form/div/div[6]/div/div[2]//div[{j}]//button"))).click()
            time.sleep(1)
        # Click on Save Button
        save = driver.find_element(By.XPATH, "//button[text()='Save']")
        save.click()
        time.sleep(2)
        # Back to Companies Button
        back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']//button")))
        back_to_company.click()
        time.sleep(2)
        # Discard
        discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
        discard.click()
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()

    def education(self):
        """ADD EDUCATION"""
        # Degree
        degree = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[1]//input")))
        degree.send_keys("Master in computer application(MCA)")
        degree.send_keys(Keys.TAB)
        time.sleep(2)
        # University
        university = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[2]//input")))
        university.send_keys("Master in computer application(MCA)")
        university.send_keys(Keys.TAB)
        time.sleep(5)
        # Location
        loc = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")
        loc.send_keys(location)
        loc.send_keys(Keys.TAB)
        time.sleep(2)
        # CGPA
        cgpa = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[2]//input")))
        cgpa.send_keys("7.98")
        # Duration from
        driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/div[1]//input").send_keys("January")
        driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/div[1]//input").send_keys(Keys.TAB)
        driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/div[1]//input").send_keys("2020")
        # Duration to
        driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]//input").send_keys("February")
        driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]//input").send_keys(Keys.TAB)
        driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]//input").send_keys("2022")
        # Currently Pursuing
        currently_pursuing = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/label//input")))
        currently_pursuing.click()
        time.sleep(3)
        # Project Description
        project_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]//p")))
        project_description.send_keys(" This is my automation Project ")
        # Extra Circular Activities
        extra_circular_activities = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[5]//p")))
        extra_circular_activities.send_keys(" These are my extra circular activities ")
        # Click to Upload Image
        click_upload_image = driver.execute_script(" return document.getElementsByTagName('u')[0]")
        driver.execute_script("arguments[0].click();", click_upload_image)
        time.sleep(5)
        # Save
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()


ref = Automation()
ref.signup()
ref.login()
ref.welcome_page()
ref.personal_details()
ref.nextback()
ref.experience()
ref.education()
