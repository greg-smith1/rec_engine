import sqlite3
import csv

with sqlite3.connect("beer.db") as conn:
    curs = conn.cursor()

    curs.execute("""
DROP TABLE IF EXISTS lookup;""")

    curs.execute("""
DROP TABLE IF EXISTS user_recs;""")

    curs.execute("""
DROP TABLE IF EXISTS content_recs;""")

    curs.execute("""
CREATE TABLE IF NOT EXISTS lookup(
pk integer PRIMARY KEY,
beerId integer,
brewerId integer,
name varchar,
style varchar,
num_ratings integer,
avg_ratings real,
stdv_ratings real
);""")

    curs.execute("""
CREATE TABLE IF NOT EXISTS user_recs(
pk integer PRIMARY KEY,
beerId integer,
rec1 integer,
rec2 integer,
rec3 integer,
rec4 integer,
rec5 integer,
rec6 integer,
rec7 integer,
rec8 integer
);
""")

    curs.execute("""
CREATE TABLE IF NOT EXISTS content_recs(
pk integer PRIMARY KEY,
beerId integer,
rec1 integer,
rec2 integer,
rec3 integer,
rec4 integer,
rec5 integer,
rec6 integer,
rec7 integer,
rec8 integer
);
""")

    curs.execute("""
DROP VIEW IF EXISTS master_list;""")

    curs.execute("""
CREATE VIEW IF NOT EXISTS master_list AS
SELECT l.beerId, l.brewerId, l.name, l.style,
l.num_ratings, l.avg_ratings, l.stdv_ratings
FROM lookup AS l
INNER JOIN user_recs AS u
ON l.beerId = u.beerId
INNER JOIN content_recs AS c
ON l.beerId = c.beerId""")

    with open("lookup.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        _ = next(reader)
        print(_)
        for row in reader:
            beer_id = row[1]
            brewer_id = row[2]
            name = row[3]
            style = row[4]
            num_ratings = row[5]
            avg_ratings = row[6]
            stdv_ratings = row[7]
            curs.execute("""
INSERT INTO
 lookup(beerId, brewerId, name, style, num_ratings, avg_ratings, stdv_ratings)
 VALUES(?, ?, ?, ?, ?, ?, ?);
""", (beer_id, brewer_id, name, style, num_ratings, avg_ratings, stdv_ratings))

    with open("user_recs.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        _ = next(reader)
        print(_)
        for row in reader:
            beer_id = row[0]
            # print(row[1:10])
            rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8 = row[1:10]
            curs.execute("""
INSERT INTO
 user_recs(beerId, rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8)
 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                         (beer_id, rec1, rec2, rec3, rec4,
                          rec5, rec6, rec7, rec8))

    with open("content_recs.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        _ = next(reader)
        print(_)
        for row in reader:
            beer_id = row[0]
            # print(row[1:10])
            rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8 = row[1:10]
            curs.execute("""
INSERT INTO
 content_recs(beerId, rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8)
 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                         (beer_id, rec1, rec2, rec3, rec4,
                          rec5, rec6, rec7, rec8))
