import os # for running shell commands
import sqlite3 as lite


# Use fresh DB
if os.path.exists("locations.db"):
  os.system('rm locations.db')


if not os.path.exists("all.sql"):
  raise Exception('no sql file')

con = lite.connect('locations.db')

# http://stackoverflow.com/questions/15856976/transactions-with-python-sqlite3
con.isolation_level = None

with con:
  cur = con.cursor()
  cur.execute("create table pop(MTFCC STRING, OID INT, GEOID INT, STATE INT, COUNTY INT, TRACT INT, BLKGRP INT, BLOCK INT, BASENAME INT, NAME STRING, LSADC STRING, FUNCSTAT STRING, POP100 INT, HU100 INT, AREALAND INT, AREAWATER INT, UR STRING, CENTLAT FLOAT, CENTLON FLOAT, INTPTLAT FLOAT, INTPTLON FLOAT)")

  i =0
  for line in open('all.sql'):
    if i % 1000 == 0:
      cur.execute("begin")

    cur.execute(line)

    if i % 1000 == 999:
      cur.execute("commit")

    if i % 10000 == 0:
      print "Processing block %s..." % i

    i += 1

  cur.execute("commit")
  # Make index
  cur.execute("create index poplookup on pop (state, county, tract, block);")

if con:
  con.close()

