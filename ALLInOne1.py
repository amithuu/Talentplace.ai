# Todo: ! Sign-UP ! Login ! Complete Profile !

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
name = "Autotest"
email = "autotest111@g.co"
password = "New@1234"
location = "Bengaluru, Karnataka, India"
company_name = "Cognizant"
skills = "Python"

class Automation:
    # Sign =-Up Page
    def signup(self):

        driver.get("https://test-talentplace.vercel.app/sign-up")

        """Sign up button !! WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//button[text()='Sign Up']"))).click()"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='firstName']"))).send_keys(
            name)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='lastName']"))).send_keys(
            name)

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='email']"))).send_keys(
            email)

        element = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='form-control telephone-input']")))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys("+1 3723449773")
        time.sleep(3)

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("25")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("03")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("1999")

        gen = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='gender']")))
        gen.send_keys("male")
        gen.send_keys(Keys.TAB)

        loc = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-14uartk']/div[5]//input")))
        loc.send_keys(Keys.CONTROL + "a")
        loc.send_keys("Bangalore, Karnataka, India")
        time.sleep(5)

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='password']"))).send_keys(
            "New@1234")
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@name='confirmPassword']"))).send_keys("New@1234")

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Sign Up']"))).click()
        time.sleep(10)

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
        carrier_profile = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//div[@class='css-1h1zoku']/div[1]//button")))
        carrier_profile.click()
        # '''As new feature is arrived I am redirecting to onboarding'''
        # driver.get("https://test-talentplace.vercel.app/onboarding")
        # time.sleep(3)
        # In Dash Board  !! Click on Build Carrier Profile
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Build Career Profile']"))).click()

    def personal_details(self):
        """PERSONAL DETAILS"""
        # First name
        driver.find_element(By.ID, "first-name").clear()
        driver.find_element(By.ID, "first-name").send_keys(name)
        # Second name
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys(name)
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
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys("1999")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(Keys.TAB)
        time.sleep(2)
        # Currency Drop-Down
        WebDriverWait(driver, 20).until( ec.element_to_be_clickable((By.XPATH, "//*[@class='chakra-stack css-11i9qz7']/div[3]/div//input"))).send_keys("INR")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(Keys.TAB)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dob']"))).send_keys(Keys.TAB)
        # Experience
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys("02")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(Keys.TAB)
        WebDriverWait(driver, 20).until( ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys( "2020")
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@name='experienceStartDate']"))).send_keys(Keys.TAB)
        time.sleep(5)

        # Check box
        # driver.find_element(By.CSS_SELECTOR, ".chakra-checkbox__control.css-exc098").click()
        # Auto suggestion// Place
        place = driver.find_element(By.XPATH, "//input[contains(@name,'loca')]")
        place.send_keys(Keys.CONTROL + "a")
        place.send_keys(location)
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
    def nextback(self):
        # Next button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[1]"))).click()
        time.sleep(2)
        # Back Button
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]"))).click()
        # Save and Next Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Save and Next']"))).click()

    # delete the old one
    # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='chakra-button css-1ixh03']"))).click()
    # time.sleep(2)
    # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='chakra-button css-11pbcgl']"))).click()
    # time.sleep(2)
    def addexperience(self):
        """ADD COMPANY"""
        # Company Name
        company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[1]//input")))
        company.send_keys(company_name)
        company.send_keys(Keys.TAB)
        time.sleep(1)
        # Job Type
        job = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[2]/div[1]//input")))
        job.send_keys("Full time")
        job.send_keys(Keys.TAB)
        time.sleep(1)
        # Industry Experience
        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[2]/div[2]//input")))
        exp.send_keys("Software engineering")
        exp.send_keys(Keys.TAB)
        time.sleep(1)
        # Organization Type
        org = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[3]/div[1]//input")))
        org.send_keys("MNC")
        org.send_keys(Keys.TAB)
        time.sleep(1)
        # Product Based??
        prd = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/div/div[3]/div[2]//input")))
        prd.send_keys("Product")
        prd.send_keys(Keys.TAB)
        time.sleep(1)
        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(3)

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
        # Development
        dev = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[2]//input")))
        dev.send_keys("Development")
        dev.send_keys(Keys.TAB)
        time.sleep(2)
        # Skill
        skil = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[1]//input")))
        skil.send_keys("Python")
        skil.send_keys(Keys.TAB)
        time.sleep(2)
        # Expertise
        expert = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[2]//input")))
        expert.send_keys("skilful")
        expert.send_keys(Keys.TAB)
        time.sleep(2)
        # Add skill Button
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
        #Click on Some Points
        for i in range(1, 4):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@role='region']/form/div/div[6]/div/div[2]//div[{i}]//button"))).click()
            time.sleep(1)
        # Click on Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)
        # Back to Companies Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']//button"))).click()
        # Click on Next
        next = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']//button[2]")))
        next.click()
    def education(self):
        """ADD EDUCATION"""
        # Degree
        degree = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[1]//input")))
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
    def cognitive_skils(self):
        """Cognitive skills"""
        driver.get("https://test-talentplace.vercel.app/onboarding/cognitive-skills")
        time.sleep(3)
        """Cognitive skills"""
        for s in range(1, 7):
            driver.find_element(By.XPATH,
                                f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div/div[{s}]//span[1]").click()
            slid = driver.find_element(By.XPATH,
                                       f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div/div[{s}]//div[@role='slider']")
            ActionChains(driver).move_to_element(slid).pause(1).click_and_hold(slid).move_by_offset((35 * s),
                                                                                                    0).release().perform()
            time.sleep(2)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(2)
        # Next
        next_ = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()
    def carrier_summary(self):
        # """ADD CARRIER SUMMARY"""
        # Generate Summary
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Generate Suggestions']"))).click()
        time.sleep(20)
        """//div[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]//button""" "in[edit-resume]"
        for a in range(1, 4):
            driver.find_element(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[{a}]//button").click()
            time.sleep(1)
        # Save
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
        time.sleep(3)
        # Customer Profile Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Customise Profile']"))).click()
        time.sleep(2)
    def customize_profile(self):
        """Customer Profile"""
        # Adding All the Other Forms
        for i in range(1, 11):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='chakra-stack css-ihq88o']/div[2]/div[1]//button"))).click()
            time.sleep(2)
        # Save and Next Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Save and Next']"))).click()
        time.sleep(2)
    def Profile_complition(self):
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()

        """Projects"""
        # Project Name
        project_name = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//input[@type='text' and @name='name']")))
        project_name.send_keys("Aws Project")
        time.sleep(1)
        # Start date
        start_date = driver.find_element(By.XPATH, "//input[@type='month' and @name='start_date']")
        start_date.send_keys("January")
        start_date.send_keys(Keys.TAB)
        start_date.send_keys("2020")
        # End date
        end_date = driver.find_element(By.XPATH, "//input[@type='month' and @name='end_date']")
        end_date.send_keys("02")
        end_date.send_keys(Keys.TAB)
        end_date.send_keys("2022")
        # Associated with
        associated_with = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/form/div/div[3]/div[1]//input")))
        associated_with.send_keys(company_name)
        associated_with.send_keys(Keys.TAB)
        # project url
        project_url = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/form/div/div[3]/div[2]//input")))
        project_url.send_keys("https://web.whatsapp.com")
        # Description
        description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/form/div/div[4]//p")))
        description.send_keys(" hlo i am learning Pytest automation tool ")
        # Skills
        skill = driver.find_element(By.XPATH,"//div[@role='region']/form/div/div[5]/div[2]/div[1]//input")
        skill.send_keys("Python")
        skill.send_keys(Keys.TAB)
        # Skill Ranger
        slider = driver.find_element(By.XPATH, "//div[@role='region']/form/div/div[5]/div[2]/div[2]//div[@role='slider']")
        ActionChains(driver).move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(280, 0).release().perform()
        time.sleep(2)
        # Button '+'
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Add Skill Complexity']"))).click()
        # Skill applications
        skill_application = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/form/div/div[6]//p")))
        skill_application.send_keys(" This is skill description what i have ")
        time.sleep(2)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        save.click()
        time.sleep(2)
    def certificate(self):
        for i in range(1, 3):
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
            next_.click()
        """Certificate"""
        # Title
        title = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[1]/div[1]//input")))
        title.send_keys(" This is Project Title ")
        time.sleep(1)
        # Institution
        institution = driver.find_element(By.XPATH, "//*[@role='region']/div/div[1]/div[2]//input")
        institution.send_keys(" Where you did Certificate ")
        time.sleep(1)
        # Duration from
        duration_from = driver.find_element(By.XPATH, "//*[@role='region']/div/div[2]/div[1]//input")
        duration_from.send_keys("January")
        duration_from.send_keys(Keys.TAB)
        duration_from.send_keys("2020")
        time.sleep(2)
        # Duration to
        duration_to = driver.find_element(By.XPATH, "//*[@role='region']/div/div[2]/div[2]//input")
        duration_to.send_keys("Feb")
        duration_to.send_keys(Keys.TAB)
        duration_to.send_keys("2022")
        time.sleep(2)
        # Skill add
        skill = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[3]/div[2]/div[1]//input")))
        skill.send_keys(skills)
        skill.send_keys(Keys.TAB)
        time.sleep(2)
        # Add Skill '+' Button
        driver.find_element(By.XPATH, "//*[@role='region']/div/div[3]/div[2]/div[2]//button").click()
        time.sleep(2)
        # Projects Description
        project_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[4]//p")))
        project_description.send_keys(" This is certification description ")
        time.sleep(1)
        # Upload Certificate
        upload_certificate = driver.execute_script("return document.getElementsByTagName('u')[0];")
        driver.execute_script("arguments[0].click();", upload_certificate)
        time.sleep(5)

        # Save Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
        # Next Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]"))).click()
        time.sleep(2)
    def publication(self):
        # """Publication"""
        # Title
        title = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[1]/div[1]//input")
        title.send_keys("This is publication Title")
        # Publication ID
        publisher_id = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[1]/div[2]//input")
        publisher_id.send_keys("This is publisher ID")
        # Publication Date
        publisher_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input]")))
        publisher_date.send_keys("02-02-2021")
        # Publication Url
        publication_url = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[2]/div[2]//input")
        publication_url.send_keys("https://test-talentplace.vercel.app")
        # Add Author
        add_author = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]//button")))
        add_author.click()
        time.sleep(3)
        # Author title
        author_title = Select(driver.find_element(By.XPATH, "//select[@name='authors.0.pronounce']"))
        author_title.select_by_visible_text("Mr")
        # Author Name
        author_name = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[1]/div[2]//input")))
        author_name.send_keys("Amith")
        # Author linkdIn link
        linkdin_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[2]//input")))
        linkdin_link.send_keys("https://www.linkedin.com/in/amith-kulkarni-1326241b4")
        # Delete Author
        # delete_author = driver.find_element(By.XPATH, "//button[@type='button'and@aria-label='Remove item']")
        # delete_author.click()
        # Description
        # Publication Description
        publication_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]//p")))
        publication_description.send_keys("this is my first Publication")
        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(10)
        # Next Button
        driver.find_element(By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]").click()
    def patent(self):
        """Patent"""
        # Title
        title = WebDriverWait(driver, 20).until( ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[1]//input")))
        title.send_keys("This is Patients Title ")
        time.sleep(2)
        # Patient Application Number
        patent_application_number = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[2]//input")))
        patent_application_number.send_keys("123456")
        time.sleep(2)
        #  Issue Date
        issue_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")))
        issue_date.send_keys("02-02-2021")
        issue_date.send_keys(Keys.TAB)
        time.sleep(2)
        # Patent Url
        patent_url = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")))
        patent_url.send_keys("https://test-talentplace.vercel.app")
        time.sleep(2)
        # Patient Not yet Issued Check box
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/label//span[1]"))).click()
        # Add Author
        add_author = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]//button")))
        add_author.click()
        # Author Title
        author_title = Select(driver.find_element(By.XPATH, "//select[@name='investors.0.pronounce']"))
        author_title.select_by_visible_text("Mr")
        # Author Name
        author_name = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[1]/div[2]//input")))
        author_name.send_keys(name)
        # linkdIn Id
        linkdin_id = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[2]//input")))
        linkdin_id.send_keys("https://www.linkedin.com/in/amith-kulkarni-1326241b4")
        time.sleep(2)
        # Delete Author
        # driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[2]//button").click()
        # Description
        description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]//p")))
        description.send_keys("this is my first Publication")
        time.sleep(2)
        # Save Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
        time.sleep(10)
        # Next Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]"))).click()
    def portfolio(self):
        """Portfolio"""
        # Title
        patent_title = driver.find_element(By.XPATH, "//*[@role='region']/div/div[1]//input")
        patent_title.send_keys("This is PATIENTS Title")
        # Description
        description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[2]//p")))
        description.send_keys("this is my automated patient")
        # Upload Certificate
        upload_certificate = driver.execute_script("return document.getElementsByTagName('u')[0];")
        driver.execute_script("arguments[0].click();", upload_certificate)
        time.sleep(5)
        # Link of Portfolio
        portfolio_link = driver.find_element(By.XPATH, "//*[@role='region']/div/div[4]/div/div[2]/div//input")
        portfolio_link.send_keys("https://test-talentplace.vercel.app/edit-profile/portfolio")
        # Add Link + Button
        driver.find_element(By.XPATH, "//*[@role='region']/div/div[4]/div/div[2]//button").click()
        time.sleep(2)
        # Link Delete
        # driver.find_element(By.XPATH, "//*[@role='region']/div/div[4]/div/div[1]//button").click()
        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(5)
        # Next Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]"))).click()
    def voluntary_roles(self):
        """Voluntary Roles"""
        # Role
        role = driver.find_element(By.XPATH, "//*[@role='region']/div/div[1]/div[1]//input")
        role.send_keys("This is PATIENTS Title")
        # Organization
        organization = driver.find_element(By.XPATH, "//*[@role='region']/div/div[1]/div[2]//input")
        organization.send_keys("This is PATIENTS Title")
        # Duration From
        duration_from = driver.find_element(By.XPATH, "//*[@role='region']/div/div[2]/div[1]//input")
        duration_from.send_keys("January")
        duration_from.send_keys(Keys.TAB)
        duration_from.send_keys("2020")
        # Duration To
        duration_to = driver.find_element(By.XPATH, "//*[@role='region']/div/div[2]/div[2]//input")
        duration_to.send_keys("march")
        duration_to.send_keys(Keys.TAB)
        duration_to.send_keys("2023")
        # Check Box[" I am currently working here"]
        # driver.find_element(By.XPATH, "//*[@role='region']/div/div[2]/div[2]/label/span[1]").click()
        # Description
        description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[3]//p")))
        description.send_keys("this is my first patient")
        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(5)
        # Next Button
        driver.find_element(By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]").click()
        time.sleep(3)
    def honor_rewards(self):
        """Honors and Awards"""
        # Title
        title_name = driver.find_element(By.XPATH, "//*[@role='region']/div/div[1]/div[1]//input")
        title_name.send_keys("This is  Title")
        # Issuer
        issuer_name = driver.find_element(By.XPATH, "//*[@role='region']/div/div[1]/div[2]//input")
        issuer_name.send_keys(" I am The Issuer")
        # Duration From
        duration_from = driver.find_element(By.XPATH, "//*[@role='region']/div/div[2]/div[1]//input")
        duration_from.send_keys("January")
        duration_from.send_keys(Keys.TAB)
        duration_from.send_keys("2020")
        # Associated With
        associated_with = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[2]/div[2]//input")))
        associated_with.send_keys(company_name)
        # Description
        description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[3]//p")))
        description.send_keys("this is my first patient")
        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(5)
        # Next Button
        driver.find_element(By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]").click()
        time.sleep(3)
    def causes(self):
        """Causes"""
        # Select The Causes Max[6]
        for i in range(1, 7):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//div[@id='root']/div[2]/div/div/div/div/div[1]/div/div[1]//span[1]"))).click()
            time.sleep(1)
        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)
        # Next Button
        driver.find_element(By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]").click()
        time.sleep(3)

    def hobbies(self):
        # """Hobbies"""
        category = ['Sports', 'Travel', 'Books']
        hobby = ['Cricket', 'Kerala', 'The untold Story']
        for i in range(len(category)):
            # Category Select
            categorys = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[1]//input")))
            categorys.click()
            categorys.send_keys(category[i])
            categorys.send_keys(Keys.TAB)
            time.sleep(2)
            # Hobbies Text
            hobbies = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[2]//input")))
            hobbies.send_keys(hobby[i])
            time.sleep(2)
            # Add Hobbies '+' Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[ @aria-label='add-hobby']"))).click()
            time.sleep(2)
        # Save Button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)
        # Next Button
        driver.find_element(By.XPATH, "//button[@class='chakra-button css-13zvu4r'][2]").click()
        time.sleep(2)

    def languages(self):
        # """Languages"""
        language = ['english', 'kannada', 'Hindi']
        proficiency = ['inter', 'exp', 'begin']
        for i in range(len(language)):
            # Language Drop Down
            lan = WebDriverWait(driver, 20).until(
                ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[1]//input")))
            lan.send_keys(language[i])
            lan.send_keys(Keys.TAB)
            # Proficiency
            prof = WebDriverWait(driver, 20).until(
                ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[2]//input")))
            prof.send_keys(proficiency[i])
            prof.send_keys(Keys.TAB)
            # Add + Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[2]/button"))).click()
            time.sleep(2)
        # Save Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
        # Next Button
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']//button[2]")))
        next_.click()


ref = Automation()
ref.signup()
ref.login()
