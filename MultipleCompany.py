import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Company variables
companyname = ["cognizant", "dell", "ibm"]
jobtype = ["full time", "intern", "part time", "freelanc", "contract"]
industryexp = ["Advanced Technologies", "IT Services", "Agri-business"]
orgtype = ["startup", "small", "mnc"]
based = ["product", "service", "both"]
location = ["Bangalore", "delhi", "american"]

# Designation variables
designationrole = ["Developer", "Automation", "application"]
managementlevel = ["jun", "sen", "mid"]
functionalarea = ["development", "human", "marketing"]
skilladd = ["java", "python", "c prog"]
expertiserole = ["beg", "skil", "expert"]
startsalary = ["1000", "2000", "3000"]
endsalary = ["10000", "20000", "30000"]


email = "prod1@g.co"
password = "New@1234"
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
class Addcompany():

    def login(self):
        # driver.get("https://test-talentplace.vercel.app/login")
        driver.get("https://talentplace.ai/login")

        driver.maximize_window()
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        editprofile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        editprofile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Experience']")))
        exp.click()
    def addcompany(self,i):

        add_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button")))
        add_company.click()
        time.sleep(2)

        # Company name
        company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]//input")))
        company.click()
        time.sleep(2)
        company.send_keys(companyname[i])
        company.send_keys(Keys.TAB)


        job_type = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]//input")))
        job_type.click()
        job_type.send_keys(jobtype[i])
        job_type.send_keys(Keys.TAB)


        experience = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]//input")))
        experience.click()
        experience.send_keys(industryexp[i])
        experience.send_keys(Keys.TAB)


        organization = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[3]/div[1]//input")))
        organization.click()
        organization.send_keys(orgtype[i])
        organization.send_keys(Keys.TAB)


        which_based = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[3]/div[2]//input")))
        which_based.click()
        which_based.send_keys(based[i])
        which_based.send_keys(Keys.TAB)


        # Save Button
        save = driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div//button")
        save.click()
        time.sleep(3)

        # # Back
        # back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
        # back_to_company.click()
        # time.sleep(2)
        #
        # # Next
        # next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
        # next_.click()
        # time.sleep(2)
    def addrole(self, s):
        for a in range(1, 3):
            """!! ADD JOB ROLES !!"""
            # Add Job Role Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div/div/div[{s+1}]//ul//button"))).click()
            # Designation
            designation = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[1]/div[1]/div[1]//input")))
            designation.send_keys(designationrole[a-1])
            designation.send_keys(Keys.TAB)
            # Management Level
            management_level = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[1]/div[2]/div[1]//input")))
            management_level.send_keys(managementlevel[s])
            management_level.send_keys(Keys.TAB)
            # Location
            loc = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[2]/div[1]/div[1]//input")))
            loc.send_keys(Keys.CONTROL + "a")
            loc.send_keys(location[a-1])
            time.sleep(5)

            """listt = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[2]/div[1]/div[1]/div/ul/li")))
            # checking result thing!!!!
            for result in listt:
                if location[a-i] in result.text:
                    result.click()
                    break
            time.sleep(7)"""

            # Functional Area
            functional_area = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[2]/div[2]/div[1]//input")))
            functional_area.send_keys("Development")
            functional_area.send_keys(Keys.TAB)

            # Skill
            skill = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[1]//input")))
            skill.send_keys(skilladd[a-1])
            skill.send_keys(Keys.TAB)

            # Expertise
            expertise = WebDriverWait(driver, 20).until(
                ec.element_to_be_clickable((By.XPATH,
                                            "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[2]//input")))
            expertise.send_keys(expertiserole[a-1])
            expertise.send_keys(Keys.TAB)

            # Add Skill Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[2]//button"))).click()
            # Start Date and End date
            start_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[1]//input")))
            start_date.send_keys("December")
            start_date.send_keys(Keys.TAB)
            start_date.send_keys("2007")

            end_date = WebDriverWait(driver, 20).until(
                ec.element_to_be_clickable((By.XPATH,
                                            "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[2]//input")))
            end_date.send_keys("April")
            end_date.send_keys(Keys.TAB)
            end_date.send_keys("2011")


            # If user is Still working in same Company
            # WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[2]/label//input"))).click()

            # Salary Start and End
            start_salary = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[5]/div[1]//input")))
            start_salary.send_keys(startsalary[a-1])
            end_salary = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[5]/div[2]//input")))
            end_salary.send_keys(endsalary[a-1])

            # # Roles and Responsibility
            # generate_suggestions = WebDriverWait(driver, 20).until(
            #     ec.element_to_be_clickable((By.XPATH,
            #                                 "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[6]/div/div[2]//button")))
            # generate_suggestions.click()
            # time.sleep(10)
            # # Click on Some Points
            # for j in range(1, 4):
            #     WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            #         (By.XPATH,
            #          f"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[6]/div/div[2]/div/div/div[{j}]//button"))).click()
            #     time.sleep(1)

            # Click on Save Button
            save = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/button")
            save.click()
            time.sleep(5)

            # Back to Companies Button
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']//button")))
            back_to_company.click()
            time.sleep(2)


ref = Addcompany()
ref.login()
i = 0
s = 0
ref.addcompany(i)
ref.addrole(s)
i = 1
s = 1
ref.addcompany(i)
ref.addrole(s)
i = 2
s = 2
ref.addcompany(i)
ref.addrole(s)


