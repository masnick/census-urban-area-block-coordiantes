import os # for running shell commands
import sqlite3 as lite

# Use fresh DB
if os.path.exists("locations.db"):
  os.system('rm locations.db')

con = lite.connect('locations.db')

# Columns in HTML
#  1  MTFCC
#  2  OID
#  3  GEOID
#  4  STATE
#  5  COUNTY
#  6  TRACT
#  7  BLKGRP
#  8  BLOCK
#  9  BASENAME
# 10  NAME
# 11  LSADC
# 12  FUNCSTAT
# 13  POP100
# 14  HU100
# 15  AREALAND
# 16  AREAWATER
# 17  UR
# 18  CENTLAT
# 19  CENTLON
# 20  INTPTLAT
# 21  INTPTLON


with con:
  cur = con.cursor()
  cur.execute("create table pop(MTFCC STRING, OID INT, GEOID INT, STATE INT, COUNTY INT, TRACT INT, BLKGRP INT, BLOCK INT, BASENAME INT, NAME STRING, LSADC STRING, FUNCSTAT STRING, POP100 INT, HU100 INT, AREALAND INT, AREAWATER INT, UR STRING, CENTLAT FLOAT, CENTLON FLOAT, INTPTLAT FLOAT, INTPTLON FLOAT)")
  cur.execute("create index poplookup on pop (state, county);")


if con:
  con.close()
