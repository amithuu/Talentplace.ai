import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
k = 59
name = "Autotest"
email = f"autotest{k}@g.co"
password = "New@1234"
location = "Bengaluru, Karnataka, India"
phone_number = f"+1 1{k}3449771"
company_name = "cognizant"
skills = "Python"
# cancel = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Cancel']")))

class Automation:
    # Sign Up Page
    def signup(self):

        driver.get("https://test-talentplace.vercel.app/")

        """Sign up button !! """
        sign_up = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Sign Up']")))
        sign_up.click()
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
        time.sleep(3)

    def login(self):
        driver.get("https://test-talentplace.vercel.app/login")
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)
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
        time.sleep(3)
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
        save.click()
        time.sleep(5)

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
        time.sleep(1)
        # Location
        loc = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")))
        loc.send_keys(Keys.CONTROL + "a")
        loc.send_keys(location)
        time.sleep(3)
        # Functional Area
        functional_area = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[2]//input")))
        functional_area.send_keys("Development")
        functional_area.send_keys(Keys.TAB)
        time.sleep(1)
        # Skill
        skill = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[1]//input")))
        skill.send_keys("Python")
        skill.send_keys(Keys.TAB)
        time.sleep(1)
        # Expertise
        expertise = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[2]//input")))
        expertise.send_keys("skilful")
        expertise.send_keys(Keys.TAB)
        time.sleep(1)
        # Add Skill Button
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/div[2]//button"))).click()
        # Start Date and End date
        start_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]/div[1]//input")))
        start_date.send_keys("December")
        start_date.send_keys(Keys.TAB)
        start_date.send_keys("2007")
        time.sleep(1)
        end_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]/div[2]//input")))
        end_date.send_keys("April")
        end_date.send_keys(Keys.TAB)
        end_date.send_keys("2011")
        time.sleep(1)
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
        time.sleep(1)
        # Location
        loc = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")
        loc.send_keys(location)
        time.sleep(3)
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
        # currently_pursuing = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/div[2]/label//span")))
        # currently_pursuing.click()
        # time.sleep(3)
        # Project Description
        project_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]//p")))
        project_description.send_keys(" This is my automation Project ")
        time.sleep(1)
        # Extra Circular Activities
        extra_circular_activities = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[5]//p")))
        extra_circular_activities.send_keys(" These are my extra circular activities ")
        time.sleep(1)
        # Click to Upload Image
        click_upload_image = driver.execute_script(" return document.getElementsByTagName('u')[0]")
        driver.execute_script("arguments[0].click();", click_upload_image)
        time.sleep(5)
        # Save
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
        time.sleep(10)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()
        time.sleep(2)
        # Discard
        discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
        discard.click()

    def cognitive_skills(self):
        driver.get("https://test-talentplace.vercel.app/onboarding/cognitive-skills")
        time.sleep(4)
        """Cognitive skills"""
        for s in range(1, 7):
            driver.find_element(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div/div[{s}]//span[1]").click()
            slid = driver.find_element(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div/div[{s}]//div[@role='slider']")
            ActionChains(driver).move_to_element(slid).pause(1).click_and_hold(slid).move_by_offset((35 * s), 0).release().perform()
            time.sleep(2)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(4)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()

    def carrier_summary(self):
        """ADD CARRIER SUMMARY"""
        # Generate Summary
        driver.set_window_size(1200, 1400)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        generate_suggestion = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Generate Suggestions']")))
        generate_suggestion.click()
        time.sleep(12)
        for a in range(1, 4):
            driver.find_element(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[{a}]//button").click()
            time.sleep(1)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(4)
        # Customer Profile Button
        customize_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Customise Profile']")))
        customize_profile.click()
        time.sleep(2)

    def customize_profile(self):
        driver.maximize_window()
        """Customer Profile"""
        # Adding All the Other Forms
        for i in range(1, 11):
            add_forms = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='chakra-stack css-ihq88o']/div[2]/div[1]//button")))
            add_forms.click()
            time.sleep(2)
        # Save and Next Button
        save_and_next = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Save and Next']")))
        save_and_next.click()
        time.sleep(4)

    def dashboard(self):
        dashboard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Dashboard']")))
        dashboard.click()
        time.sleep(3)
        # Click on Edit Profile
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//p[text()='Edit Profile']"))).click()

        # GO to  Projects
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//p[text()='Projects']"))).click()

    def projects(self):
        """Projects"""
        # Project Name
        project_name = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//input[@type='text' and @name='name']")))
        project_name.send_keys("Aws Project")
        time.sleep(1)
        # Start date
        start_date = driver.find_element(By.XPATH, "//input[@type='month' and @name='start_date']")
        start_date.send_keys("January")
        start_date.send_keys(Keys.TAB)
        start_date.send_keys("1999")
        # End date
        end_date = driver.find_element(By.XPATH, "//input[@type='month' and @name='end_date']")
        end_date.send_keys("02")
        end_date.send_keys(Keys.TAB)
        end_date.send_keys("2022")
        # Associated with
        associated_with = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/form/div/div[3]/div[1]//input")))
        associated_with.send_keys(company_name)
        associated_with.send_keys(Keys.TAB)
        # Project url
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
        ActionChains(driver).move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset((35 * 4), 0).release().perform()
        time.sleep(1)
        # Button '+'
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Add Skill Complexity']"))).click()
        # Skill applications
        skill_application = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@role='region']/form/div/div[6]//p")))
        skill_application.send_keys(" This is skill description what i have ")
        time.sleep(1)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(4)

    def certificate(self):
        for i in range(2):
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
            next_.click()
            time.sleep(2)
            # Discard
            discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
            discard.click()
            time.sleep(2)
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
        duration_from.send_keys("1999")
        time.sleep(2)
        # Duration to
        duration_to = driver.find_element(By.XPATH, "//*[@role='region']/div/div[2]/div[2]//input")
        duration_to.send_keys("Feb")
        duration_to.send_keys(Keys.TAB)
        duration_to.send_keys("2020")
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
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(4)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']/button[2]")))
        next_.click()
        # Discard
        discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
        discard.click()

    def publication(self):
        # """Publication"""
        # Title
        title = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[1]/div[1]//input")
        title.send_keys("This is publication Title")
        # Publication ID
        publisher_id = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[1]/div[2]//input")
        publisher_id.send_keys("This is publisher ID")
        # Publication Date
        publisher_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")))
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
        author_name.send_keys(name)
        # Author linkdIn link
        linkdin_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[2]//input")))
        linkdin_link.send_keys("https://www.linkedin.com/in/amith-kulkarni-1326241b4")
        # Delete Author
        # delete_author = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[2]//button")
        # delete_author.click()
        # Description
        # Publication Description
        publication_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[4]//p")))
        publication_description.send_keys("this is my first Publication")
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()

    def patent(self):
        """Patent"""
        # Title
        title = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[1]//input")))
        title.send_keys("This is Patients Title ")
        # Patient Application Number
        patent_application_number = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[1]/div[2]//input")))
        patent_application_number.send_keys("123456")
        # Issue Date
        issue_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[1]//input")))
        issue_date.send_keys("02-02-2021")
        issue_date.send_keys(Keys.TAB)
        # Patent Url
        patent_url = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/div[2]/div[2]//input")))
        patent_url.send_keys("https://test-talentplace.vercel.app")
        # Patient Not yet Issued Check box
        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/form/div/label//span[1]"))).click()
        # Add Author
        time.sleep(3)
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
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()

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
        time.sleep(1)
        # Link Delete
        # driver.find_element(By.XPATH, "//*[@role='region']/div/div[4]/div/div[1]//button").click()
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(5)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()

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
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()

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
        associated_with.send_keys(Keys.TAB)
        # Description
        description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@role='region']/div/div[3]//p")))
        description.send_keys("this is my first patient")
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()
        time.sleep(1)

    def causes(self):
        """Causes"""
        # Select The Causes Max[6]
        for i in range(1, 7):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//div[@id='root']/div[2]/div/div/div/div/div[1]/div/div[{i}]//span[1]"))).click()
            time.sleep(1)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()
        time.sleep(2)

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
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[2]/button"))).click()
            time.sleep(2)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()
        time.sleep(2)

    def languages(self):
        """Languages"""
        language = ['english', 'kannada', 'Hindi']
        proficiency = ['inter', 'exp', 'begin']
        for i in range(len(language)):
            # Language Drop Down
            lan = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[1]//input")))
            lan.send_keys(language[i])
            lan.send_keys(Keys.TAB)
            # Proficiency
            prof = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[2]//input")))
            prof.send_keys(proficiency[i])
            prof.send_keys(Keys.TAB)
            # Add + Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div/div[2]/button"))).click()
            time.sleep(2)

        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]//button[2]")))
        next_.click()
        time.sleep(2)

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
        upgrade = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div[6]/div/div[3]//button")))
        upgrade.click()
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

    def my_profile(self):
        """ My Profile """
        # Click on My Profile
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//p[text()='My Profile']"))).click()
        my_profile_window = driver.current_window_handle
        # CLick on Share Button to share the Profile
        share_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[3]/div[1]//button[3]")))
        share_profile.click()
        # Copy link
        copy_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='edit profile'][4]")))
        copy_link.click()
        time.sleep(3)
        driver.get("https://test-talentplace.vercel.app/share-profile/amithkulkarni98")
        driver.switch_to.window(my_profile_window)
        time.sleep(2)
        driver.back()


ref = Automation()
# ref.signup()
ref.login()
# ref.welcome_page()
# ref.personal_details()
# ref.nextback()
# ref.experience()
# ref.education()
ref.cognitive_skills()
ref.carrier_summary()
ref.customize_profile()
ref.dashboard()
ref.projects()
ref.certificate()
ref.publication()
ref.patent()
ref.portfolio()
ref.voluntary_roles()
ref.honor_rewards()
ref.causes()
ref.hobbies()
ref.languages()
ref.take_assesment()
ref.personality_assesment()
ref.my_profile()


