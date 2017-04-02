import requests
from bs4 import BeautifulSoup
import MySQLdb
conn= MySQLdb.Connect('localhost', 'USERNAME','PASSWORD','DB_NAME')
mycursor = conn.cursor()
url="http://www.gsmarena.com/makers.php3"
r = requests.get(url)
soup = BeautifulSoup(r.content)
data= soup.find_all("td")
for i in range(0,len(data)-1,2) :
    b = str(data[i].find("a").get("href"))
    c = str(data[i+1].find("a").get_text())
    mycursor.execute("insert into bs4_table(brand, url, processed) values ('" + str(c) + "', '" + str(b)  + "', 0)")
    conn.commit()
    #print(c,b)

    
