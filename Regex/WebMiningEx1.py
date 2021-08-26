import requests
import re
from tabulate import tabulate
table=[['level 1', 'level2']]
def link_tree(str):
	req_obj=requests.get((str))
	str1 = req_obj.text 
	substr = "href"
	result = [_.start() for _ in re.finditer(substr, str1)]
	x = 0
	for i in range(len(result)):
        	b = str1.find('"',result[i]+6)
        	c = str1.find("'", result[i]+6, b)
        	if(str1[result[i]+6] == 'h'):
            		c = str1.find("'", result[i]+6, b)
            		x +=1
            		if(c!=-1):
                		print(str1[result[i]+6:c])
            		else:
                		table.append([[str,str1[result[i]+6:b]]]); 
a = requests.get('https://vit.ac.in/')
str1 = a.text
substr = "href"
result = [_.start() for _ in re.finditer(substr, str1)]
x = 0
links=[]
for i in range(len(result)):
        b = str1.find('"',result[i]+6)
        c = str1.find("'", result[i]+6, b)
        if(str1[result[i]+6] == 'h'):
            c = str1.find("'", result[i]+6, b)
            x +=1
            if(c!= -1):
                print(''); 
            else:
                links.append(str1[result[i]+6:b])
print("No. of urls found : " + str(x))
# Now we have all the links in the list with name links, now calling the fuunction to generate the table
first_link=links[1]; link_tree(first_link)
second_link=links[2]; link_tree(second_link)
print(tabulate(table))