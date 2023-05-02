import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE link_urls (url,status,username)''')
c.execute('''CREATE INDEX url_index ON link_urls(url)''')
c.execute('''CREATE INDEX username_index ON link_urls(username)''')
c.execute('''CREATE INDEX status_index on link_urls(status)''')
conn.commit()
conn.close()
print("Created Database")