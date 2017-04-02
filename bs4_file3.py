import requests
from bs4 import BeautifulSoup
import MySQLdb
conn= MySQLdb.Connect('localhost', 'USERNAME','PASSWORD','DB_NAME')
mycursor = conn.cursor()
mycursor.execute("select * from bs4_table3")
d1 = mycursor.fetchall()
c1=0
for row in d1 :
	url="http://www.gsmarena.com/"+row[4]
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	data = soup.find_all("tr")
	c,flag=0,0
	st1 = str(row[0])
	c1=c1+1
	for i in range(len(data)-1,0,-1) :
		c=c+1
		try :
			string = str(data[i].find("a").get_text())
			string1 = str(data[i].find("td",{"class":"nfo"}).get_text())
			if string=="Price group" :
				if string1[1]=="0" :
					s2 = string1[:2]
				else :
					s2 = string1[0]
				#print(c1,s2,row[3])
				mycursor.execute("insert into bs4_table4(id, price, model) values('" + str(st1) + "', '" + str(s2) + "', '" + row[3] + "')")
				conn.commit()
				flag=1
				break
		except :
			if c>15 and flag!=1 :
				s2=str(-1)
				mycursor.execute("insert into bs4_table4(id, price, model) values('" + str(st1) + "', '" + str(s2) + "', '" + row[3] + "')")
				conn.commit()
				#print(c1,s2,row[3])
		else :
			if c>15 and flag!=1 :
				s2=str(-1)
				mycursor.execute("insert into bs4_table4(id, price, model) values('" + str(st1) + "', '" + str(s2) + "', '" + row[3] + "')")
				conn.commit()
				#print(c1,s2,row[3])
				flag=1
				break
    
