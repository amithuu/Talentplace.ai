import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec\


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

email = "autotest64@g.co"
password = "New@1234"
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

class Projects():

    def login(self):
        driver.get("https://test-talentplace.vercel.app/login")
        driver.maximize_window()
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        editprofile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        editprofile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Projects']")))
        exp.click()
    def projects(self):
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


ref = Projects()
ref.login()
ref.projects()
