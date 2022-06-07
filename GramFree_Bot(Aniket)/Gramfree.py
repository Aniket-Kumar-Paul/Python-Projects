from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(20)

for j in range(10):
    driver.get('https://gramfree.net/login/')
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/section/div/div/div/div[2]/div/div[2]/div/center/a[2]/img').click()
    driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[{}]/div'.format(j+1)).click()
    try:
        gotofree=driver.find_element_by_xpath('//*[@id="dashboard-analytics"]/div[3]/div[2]/div/div/div/a/button').click()
    except:
        sleep(30)
        gotofree=driver.find_element_by_xpath('//*[@id="dashboard-analytics"]/div[3]/div[2]/div/div/div/a/button').click()
    roll=driver.find_element_by_xpath('//*[@id="roll-button"]').click()
    sleep(10)
    videos=driver.find_element_by_xpath('//*[@id="main-menu-navigation"]/li[9]/a').click()
    for i in range(5):
        watch=driver.find_element_by_xpath('//*[@id="wishlist"]/div[2]/div/div[3]/a/div/span').click()
        sleep(70)
        driver.refresh()
    sc=driver.find_element_by_xpath('//*[@id="main-menu-navigation"]/li[10]/a').click()
    try:
        risky=driver.find_element_by_xpath('//*[@id="place-order"]/div/div[1]/div/div[2]/div[2]/label').click()
        take=driver.find_element_by_xpath('//*[@id="place-order"]/div/div[1]/div/div[3]/button').click()
        sign=driver.find_element_by_xpath('//*[@id="place-order"]/div/div[1]/div/div[3]/div[2]').click()
        yes=driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[1]').click()
    except:
        pass
    for i in range(1,5):
        try:
            confirm=driver.find_element_by_xpath('//*[@id="place-order"]/div/div[{}]/div/div[3]/div[3]'.format(i)).click()
            yes=driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[1]').click()
        except:
            break
    logout=driver.find_element_by_xpath('//*[@id="main-menu-navigation"]/li[12]/a').click()
    
