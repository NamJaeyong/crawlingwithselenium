from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'


driver = webdriver.Chrome('./chromedriver')
driver.get(url)

ranks = driver.find_elements_by_css_selector('#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul')

texts = [rank.text for rank in ranks]

with open('result.txt', 'w', encoding='utf-8') as f:
 for text in texts:
     f.write(text+'\n')

driver.quit()