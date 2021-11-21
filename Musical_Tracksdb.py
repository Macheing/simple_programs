#import libraries (xml & sqlite database)
import xml.etree.ElementTree as ET
import sqlite3

#makes a databse connection
conn = sqlite3.connect('musical_tracksdb.sqlite')
cur = conn.cursor()

# create tables using sql command executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

file_name = input('Enter file name: - ')
if (len(file_name) < 1): file_name = 'Library.xml'

# structure of Library xml file
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

#lookup function to browse the xml file
def lookup(d,key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True  
    return None

#parse xml file
stuff = ET.parse(file_name)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
#print(clean_data)

#iteract through clean_data
for entry in all:
    if (lookup(entry,'Track ID') is None): continue

    #find specific data entry
    title = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry,'Album')
    genre = lookup(entry,'Genre')
    count = lookup(entry,'Play Count')
    rating = lookup(entry,'Rating')
    length = lookup(entry,'Total Time')
    
    #checks for nontype data and skip further computition if true
    if title is None or artist is None or album is None or genre is None:
        continue
    print()
    print('Title:',title)
    print('Artist:',artist)
    print('Album:',album)
    print('Genre:',genre)
    print( 'Play Count:',count)
    print('Rating:',rating)
    print('Play Time:',length)
    
    #execute sql queries based on extracted datasets to populate database
    cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?)',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album(title,artist_id) VALUES(?,?)',(album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track(title,album_id,genre_id,len,rating,count)
                VALUES(?,?,?,?,?,?)''',(title,album_id,genre_id,length,rating,count))
    
    conn.commit()

print()
print('Database query is printed below this line:')
#send query to database
sql_query = ('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
    ORDER BY Artist.name ASC LIMIT 3''')

 #loop thru sql_query
for row in cur.execute(sql_query):
    print(row[0],row[1],row[2],row[3])

cur.close
