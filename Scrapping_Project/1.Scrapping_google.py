import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup
import requests
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.google.co.kr/search?q=%EC%82%AC%EC%9E%90&sxsrf=ALeKk02at7-a-IKSNP1T4yOe3rUCsS9OnA:1612090380047&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiN4srTgMbuAhXCAYgKHR57DIgQ_AUoAXoECAIQAw&biw=602&bih=649&dpr=1.5'
chrome_options = Options()
# chrome_options.add_argument('--headless') # CLI 환경으로 만듬
browser = webdriver.Chrome(options = chrome_options,\
executable_path='C:/Users/sw993/Project/chrome/chromedriver')
# Selenium 을 써야하는 이유 -> 현재 일반적으로 Requests 모듈 쓸 경우 대부분 막혀 있음
# Selenium 으로 해도 막혀 있다.
# Google은 되는데 Naver는 막혀 있음

browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')
time.sleep(3)
browser.quit()

lists = soup.select('div#islrg > div > div > a > div > img')
for list in lists:
    if list.get('data-src') == None:
        pass
    else:
        print(list.get('data-src'))
