from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

url='https://www.census.gov/data/datasets.html'
driver=webdriver.Chrome()

driver.get(url)
time.sleep(5)
soup=BeautifulSoup(driver.page_source, 'html.parser')

#print(soup)


Bigger_contents=[]
page=[1,2,3,4,5]

for x in page:
    data=soup.find_all('div',class_='article row nested-row no-gutter ng-binding ng-scope')

    time.sleep(8)
    contents=[]
    for item in data:
       
        store={}
        title=item.find('div',class_='uscb-default-x-column-title uscb-heading-2 ng-binding').text
        date=item.find('div',class_='uscb-author-text-wrapper uscb-meta-data-text ng-binding ng-scope').text
        store={
            'title':title,
            'date':date
        }
        
        contents.append(store)
    Bigger_contents.append(contents)    
        
    if x<6:

        driver.find_element(By.CLASS_NAME,'nextButton').click()
        
    else:
        break
print(Bigger_contents)



