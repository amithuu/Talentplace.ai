import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
email = "autotest64@g.co"
password = "New@1234"
portfoliotitle = ["portfolio1", "portfolio2", "portfolio3"]
linkdinlink = ["https://www.linkedin.com/in/amith-kulkarni-1326241b4", "https://www.linkedin.com/in/amith-kulkarni-1326241b4","https://www.linkedin.com/in/amith-kulkarni-1326241b4"]
descriptions = ["hiii i am writing description about my portfolio 1", "hiii i am writing description about my portfolio 2", "hiii i am writing description about my portfolio 3"]

class Portfolio():

    def login(self):
        driver.get("https://test-talentplace.vercel.app/login")
        driver.maximize_window()
        """ Login Page"""
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
        time.sleep(3)

        edit_profile = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Edit Profile']")))
        edit_profile.click()

        exp = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Portfolio']")))
        exp.click()
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


ref = Portfolio()
ref.login()
ref.portfolio()

