import time
import unicodedata
import json
from bs4 import BeautifulSoup
from common import *

driver.get("https://apps.unnes.ac.id/")
window_before = driver.window_handles[0]
click("g-signin2", By.CLASS_NAME)

#switch to login window
print('loging in')
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
send_keys(username, '//input[@type="email"]', By.XPATH)
click('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div', By.XPATH)

# isi password
send_keys(password, "password", By.NAME)

# next
click("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div", By.XPATH)
driver.switch_to.window(window_before)

# go to elena dashboard
print('Going to Elena')
click("//a[contains(@href, 'https://apps.unnes.ac.id/30')]", By.XPATH)
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
click("//input[contains(@class, 'btn btn-lg btn-primary')]", By.XPATH)
click("//a[contains(text(), 'Go to calendar...')]", By.XPATH)

#making soup
print('Retrieving Assignment from Calendar')
soup = BeautifulSoup(driver.page_source, 'lxml')

assignment_list = []
for result in soup.find_all("div", class_="card rounded"):
    assignment = dict()
    assignment['title'] = result.find('h3', class_="name").string
    desc_list = result.find('div', class_="description card-body").text.strip().split('\n')
    desc_list = [unicodedata.normalize("NFKD", i) for i in desc_list if i] 
    assignment['due_date'] = desc_list[0]
    assignment['type'] = desc_list[1]
    assignment['description'] = desc_list[2]
    assignment['class'] = desc_list[3]
    assignment_list.append(assignment)

print(assignment_list)

with open('assignment.json', 'w', encoding='utf-8') as f:
    json.dump(assignment_list, f, ensure_ascii=False, indent=4)