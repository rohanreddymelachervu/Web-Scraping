import requests
import sys 
import os 
from bs4 import BeautifulSoup
# Initializing a set to store visited links
visited_links=set()
# Defining the paths
pages_path1 = 'Crawled-URL-pages\\'
pages_path = os.path.join(os.getcwd(),pages_path1)
# Function to read seed.txt file 
def initialize_Frontier(str):
    try:
        f=open(str,"r")
        temp_list=[]
        temp_list.append(f.read())
    except: pass
    return temp_list
# Function to add a link to the frontier, takes filename and frontier as parameter and returns the frontier 
def enqueue(str,li):
    li.append(str)
    return li
# Function to dequeue a link for it to be crawled. takes the frontier as parameter and returns the link and frontier 
def dequeue(li):
    temp_URL=li.pop(0)
    return temp_URL,li
# Function to write the visited links to a text file in a directory. 
def writeToFile(k):
    try:
        f=open("Crawled URLS-temp.txt","w+")
        for i in k:
            f.write(i)
            f.write("\n")
    except: pass
# Function to get content of a web page link and write to separate text files in the same directory
def writeContentToFile(str1,r,pages_path):
    dir=pages_path+str1+".txt"
    f=open(dir,"w+",encoding='utf-8')
    f.write(r)
 # Initialize the frontier link 
seed=initialize_Frontier("seed1.txt")
# Set a counter for number of crawls
counter=90
try:
    pages_path2 = os.mkdir(os.path.join(os.getcwd(),pages_path1))
except: pass
n=0
# while the length of the frontier is greater than zero
while(len(seed)>0):
   temp_URL,seed=dequeue(seed)
   if(temp_URL not in visited_links):
    try:
        soup=(BeautifulSoup(requests.get((temp_URL)).text,'html.parser')) # Scrape content 
        n+=1
        for link in soup.find_all('a'):
            try: 
                temp_text=soup.text.strip()
                writeContentToFile("WebPage"+str(n),temp_text,pages_path)
                temp=link['href'].strip().replace('\\n','')
                seed=enqueue(temp,seed)
            except Exception as e: pass
    except: pass
    counter-=1
    visited_links.add(temp_URL)
    if counter==0: break
writeToFile(visited_links)
