import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
email = "sozolebur@mailinator.com"
password = "New@1234"
publicationtitle = ["publication1","publication2","publication3"]
publicationid = ["123", "1234", "12345"]
publicationdate = ["02/02/1999", "03/03/2020", "02/04/1898"]
publicationurl = ["https://test-talentplace.vercel.app/edit-resume/publication", "https://test-talentplace.vercel.app/edit-resume/portfolio", "https://test-talentplace.vercel.app/edit-resume/causes"]
selects = ["Mr", "Ms", "Mrs"]
name = ["amith0", "amith1", "amith2"]
linkdinlink = ["https://www.linkedin.com/in/amith-kulkarni-1326241b4", "https://www.linkedin.com/in/amith-kulkarni-1326241b4","https://www.linkedin.com/in/amith-kulkarni-1326241b4"]
descriptions = ["hiii i am writing description about my Publication 1", "hiii i am writing description about my Publication 2", "hiii i am writing description about my Publication 3"]

class Publication():

    def login(self):
        driver.get("https://www.talentplace.ai/login")
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

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Publication']")))
        exp.click()
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
            back = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[1]")))
            back.click()
            # Next
            next_ = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div/div[2]/button[2]")))
            next_.click()
            time.sleep(2)


ref = Publication()
ref.login()
ref.publication()
