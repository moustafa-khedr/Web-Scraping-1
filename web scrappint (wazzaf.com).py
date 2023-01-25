#moustafa khedr
#1st step install and import modules

import requests
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import zip_longest

jop_title = []
skills = []
company_name = []
company_location = []
links = []
salary = []
jop_requrement = []
date = []
page_number = 0

while True:
    #2nd step use requests to fetch the url
    try:
        url = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_number}")   # page link who would to get information's
        #print(url)  #as test to work <200>

        #3rd step save a page content /markup
        scr = url.content     # save all content of page in varible
        #print(scr)  # as test to work all html for page

        #4th step creat soup object to parse content
        soup = BeautifulSoup(scr, "lxml")   #creat object(any name) form class (page i need to get information , parsr to do prosse on information page)
        # print(soup)    # as test to work
        page_limit = int(soup.find("strong").text)

        if (page_number > page_limit // 15):
            print("pages ended,terminate")
            break


        #5th step find the elements containing info we need
        #-- jop titles, jop skills, company names, company location,
        jop_titles = soup.findAll("h2",{"class":"css-m604qf"})   #find all("tag" , Characteristics of the element in dictionary{"class":"value"}
        #print(jop_titles)  #as a test (see end page to sure the content)

        company_names = soup.findAll("a",{"class":"css-17s97q8"})
        #print(company_names)

        company_locations = soup.findAll("span",{"class":"css-5wys0k"})
        #print(company_location)

        jop_skills_all = soup.findAll("div",{"class":"css-y4udm8"})
        posted_new = soup.findAll("div",{"class":"css-4c4ojb"})
        posted_old = soup.findAll("div",{"class":"css-do6t5g"})
        posted = [*posted_new,*posted_old]


        #print(jop_skills_all)

        #6th step loop over returned lists to extract needed info into other lists
        for i in range(len(jop_titles)):   #loop to get information for list as text
            jop_title.append(jop_titles[i].text)    #save info in a new list (::chang a name of list::) as text for every item
            links.append(jop_titles[i].find("a",{"class":"css-o171kl"}).attrs['href'])
            company_name.append(company_names[i].text)
            company_location.append(company_locations[i].text)
            skills.append(jop_skills_all[i].text)
            date_text = posted[i].text.replace("-","").strip()
            date.append(date_text)


        #print(skills)  # as test for anew list
        #print(jop_title, company_name, company_location, skills)
        page_number +=1
        print("page switched")
    except:
        print("error occurred")
        break

'''
for link in links:
    result = requests.get("https://wuzzuf.net/"+link)
    scr = result.content
    soup = BeautifulSoup(scr, "lxml")
    salaries = soup.findAll("span",{"class":"css-47jx3m"})
    salary.append(salaries.text)
    jop_requrements = soup.find("div",{"class":"css-1t5f0fr"}).find("p")
    respon_text =""
    for li in jop requrement.findall("li"):
        respon_text += li.text+"| "
     respon_text =  respon_text[:-2]    
    jop_requrement.append()    
'''



#7th step creativ csv file and fill it with values
file_list = [jop_title, company_name, date, company_location, skills,links, salary, jop_requrement]    #varible to save all list
exported = zip_longest(*file_list)     #varible to save unpaking list with (*) and zip_longest to take index[0] form all an put this in new list and take index[1] etc.

with open("python_jops.csv","w") as myfile:   #to open file (pasth or name file , prosse in file)  as (name to using in code )
    wr = csv.writer(myfile)     #take object form module csv with func(writer)(name file using ) to write in file
    wr.writerow(["jop_title", "company_name","date", "company_location", "skills", "salary", "jop_requrement"])   #put a items as one item in list
    wr.writerows(exported)   #to put lists in new_lines

#8th step to fetch the link of the jop and fetch in page details
#--- salary , jop requrements

#9th step is to do the above for all pages

#10th step is to optimaize code and clean data

