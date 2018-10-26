from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import pandas as pd




zip_list=[35801,99501,85001,72201,94203,90001,80201,"06101",
          19901,20001,33124,30301,96081,83254,60601,46201,
          52801,67201,41701,70112,"04032",21201,"02101",49036,
          55801,39530,63101,59044,68901,89501,"03217","07039",
          87500,10001,27565,58282,44101,74101,97201,15201,
          "02840",29020,57401,37201,78701,84321,"05751",24517,
          98004,25813,53201,82941]
state=[
"AL","AK","AZ","AR","CA","CA","CO","CT","DE","DC",
"FL","GA","HI","ID","IL","IN","IA",'KS',"KY","LA",
"ME","MD","MA","MI","MN","MS","MO","MT","NE","NV",
"NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA",
"RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]



def url(pg,zpcd):
	return "https://www.cars.com/for-sale/searchresults.action/?page="+str(pg)+"&perPage=100&rd=150&searchSource=PAGINATION&showMore=true&sort=relevance&stkTypId=28881&zc="+str(zpcd)
	
	
	
for j in range(52):#52 zipcodes and state names
	print("zipcode: "+str(zip_list[j]))
	czpdf=[]
	for i in range(50):
		read=urlopen(url(i,zip_list[j])).read()
		soup = BeautifulSoup(read, "lxml")
		match1=soup.findAll("script")[1]
		scriptlis = re.findall('(?si)CARS.digitalData = (.*?)</script>', str(match1))
		data=json.loads((scriptlis[0])[:-2])
		pddf=pd.DataFrame((data)["page"]['vehicle'])
		czpdf.append(pddf)
		print("page"+str(i)+"finish append")
	dfwriter=pd.concat(czpdf)
	dfwriter["state"]=state[j]
	with open('carscom.csv', 'a') as f:
		dfwriter.to_csv(f, header=True)
	
	

		
