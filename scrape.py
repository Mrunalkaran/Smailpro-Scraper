from selenium import webdriver
import time
import re

driver = webdriver.Chrome()
driver.get("https://smailpro.com/")
time.sleep(3)
for x in range(50000):
        button = driver.find_element_by_id('btnChange')
        button.click()
        time.sleep(1)
        doc = driver.page_source

        emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
        email = emails[0]
        datafile = open('email1.txt','r').read()
        if email in datafile:
                print(email+" already exist")
        else:
                f=open("email1.txt", "a+")
                f.write(email+"\n")
                print("scaping "+str(x)+" email: "+emails[0])
