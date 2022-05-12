from selenium.webdriver.common.by import By

class ServicePageLocators():
    POST_FORM = (By.XPATH, '//*[@id="postform-text"]')
    POST_NAME = (By.XPATH, '//*[@id="postform-name"]')
    PASTE_EXPIRATION = (By.XPATH, '//*[@id="w0"]/div[5]/div[1]/div[2]/div/span/span[1]/span/span[2]')
    CHOOSE_NUMB = (By.XPATH, '//li[contains(text(), "10 Minutes")]')
    BUTTON = (By.XPATH, '//*[@id="w0"]/div[5]/div[1]/div[8]/button')
    SYNTAX = (By.XPATH, '//*[@id="w0"]/div[5]/div[1]/div[1]/div/span/span[1]/span/span[2]')
    CHOOSE_BASH = (By.XPATH, '//li[contains(text(), "Bash")]')
    BASH = (By.XPATH, '//ol[@class ="bash"]')
    TITLE =(By.XPATH, '//h1') #/html/head/title
    SHOOLD_BE_BASH = (By.CLASS_NAME, "bash")

class CalcLocators():
    FIND=(By.XPATH, '//div[@class ="devsite-search-container"]')
    SEARCH=(By.XPATH, '//div[@class ="devsite-searchbox"]/input')
    OPEN_LINK=(By.XPATH, '//div[@class="gs-title"]/a[@data-ctorig="https://cloud.google.com/products/calculator"]')
    IFRAME=(By.XPATH, '//devsite-iframe/iframe')
    IFRAME1 = (By.ID, 'myFrame')
    NUMBER_OF_INSTANCE=(By.XPATH, '//input[@ng-model="listingCtrl.computeServer.quantity"]')
    SELECT_VALUE=(By.XPATH, '')
    FREE=(By.XPATH, '')




