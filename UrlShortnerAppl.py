import sqlite3

class URLShortnerApp:

    id=100000000000
    urls_list = {}
    con = sqlite3.connect("app.db")
    cursor = con.execute(''' SELECT url,shorturl,id from urldb;''')
    c=0
    for i in cursor:
        urls_list[i[0]]=i[2]
        id = i[2]
        c +=1
    id +=1
    def short_url(self,original_url):
        
        if original_url in self.urls_list:
            id=self.urls_list[original_url]
            shorten_url = self.id_range(id)
        
        else:
            self.urls_list[original_url]=self.id
            shorten_url = self.id_range(self.id)
            self.id += 1
        
        return "shorten_url/"+ shorten_url
        

    def id_range(self,id):
        char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(char)
        data = []
        while id > 0:
            val = id % base
            data.append(char[val])
            id = id // base
        return "".join(data[::-1])

shortner= URLShortnerApp()

a = input("Enter your url: ")
print(shortner.short_url(a))


conn = sqlite3.connect("app.db")
var = conn.execute(''' SELECT url,shorturl,id from urldb;''')
count = 1
for i in var:
    
    if (shortner.urls_list[i[0]]==shortner.urls_list[a]):
        print("Entered URL is already available in database..")
        print("your shorten url is: ",i[1])
        break
    elif(count < shortner.c):
        count += 1
    else:
        insert = ''' INSERT INTO urldb(id,url,shorturl)
              VALUES(?,?,?) '''

        data = (shortner.urls_list[a],a,shortner.short_url(a))
        cur = conn.cursor()
        cur.execute(insert, data)
        conn.commit()   
        break
conn.close()