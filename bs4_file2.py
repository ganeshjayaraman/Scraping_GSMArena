import re
import requests
from bs4 import BeautifulSoup
import MySQLdb
conn= MySQLdb.Connect('localhost', 'USERNAME','PASSWORD','DB_NAME')
mycursor = conn.cursor()
mycursor.execute("select * from bs4_table")
d = mycursor.fetchall()
co=0
for row in d :
	url1="http://www.gsmarena.com/"+row[1]
	r1 = requests.get(url1)
	soup1 = BeautifulSoup(r1.content, "html5lib")
	data2=soup1.find_all("div",{"class":"makers"})
	res=data2[0].find_all("li")
	st1,st2 = str(1),str(row[3])
	for i in range(len(res)) :
                co=co+1
		try :
                        s1 = str(res[i].find("a").get("href"))
		        s2 = str(res[i].get_text())
                        mycursor.execute("insert into bs4_table3(id, url, brand, model, url2, processed) values('" + str(st2) + "', '" + str(row[1]) + "', '" + str(row[0]) + "', '" + str(s2) + "', '" + str(s1) + "', '" + str(st1) + "')")
		        conn.commit()
		except :
                        #if "'" in s2 :
                                #s2.replace("'","")
                        s2 = re.sub('[^a-zA-Z0-9\n\.]', ' ', s2)
                        mycursor.execute("insert into bs4_table3(id, url, brand, model, url2, processed) values('" + str(st2) + "', '" + str(row[1]) + "', '" + str(row[0]) + "', '" + str(s2) + "', '" + str(s1) + "', '" + str(st1) + "')")
                        conn.commit()
		#print(co,st2,row[0],row[1],s2,s1)
	data1 = soup1.find_all("div",{"class":"nav-pages"})
	for i in data1 :
		s=i.find_all("a")
		for j in range(len(s)) :
			s1 = str(s[j].get("href"))
			url2 = "http://www.gsmarena.com/"+s1
			r2 = requests.get(url2)
			soup2 = BeautifulSoup(r2.content, "html5lib")
			data3=soup2.find_all("div",{"class":"makers"})
			res3=data3[0].find_all("li")
			st1,st2 = str(1),str(row[3])
			for i in range(len(res3)) :
                                co=co+1
				try :
                                        s3 = str(res3[i].find("a").get("href"))
				        s2=str(res3[i].get_text())
                                        mycursor.execute("insert into bs4_table3(id, url, brand, model, url2, processed) values('" + str(st2) + "', '" + str(row[1]) + "', '" + str(row[0]) + "', '" + str(s2) + "', '" + str(s3) + "', '" + str(st1) + "')")	
                        		conn.commit()
                        	except :
                                        #if "'" in s2 :
                                                #s2.replace("'","")
                                        s2 = re.sub('[^a-zA-Z0-9\n\.]', ' ', s2)
                                        mycursor.execute("insert into bs4_table3(id, url, brand, model, url2, processed) values('" + str(st2) + "', '" + str(row[1]) + "', '" + str(row[0]) + "', '" + str(s2) + "', '" + str(s3) + "', '" + str(st1) + "')")
                                        conn.commit()
				#print(co,st2,row[0],row[1],s2,s3)


