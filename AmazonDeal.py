import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.amazon.in/')
soup=BeautifulSoup(r.text,'html.parser')
today_deal=soup.find('div',class_='a-cardui-header as-title-block')
header_today_deal=today_deal.h2.text; print(header_today_deal)
link_today_deals=today_deal.a['href']; 
final_link="amazon.in"+link_today_deals; print(final_link)
