from bs4 import BeautifulSoup
import requests
print("Your unfamiliar skills (Enter over to exit)")
unfamiliar_skills=[] 
unfamiliar_skill=""
while(True):
    unfamilir_skill=input('>') 
    if(unfamilir_skill=="over"): break
    else: unfamiliar_skills.append(unfamilir_skill)
print(f"Filtering out {unfamiliar_skill}"); 
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print("Headers from the website are \n"); print(html_text.headers); print("\n")
soup=BeautifulSoup(html_text.text, 'html.parser')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date=job.find('span',class_='sim-posted').span.text
    if('few' in published_date):
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=job.find('span',class_='srp-skills').text.replace(' ','') 
        for unfamiliar_skill in unfamiliar_skills:
            if unfamiliar_skill not in skills:
                more_info=job.header.h2.a['href']
                print(f"More info: {more_info.strip()}")
                print(f"Company Name: {company_name.strip()}")
                print(f"Skills: {skills.strip()}"); print(' ')
    
