from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from reader import convert_audio

url="https://www.angelone.in/smart-money/trading-courses/technical-trading-indicators"
path=r"C:\Users\ayush\Desktop\chromedriver.exe"
sev=webdriver.ChromeService(executable_path=path)
b= webdriver.Chrome( service=sev, options= webdriver.ChromeOptions())
sections_len=0
lesson_len=0
sections=[1,2,3]
lessons=[1,2,3]
b.get(url)
'''
# x=b.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/section/div/div/div/div[1]/section/div/ol/li/p/a')
try:
    m=b.find_elements(By.XPATH, "//*[@id=\"wzrk-cancel\"]")
    m[-1].click()
except:
    print("some error occoured")
# /html/body/div[1]/main/div[2]/div/div/div[2]/div[2]/h2/button
sections=b.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/section/div/div/div/div/h2/button/div[1]/p[1]/a')

sections=b.find_element(By.XPATH, "//*[@id=\":R6kp7rpja:\"]")
b.execute_script("scrollBy(0,1300);")
sleep(5)
sections.is_enabled()
sections.is_selected()
b.execute_script("arguments[0].click();", sections)
sections.click()
b.execute_script("arguments[0].click();", sections)
sections.click()


sections=b.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/section/div/div/div/div/h2/button/div[1]/p[1]/a')
sections_len=len(sections)
'''
# for i in range(len(sections)):
j = 2
itr = 0
while(j-1>itr):
    itr+=1
    b.get(url)
    sleep(5)
    # x=b.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/section/div/div/div/div[1]/section/div/ol/li/p/a')
    # try:
    #     m=b.find_elements(By.XPATH, "//*[@id=\"wzrk-cancel\"]")
    #     m[-1].click()
    # except:
    #     print("already clicked")
    # sections=b.find_elements(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div/section/div/div/div/div/h2/button/div[1]/p[1]/a')
    # sections_len=len(sections)
    # sleep(3)
    # sections[i].click()
    
    lessons=b.find_elements(By.PARTIAL_LINK_TEXT,"Start")
    j=max(len(lessons),j)
    # b.execute_script(f'b.find_elements(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/section/div/div/div/div/h2/button/span")[2].click()')
    lessons[itr].click()
    sleep(5)
    sleep(5)
    x1=b.find_element(By.XPATH, '//html/body/div[1]/main/div/div/main/section/div[2]/div[2]/div[1]/div[1]/h1')
    x2=b.find_element(By.XPATH, '//html/body/div[1]/main/div/div/main/section/div[2]/div[2]/div[3]/div[2]/div')
    convert_audio(x1,x2,4)

