import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='pythonlogin',
                                         user='root',
                                         password='database2020')
mySql_insert_query = """INSERT INTO `movie_detailed` (`name`, `director`, `duration`, `year`, `actors`, `genres`, `imdbscore`, `imdblink`) VALUES ('%s', '%s', '%s', '%s', '%s', "%s", '%s', '%s')"""

cursor = connection.cursor()

header = True
with open('moviedata.txt', encoding= "utf8") as csv:
    for line in csv:
        try:
            args = line.replace('\n', '').split('\t')
            if header:
                print(args)
                header = False
                continue
            id = args[0]
            name = args[1]
            director = args[2]
            duration = args[3]
            year = args[4]
            actors = args[5] + ", " + args[6] + ", " + args[7]
            genres = args[8].split('|')
            imdbscore = args[9]
            imdblink = args[10]
            print(id, name, director, duration, year, actors, genres, imdbscore,imdblink)
            cursor.execute('INSERT INTO `movie_detailed` (name, director, duration, year, actors, genres, imdbscore, imdblink) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', [name, director, duration, year, actors, genres, imdbscore, imdblink])
        except:
            print("Wrong Value")
connection.commit()
print(cursor.rowcount, "Record inserted successfully into table")
cursor.close()
