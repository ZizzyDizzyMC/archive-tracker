import argparse
import sqlite3

# Get args for input
parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

# Default database connection
conn = sqlite3.connect('database.db')
db = conn.cursor()

# Open the file in question and read the lines directly into the db.
with open(args.file) as f:
    for line in f:
        item = (line.strip(),'None','None')
        print(line.strip())
        db.execute('INSERT INTO link_urls ( url, status, username) VALUES (?,?,?)', item)

# Close the db connection
conn.commit()
conn.close()