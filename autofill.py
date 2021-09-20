import sqlite3
import random
import editDistance
import time
# The limit for the extended ASCII Character set
def randStrings(i):
    for _ in range(i):
        random_string = ''
        for _ in range(random.randint(30,60)):
            

            random_integer = random.randint(64, 124)
            # Keep appending random characters using chr(x)
            random_string += chr(random_integer)
        yield (random_string,)
print(list(randStrings(200)))
t = time.time()
con = sqlite3.connect("test.db")
con.create_collation("edits", editDistance.collation("fQrkx").collate)
#con.execute("create index idx on strings(name)")
con.execute("create table if not exists strings (name varchar(30) primary key)")
con.executemany("insert into strings(name) values (?)",list(randStrings(60000)))
con.commit()

print(con.execute("select * from strings order by name collate edits desc limit 5").fetchall())
print(time.time() - t)