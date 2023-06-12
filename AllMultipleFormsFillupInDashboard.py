import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
k=1
name = "Autotest"
email = f"prod1@g.co"
password = "New@1234"
location = "Bengaluru, Karnataka, India"
phone_number = f"+1 1231449771"

# Company variables
companyname = ["cognizant", "dell", "ibm"]
jobtype = ["full time", "intern", "part time", "freelanc", "contract"]
industryexp = ["Advanced Technologies", "IT Services", "Agri-business"]
orgtype = ["startup", "small", "mnc"]
based = ["product", "service", "both"]
location = ["Bangalore", "delhi", "america"]

# Designation variables
designationrole = ["Developer", "Automation", "application"]
managementlevel = ["jun", "sen", "mid"]
functionalarea = ["development", "human", "marketing"]
skilladd = ["java", "python", "c prog"]
expertiserole = ["beg", "skil", "expert"]
startsalary = ["1000", "2000", "3000"]
endsalary = ["10000", "20000", "30000"]

# Projects variables
projectname= ["My Project1", "My Project2", "My Project3"]
associatedwith = ["cognizant", "dell", "ibm"]
projectlink = ["https://test-talentplace.vercel.app/edit-resume/projects", "https://test-talentplace.vercel.app/edit-resume/education", "https://test-talentplace.vercel.app/edit-resume/portfolio"]
descriptions = ["hiii i am writing description about my projects 1", "hiii i am writing description about my projects 2", "hiii i am writing description about my projects 3"]
skilladd = ["java", "python", "c prog"]
skillapplications = ["hiii this is my skill application 1", "hiii this is my skill application 2", "hiii this is my skill application 3"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
endmonth = ["feb", "april", "jan"]
endyear = ["2019", "2020", "2021"]

# Education variables
degreequalification = ["Mca", "BCA", "Mtech"]
universitys = ["REVA UNI", "seshadri", "presid"]
locations = ["Bangalore", "delhi", "america"]
Cgpas= ["8.98", "7.65", "5.09"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
endmonth = ["feb", "april", "jan"]
endyear = ["2019", "2020", "2021"]
skilladd = ["java", "python", "c prog"]
extraactivities = ["!!!!!!!!!!I love playing Cricket!!!!!!!!", "!!!!!!!!!!!!!I love Watching Cricket!!!!!!!", "!!!!!!!!!!!I love Cricket that it!!!!!!!!"]

# Certification variables
certificate_title= ["My Certificate 1", "My Certificate 2", "My Certificate 3"]
institutions = ["Reva", "Isam", "Revam"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
endmonth = ["feb", "april", "jan"]
endyear = ["2019", "2020", "2021"]
skilladd = ["java", "python", "c prog"]
projects = ["hiii i am writing description about my Certificate 1", "hiii i am writing description about my Certificate 2", "hiii i am writing description about my Certificate 3"]

# Publication variables
publicationtitle = ["publication1","publication2","publication3"]
publicationid = ["123", "1234", "12345"]
publicationdate = ["02/02/1999", "03/03/2020", "02/04/1898"]
publicationurl = ["https://test-talentplace.vercel.app/edit-resume/publication", "https://test-talentplace.vercel.app/edit-resume/portfolio", "https://test-talentplace.vercel.app/edit-resume/causes"]
selects = ["Mr", "Ms", "Mrs"]
name = ["amith0", "amith1", "amith2"]
linkdinlink = ["https://www.linkedin.com/in/amith-kulkarni-1326241b4", "https://www.linkedin.com/in/amith-kulkarni-1326241b4","https://www.linkedin.com/in/amith-kulkarni-1326241b4"]
descriptions = ["hiii i am writing description about my Publication 1", "hiii i am writing description about my Publication 2", "hiii i am writing description about my Publication 3"]

# Patent variables
patenttitle = ["Patent1", "Patent2", "Patent3"]
patentid = ["123", "1234", "12345"]
patentdate = ["02/02/1999", "03/03/2020", "02/04/1898"]
patenturl = ["https://test-talentplace.vercel.app/edit-resume/Patent", "https://test-talentplace.vercel.app/edit-resume/portfolio", "https://test-talentplace.vercel.app/edit-resume/causes"]
selects = ["Mr", "Ms", "Mrs"]
name = ["amith0", "amith1", "amith2"]
linkdinlink = ["https://www.linkedin.com/in/amith-kulkarni-1326241b4", "https://www.linkedin.com/in/amith-kulkarni-1326241b4","https://www.linkedin.com/in/amith-kulkarni-1326241b4"]
descriptions = ["hiii i am writing description about my Patent 1", "hiii i am writing description about my Patent 2", "hiii i am writing description about my Patent 3"]

# Portfolio variables
portfoliotitle = ["portfolio1", "portfolio2", "portfolio3"]
linkdinlink = ["https://www.linkedin.com/in/amith-kulkarni-1326241b4", "https://www.linkedin.com/in/amith-kulkarni-1326241b4","https://www.linkedin.com/in/amith-kulkarni-1326241b4"]
descriptions = ["hiii i am writing description about my portfolio 1", "hiii i am writing description about my portfolio 2", "hiii i am writing description about my portfolio 3"]

# Voluntary Roles
roles = ["voluntaryroles1", "voluntaryroles2", "voluntaryroles3"]
organization = ["Reva", "BMSIT", "ISCIT"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
endmonth = ["feb", "april", "jan"]
endyear = ["2019", "2020", "2021"]
descriptions = ["hiii i am writing description about my voluntaryroles 1", "hiii i am writing description about my voluntaryroles 2", "hiii i am writing description about my voluntaryroles 3"]

# Honor and Awards variable
titles = ["voluntaryroles1", "voluntaryroles2", "voluntaryroles3"]
issuers = ["Reva", "BMSIT", "ISCIT"]
startmonth = ["jan", "march", "dec"]
startyear = ["1999", "2000", "2001"]
associatedwith = ["cognizant", "dell", "ibm"]
descriptions = ["hiii i am writing description about my voluntaryroles 1", "hiii i am writing description about my voluntaryroles 2", "hiii i am writing description about my voluntaryroles 3"]

# Hobbies variables
category = ['Sports', 'Travel', 'Books']
hobby = ['Cricket', 'Kerala', 'The untold Story']
# Languages variables
language = ['english', 'kannada', 'Hindi']
proficiency = ['inter', 'adv', 'begin']

class MultipleForms():

    def login(self):
        # driver.get("https://test-talentplace.vercel.app/login")
        driver.get("https://www.talentplace.ai/login")
        driver.maximize_window()
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(4)

        edit_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        edit_profile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Experience']")))
        exp.click()
    def addcompany(self, i):

        add_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button")))
        add_company.click()
        time.sleep(2)

        # Company name
        company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div[1]//input")))
        company.click()
        time.sleep(2)
        company.send_keys(companyname[i])
        company.send_keys(Keys.TAB)
        time.sleep(1)

        job_type = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]//input")))
        job_type.click()
        job_type.send_keys(jobtype[i])
        job_type.send_keys(Keys.TAB)
        time.sleep(1)

        experience = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]//input")))
        experience.click()
        experience.send_keys(industryexp[i])
        experience.send_keys(Keys.TAB)
        time.sleep(1)

        organization = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[3]/div[1]//input")))
        organization.click()
        organization.send_keys(orgtype[i])
        organization.send_keys(Keys.TAB)
        time.sleep(1)

        which_based = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div[3]/div[2]//input")))
        which_based.click()
        which_based.send_keys(based[i])
        which_based.send_keys(Keys.TAB)
        time.sleep(1)

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
            time.sleep(3)
            # Functional Area
            functional_area = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[2]/div[2]/div[1]//input")))
            functional_area.send_keys("Development")
            functional_area.send_keys(Keys.TAB)
            # Skill
            skill = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[1]//input")))
            skill.send_keys(skilladd[a-1])
            skill.send_keys(Keys.TAB)
            # Expertise
            expertise = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[2]//input")))
            expertise.send_keys(expertiserole[a-1])
            expertise.send_keys(Keys.TAB)
            # Add Skill Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[3]/div[2]/div[2]//button"))).click()
            # Start Date and End date
            start_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[1]//input")))
            start_date.send_keys("December")
            start_date.send_keys(Keys.TAB)
            start_date.send_keys("2007")
            end_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='root']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div/div[4]/div[2]//input")))
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
            time.sleep(2)

            # Back to Companies Button
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='css-hboir5']//button")))
            back_to_company.click()
            time.sleep(2)
    def projects(self):
        editprofile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        editprofile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Projects']")))
        exp.click()
        for j in range(3):
            # Add Projects
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button[1]"))).click()
            time.sleep(2)
            # Add Project
            """Projects"""
            # Project Name
            project_name = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/input")))
            project_name.send_keys(projectname[j])
            # Start date
            start_date = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input")
            start_date.send_keys(startmonth[j])
            start_date.send_keys(Keys.TAB)
            start_date.send_keys(startyear[j])
            # End date
            end_date = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input")
            end_date.send_keys(endmonth[j])
            end_date.send_keys(Keys.TAB)
            end_date.send_keys(endyear[j])
            time.sleep(2)
            # Associated with
            associated_with = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]//input")))
            associated_with.click()
            associated_with.send_keys(associatedwith[j])
            associated_with.send_keys(Keys.TAB)
            # Project url
            project_url = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/div[2]//input")))
            project_url.send_keys(projectlink[j])
            # Description
            description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p")))
            description.send_keys(descriptions[j])
            # Skills
            skill = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]/div[2]/div[1]//input")
            skill.send_keys(skilladd[j])
            skill.send_keys(Keys.TAB)
            # Skill Ranger
            slider = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]/div[2]/div[2]//div[@role='slider']")
            ActionChains(driver).move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset((35 * (j+1)), 0).release().perform()
            time.sleep(1)
            # Button '+'
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[5]/div[2]/div[2]//button"))).click()
            # Skill applications
            skill_application = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[6]//p")))
            skill_application.send_keys(skillapplications[j])
            time.sleep(1)
            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/button")))
            save.click()
            time.sleep(4)

            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(1)

        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(1)
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
            loc = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input")
            loc.send_keys(Keys.CONTROL + "a")
            loc.send_keys(locations[i])
            time.sleep(3)
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
            # click_upload_image = driver.execute_script(" return document.getElementsByTagName('u')[0]")
            # driver.execute_script("arguments[0].click();", click_upload_image)
            # time.sleep(5)

            # Save
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div/div[2]/div/div/form/div/button"))).click()
            time.sleep(5)

            # Back
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            next_.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            # Discard
            # discard = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Discard']")))
            # discard.click()
            # time.sleep(2)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
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

            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)

        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)
    def publication(self):
        for i in range(3):
            # Add Publication
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"))).click()
            time.sleep(1)
            """Publication"""
            # Title
            title = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[1]//input")
            title.send_keys(publicationtitle[i])
            # Publication ID
            publisher_id = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input")
            publisher_id.send_keys(publicationid[i])
            # Publication Date
            publisher_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input")))
            publisher_date.send_keys(publicationdate[i])
            # Publication Url
            publication_url = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input")
            publication_url.send_keys(publicationurl[i])
            time.sleep(2)
            # Add Author
            add_author = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]//button")))
            add_author.click()
            time.sleep(1)
            driver.find_element(By.TAG_NAME, value="html").send_keys(Keys.END)
            # Author title
            author_title = Select(driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[1]//select"))
            author_title.select_by_visible_text(selects[i])
            # Author Name
            author_name = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[2]//input")))
            author_name.send_keys(name[i])
            # Author linkdIn link
            linkdin_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[2]//input")))
            linkdin_link.send_keys(linkdinlink[i])
            # Delete Author
            # delete_author = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[2]//button")
            # delete_author.click()
            # Publication Description
            publication_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p")))
            publication_description.send_keys(descriptions[i])
            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/button")))
            save.click()
            time.sleep(3)
            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)
    def patent(self):
        for i in range(3):
            # Add Patent
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"))).click()
            time.sleep(1)
            """Patent"""
            # Title
            title = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[1]//input")
            title.send_keys(patenttitle[i])
            # Patent ID
            patent_id = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input")
            patent_id.send_keys(patentid[i])
            # Patent Date
            patent_date = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input")))
            patent_date.send_keys(patentdate[i])
            # Patent Url
            patent_url = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input")
            patent_url.send_keys(patenturl[i])
            time.sleep(2)
            # Add Author
            add_author = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]//button")))
            add_author.click()
            time.sleep(1)
            # Author title
            author_title = Select(driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[1]//select"))
            author_title.select_by_visible_text(selects[i])
            # Author Name
            author_name = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[2]//input")))
            author_name.send_keys(name[i])
            # Author linkdIn link
            linkdin_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[2]//input")))
            linkdin_link.send_keys(linkdinlink[i])
            # Delete Author
            # delete_author = driver.find_element(By.XPATH, "//*[@role='region']/form/div/div[3]/form/div/div[2]//button")
            # delete_author.click()
            # Patent Description
            patent_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p")))
            patent_description.send_keys(descriptions[i])
            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/button")))
            save.click()
            time.sleep(3)
            # Back
            back = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)
    def portfolio(self):
        for i in range(3):
            # Add portfolio
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"))).click()
            time.sleep(1)
            """portfolio"""
            # Title
            title = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]//input")
            title.send_keys(portfoliotitle[i])

            # Description
            portfolio_description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]//p")))
            portfolio_description.send_keys(descriptions[i])

            # upload_image = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div[1]/div[1]//u")))
            # upload_image.click()
            # time.sleep(2)

            # Links
            link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[2]//input")))
            link.send_keys(linkdinlink[i])

            # Add Button
            add_button = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[2]//button")))
            add_button.click()

            # Delete Button
            # delete_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[1]//button")))
            # delete_link.click()
            # time.sleep(3)

            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/button")))
            save.click()
            time.sleep(3)

            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()

            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)
    def voluntaryroles(self):
        for i in range(3):
            # Add voluntary_roles
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"))).click()
            time.sleep(1)
            """Voluntary_Roles"""
            # Role
            voluntary_role = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]//input")
            voluntary_role.send_keys(roles[i])

            # Organisation
            voluntary_organization = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]//input")))
            voluntary_organization.send_keys(organization[i])

            duration_from = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//input")))
            duration_from.send_keys(startyear[i])
            duration_from.send_keys(Keys.TAB)
            duration_from.send_keys(startyear[i])

            duration_to = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//input")))
            duration_to.send_keys(endmonth[i])
            duration_to.send_keys(Keys.TAB)
            duration_to.send_keys(endyear[i])

            description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]//p")))
            description.send_keys(descriptions[i])

            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button")))
            save.click()
            time.sleep(3)

            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()

            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)
    def honorawards(self):
        for i in range(3):
            # Add voluntary_roles
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"))).click()
            time.sleep(1)
            """Voluntary_Roles"""
            # Title
            title = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]//input")
            title.send_keys(titles[i])

            # Issuer
            issuer = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]//input")))
            issuer.send_keys(issuers[i])

            duration_from = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]//input")))
            duration_from.send_keys(startyear[i])
            duration_from.send_keys(Keys.TAB)
            duration_from.send_keys(startyear[i])

            # Associated With
            associated_with = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]//input")))
            associated_with.send_keys(associatedwith[i])
            associated_with.send_keys(Keys.TAB)

            # Description
            description = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]//p")))
            description.send_keys(descriptions[i])

            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/button")))
            save.click()
            time.sleep(3)

            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()

            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)
    def causes(self):
        time.sleep(4)
        """Causes"""
        # Select The Causes Max[6]
        for i in range(1, 7):
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div[{i}]//span[1]"))).click()
            time.sleep(1)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div/button")))
        save.click()
        time.sleep(3)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)
    def hobbies(self):
        """Hobbies"""
        for i in range(len(category)):
            # Category Select
            categorys = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div[1]//input")))
            categorys.click()
            categorys.send_keys(category[i])
            categorys.send_keys(Keys.TAB)
            time.sleep(1)
            # Hobbies Text
            hobbies = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div[2]//input")))
            hobbies.send_keys(hobby[i])
            # Add Hobbies '+' Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[1]/div[2]//button"))).click()
            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
            save.click()
            time.sleep(2)
            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(1)

        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(2)
    def languages(self):
        time.sleep(2)
        """Languages"""
        for i in range(len(language)):
            # Language Drop Down
            lan = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div/div[1]//input")))
            lan.send_keys(language[i])
            lan.send_keys(Keys.TAB)
            # Proficiency
            prof = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div/div[2]//input")))
            prof.send_keys(proficiency[i])
            prof.send_keys(Keys.TAB)
            # Add + Button
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div/div[2]/div[2]//button"))).click()
            time.sleep(2)
            # Save
            save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
            save.click()
            time.sleep(2)
            # Back
            back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back_to_company.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(1)
        # Next
        next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        next_.click()
        time.sleep(1)
    def cognitive(self):
        time.sleep(4)
        """Cognitive skills"""
        for s in range(1, 7):
            driver.find_element(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div/div/div[{s}]//span[1]").click()
            slid = driver.find_element(By.XPATH,f"//*//*[@id='root']/div[2]/div[2]/div/div/div/div/div[{s}]//div[@role='slider']")
            ActionChains(driver).move_to_element(slid).pause(1).click_and_hold(slid).move_by_offset((35 * s), 0).release().perform()
            time.sleep(1)

        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(2)
        # Back
        back_to_company = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
        back_to_company.click()
    def carrier_summary(self):
        """ADD CARRIER SUMMARY"""
        # Generate Summary
        # driver.set_window_size(1200, 1400)
        # driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        # time.sleep(2)
        # generate_suggestion = WebDriverWait(driver, 20).until(
        #     ec.element_to_be_clickable((By.XPATH, "//button[text()='Generate Suggestions']")))
        # generate_suggestion.click()
        # time.sleep(12)
        # for a in range(1, 4):
        #     driver.find_element(By.XPATH, f"//div[@id='root']/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div{a}//button").click()
        #     time.sleep(1)
        # Save
        save = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save.click()
        time.sleep(4)


ref = MultipleForms()
ref.login()
# i = 0
# s = 0
# ref.addcompany(i)
# ref.addrole(s)
# i = 1
# s = 1
# ref.addcompany(i)
# ref.addrole(s)
# i = 2
# s = 2
# ref.addcompany(i)
# ref.addrole(s)
ref.projects()
ref.education()
ref.certificate()
ref.publication()
ref.patent()
ref.portfolio()
ref.voluntaryroles()
ref.honorawards()
ref.causes()
ref.hobbies()
ref.languages()
ref.cognitive()
ref.carrier_summary()

