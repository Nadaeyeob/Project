# 0. Deep Learning/Machine Learning을 위한 Data 를 쌓기 위한 Project

# 1. Web에서 Image를 취출하여 HW에 저장
# 2. 해당 기능 구현 후 자동화 프로그램으로 만들 것

# 3. 필요한 Image, Excel에 저장 기능 구현
# 3-1. Click
# 3-2. List에 담아 해당 항목만 저장


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os # 파이썬을 쓰고있는 OS에 접근해서 명령어 실행

# Volume / Variety / Velocity

base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus('아이유')
url = base + quote

print(url)

res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
print(soup)

print('------')
# print(soup)
print('------')
img_list = soup.select('img')
print(img_list)
