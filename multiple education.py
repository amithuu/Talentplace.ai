import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec\


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

class Projects():

    def projects(self):

ref = Projects()
ref.projects()