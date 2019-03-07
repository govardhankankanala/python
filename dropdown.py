import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



driver= webdriver.Firefox()
#driver= webdriver.Chrome("E:\QA\Resource\WEBDRIVER\chromedriverserver\chromedriver.exe")
driver.get("https://www.hostblast.online/clientarea.php")


emailid = driver.find_element_by_id("inputEmail")
emailid.send_keys("govardhankankanala11@gmail.com")


passw=driver.find_element_by_id("inputPassword")
passw.send_keys("Sg@1107125")


signin=driver.find_element_by_id("login")
signin.click()
time.sleep(15)

select = Select(driver.find_element_by_xpath("/html/body/section[2]/nav/div/div[2]/ul[1]/li[7]/a"))
all_selected_options = select.all_selected_options
options = select.options
#serv = driver.find_element_by_xpath("/html/body/section[2]/nav/div/div[2]/ul[1]/li[7]/a")
#serv.click()

#element = driver.find_element_by_xpath("/html/body/section[2]/nav/div/div[2]/ul[1]/li[6]/a").send_keys("Downloads")
#element.click(Downloads)
#all_options = element.find_elements_by_tag_name("Support")
#for option in all_options:
#    print("Downloads is: %s" % option.get_attribute("Downloads"))
#   option.click()