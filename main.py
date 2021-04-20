import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from multiprocessing import Process
chrome_options = Options()

import art

whichagent = random.uniform(1, 15)
delay = random.uniform(2, 3.5)
readelay = random.uniform(1.5, 3.5)

combospath = str(input('Enter the path to your combos file: '))
print('')
proxiespath = str(input('Enter the path to your proxies file: '))
print('')
target = input('Who do you want to mass report?: ')
print('')
reason = int(input('''
Which reason do you want to report for? (sorted from the most "bannable")
==========================
1) Suicide and self-injury
2) Nudity and sexual activity (CP)
3) Sale of illegal and regulated goods (guns)
4) Violence threats
5) Hate speech
6) Harassment
7) False information
8) Scamming and fraud
9) Spam
==========================
Input the number here: '''))
print('')
accounts = int(input('How many accounts do you have/wanna report from?: '))
print('')
def report():
    chrome_options.add_argument("--headless") #if you want browser windows visible, just comment out this line
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(480, 853)
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button').click()
    time.sleep(5)
    try:
        nocookiespls = driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
        nocookiespls.click()
        print('Successfully logged in with account number ' + str(combonumber))
    except NoSuchElementException:
        print('Unable to login at with account number ' + str(combonumber) + ', terminating that instance now')
        driver.quit()
    time.sleep(1)
    print('')
    driver.get('https://www.instagram.com/' + target)
    time.sleep(2)
    driver.find_element_by_class_name('wpO6b').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[3]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]').click()
    time.sleep(0.7)
    if reason == 1:
        driver.find_element_by_xpath(su1cide).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(submitbutton).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for Suicide and Self-injury')
        print('')
        driver.quit()
    if reason == 2:
        driver.find_element_by_xpath(sactivity).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(cp).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(submitbutton2).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for CP')
        print('')
        driver.quit()
    if reason == 3:
        driver.find_element_by_xpath(goods).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(firearms).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(submitbutton2).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for Sale of firearms')
        print('')
        driver.quit()
    if reason == 4:
        driver.find_element_by_xpath(violence).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(threat).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(submitbutton2).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for Violent threats')
        print('')
        driver.quit()
    if reason == 5:
        driver.find_element_by_xpath(speech).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(submitbutton).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for Hate speech')
        print('')
        driver.quit()
    if reason == 6:
        driver.find_element_by_xpath(harassment).click()
        time.sleep(readelay)
        driver.find_element_by_xpath(someoneyk).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for Harassment')
        print('')
        driver.quit()
    if reason == 7:
        driver.find_element_by_xpath(fakenews).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for False information')
        print('')
        driver.quit()
    if reason == 8:
        driver.find_element_by_xpath(scammaz).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for Scamming and fraud')
        print('')
        driver.quit()
    if reason == 9:
        driver.find_element_by_xpath(spam).click()
        time.sleep(delay)
        print('Successfully reported ' + target + ' for Spam')
        print('')
        driver.quit()

#report xpaths
spam = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]' #does not need submit button
su1cide = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[3]/div/div[1]'
goods = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[4]/div/div[1]' #needs one of checkboxes - firearms
sactivity = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[5]/div/div[1]' #needs one of checkboxes - cp
speech = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[6]/div/div[1]'
violence = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[7]/div/div[1]' #needs one of checkboxes - threat
harassment = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[8]/div/div[1]' #needs one click (someoneyk), doesnt need submit
scammaz = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[10]/div/div[1]' #does not need submit button
fakenews = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[11]/div/div[1]' #does not need submit button
firearms = '//*[@id="igCoreRadioButtontag-1"]'
cp = '//*[@id="igCoreRadioButtontag-3"]'
threat = '//*[@id="igCoreRadioButtontag-0"]'
someoneyk = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]'
submitbutton = '/html/body/div[4]/div/div/div/div[2]/div/div/button'
submitbutton2 = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[6]/button'
#report xpaths

with open(combospath, 'r') as file:
    proxies = open(proxiespath, 'r')
    combonumber = 0
    for jodej in range(accounts):
        combonumber = combonumber + 1
        if whichagent <= 5:
            chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/18.1 Mobile/16B92 Safari/605.1.15"')
        if  5 < whichagent <= 10:
            chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/70.0.3538.60 Mobile/15E148 Safari/605.1"')
        if 10 < whichagent <= 15:
            chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/76.0.3809.81 Mobile/15E148 Safari/605.1"')
        content = file.readline()
        llll = content.split(":")
        username = llll[0]
        password = llll[1]
        proxy = proxies.readline()
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        if __name__ == '__main__':
            Process(target=report).start()
