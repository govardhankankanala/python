import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import html.parser
from html.parser import HTMLParser

import unittest

driver = webdriver.Chrome(r'C:\Users\gk24477\Desktop\Work\chromedriver.exe')

driver.get("https://releaselifecyclemanagement.citigroup.net/brpm/requests/1215669")


emailid = driver.find_element_by_id("user_login")
emailid.send_keys("gk24477")

passw=driver.find_element_by_id("user_password")
passw.send_keys("Lordrama@1107")
driver.find_element_by_xpath("//*[@id='login_box']/div[4]").click()
driver.get("https://releaselifecyclemanagement.citigroup.net/brpm/requests/730114")
time.sleep(10)


ids = driver.find_elements_by_xpath('//*[@*]')
outF = open("myOutFile.txt", "w")
for ii in ids:
    #print ii.tag_name
	outF.write(ii.get_attribute('id'))
	outF.write("\n")
    #print(ii.get_attribute('id'))
	 #with open("test.txt", "w") as myfile:
       #myfile.write(string)
outF.close()


xelm = open("test.txt", "w")
with open("myOutFile.txt","r") as f:
  line=f.readlines()
for text in line:
    if re.search('select', text):
	    for output in text:
             xelm.write(output)
          #output=print(text)
		  
xelm.close()		 
elist = []	  
xp=open('test.txt')
lines=xp.readlines()
for words in lines:
  index=words[5:12]
  elist.append(index)
  
#i=elist[0]
#for i in x:
#s='//*[@id="step__select"]'
driver.find_element_by_xpath("//*[@id='sidebar']/div[1]/div[2]/p/a").click()
time.sleep(10)


#######Step1 #####
#s1='driver.find_element_by_xpath("//*[@id=\'step__1_heading\']/td[15]/form[1]/input[2]").click()'
#refresh=s1[:44]+i+s1[44:]
#exec(refresh)

#s='driver.find_element_by_xpath("//*[@id=\'step__select\']").click()'
#check=s[:44]+i+s[44:]
#exec(check)

#s2='driver.find_element_by_xpath("//*[@id=\'step__1_heading\']/td[15]/a[1]/img").click()'
#edit=s2[:44]+i+s2[44:]
#exec(edit)
#time.sleep(3)
#driver.window_handles
#time.sleep(3)
#driver.find_element_by_xpath("//*[@id='st_automation']/a").click()
#time.sleep(2)

######Step2####

j=elist[5]

#l1='driver.find_element_by_xpath("//*[@id=\'step__select\').click()'
#edit=l1[:44]+j+l1[44:]
#exec(edit)
#time.sleep(3)
l2='driver.find_element_by_xpath("//*[@id=\'step__5_heading\']/td[15]/a[1]").click()'

refresh=l2[:44]+j+l2[44:]
exec(refresh)
time.sleep(1)
#driver.window_handles
driver.current_window_handle
time.sleep(1)
dd=Select(driver.find_element_by_xpath("//*[@id='step_runtime_phase_id']"))
dd.select_by_index(3)
driver.find_element_by_xpath("//*[@id='new_step_form']/div[4]/div[2]/input").click()
time.sleep(1)
k=elist[8]

lastedit=l2[:44]+k+l2[44:]
driver.current_window_handle
exec(lastedit)
time.sleep(1)
driver.current_window_handle
driver.find_element_by_xpath("//*[@id='st_automation']/a").click()
time.sleep(2)
#chg=driver.find_element_by_class_name('step_script_argument')

chg=driver.find_element_by_id("script_argument_11420")
chg.send_keys("CHG123")

driver.find_element_by_xpath("//*[@id='argument_11100']/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='save_data_retriever']").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='argument_11103']/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='save_data_retriever']").click()
time.sleep(2)
#driver.find_element_by_xpath("//*[@id='step_form_holder_tr_div']/div[2]/div/input").click()
driver.find_element_by_css_selector('#new_step_form > div.button_bar.options > div.form_action_btns > input[type="button"]').click()
