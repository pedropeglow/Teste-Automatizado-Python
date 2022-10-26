import time
import warnings

from selenium.webdriver.support.wait import WebDriverWait

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def testLoginSucess(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(4)
        usuario = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        usuario.send_keys("standard_user")
        usuario.send_keys(Keys.RETURN)
        senha = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        senha.send_keys("secret_sauce")
        senha.send_keys(Keys.RETURN)
        botaoLogin = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        botaoLogin.click()
        time.sleep(10)
        self.assertNotIn("No results found.", driver.page_source)

    def testLoginWrongPassword(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(4)
        usuario = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        usuario.send_keys("standard_user")
        usuario.send_keys(Keys.RETURN)
        senha = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        senha.send_keys("wrong_password")
        senha.send_keys(Keys.RETURN)
        botaoLogin = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        botaoLogin.click()
        time.sleep(10)
        self.assertNotIn("No results found.", driver.page_source)


    def testLogout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(4)
        usuario = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        usuario.send_keys("standard_user")
        usuario.send_keys(Keys.RETURN)
        senha = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        senha.send_keys("secret_sauce")
        senha.send_keys(Keys.RETURN)
        botaoLogin = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        botaoLogin.click()
        time.sleep(3)
        menu = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
        menu.click()
        time.sleep(3)
        logout = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")
        logout.click()
        time.sleep(10)
        self.assertNotIn("No results found.", driver.page_source)

    def testMarket(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(4)
        usuario = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        usuario.send_keys("standard_user")
        usuario.send_keys(Keys.RETURN)
        senha = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        senha.send_keys("secret_sauce")
        senha.send_keys(Keys.RETURN)
        botaoLogin = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        botaoLogin.click()
        time.sleep(3)
        addToCart = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        addToCart.click()
        time.sleep(3)
        checkCart = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        checkCart.click()
        time.sleep(10)
        self.assertNotIn("No results found.", driver.page_source)
        
    def testOrder(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(4)
        usuario = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        usuario.send_keys("standard_user")
        usuario.send_keys(Keys.RETURN)
        senha = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        senha.send_keys("secret_sauce")
        senha.send_keys(Keys.RETURN)
        botaoLogin = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        botaoLogin.click()
        time.sleep(3)
        order = driver.find_element(by=By.XPATH, value="//html/body/div/div/div/div[1]/div[2]/div[2]/span/select")
        order.click()
        time.sleep(3)
        priceLowToHigh = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[3]")
        priceLowToHigh.click()
        time.sleep(10)
        self.assertNotIn("No results found.", driver.page_source)

    

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()