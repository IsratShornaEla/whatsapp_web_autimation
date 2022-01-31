from email import message
import time
from lib2to3.pgen2 import driver
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\lovin\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver")
driver.get("https://web.whatsapp.com/")


def msg():
    name = input('\nEnter Group/username :')
    message = input("Enter your message to Group/User :")
    Count = int(input("Enter the message count: "))

    #find user seacrh bar
    user = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    user.click()
    time.sleep(5)

    #type user name and click
    user.send_keys(name)
    time.sleep(5)
    name_click = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[7]/div/div/div[2]')
    name_click.click()
    time.sleep(2)

# detecting message box
    text_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

    # send button
    for i in range(Count):
        text_box.send_keys(message)
        text_box.send_keys(Keys.ENTER)


msg()



def reps():
    print("do you wnat to send msdg to anyone?")
    askUser = input("press y for yes & n for No")

    if (askUser == 'Y' or askUser == 'y'):
        msg()
        reps()
    elif (askUser == 'N' or askUser == 'n'):
        print("see you soon!!")
    else:
        print("please insert valid option : \n")
        reps()


reps()