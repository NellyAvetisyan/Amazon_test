# from selenium import webdriver
from selenium.webdriver.common.by import By


class NavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def click_to_navigation_bar(self):
        cartrButtonElement = self.driver.find_element(By.ID, "nav-cart-text-container")
        cartrButtonElement.click()


