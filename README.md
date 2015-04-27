This is a script to scrape the [Census HTML pages for 2010 blocks](http://tigerweb.geo.census.gov/tigerwebmain/TIGERweb2010_tabblock_census2010.html) into a usable `sqlite3` database.

Not tested or verified. Use at your own risk.

# Running
This is meant to be executed on a beefy cloud server.

1. Run `python html_to_sql.py 0` to start the first worker. I recommend doing this inside `tmux`.
2. If you are using `tmux`, you can easily run this command multiple times (increment the last number each time) in separate `tmux` windows. E.g., `python html_to_sql.py 1`, `python html_to_sql.py 2`, etc. The script will create a file in `lock/` when it starts processing a county so that other instances of the script will not process the same county.
3. When finished, run `cat output/*.sql > all.sql` to combine the SQL files created by each instance of the script.
4. Run `batch_write_sqlite3.py` to run the SQL statements.

Output is a sqlite3 database with the following columns:

     1  MTFCC
     2  OID
     3  GEOID
     4  STATE
     5  COUNTY
     6  TRACT
     7  BLKGRP
     8  BLOCK
     9  BASENAME
    10  NAME
    11  LSADC
    12  FUNCSTAT
    13  POP100
    14  HU100
    15  AREALAND
    16  AREAWATER
    17  UR
    18  CENTLAT
    19  CENTLON
    20  INTPTLAT
    21  INTPTLON


# License
The MIT License (MIT)

Copyright (c) 2015 Max Masnick

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
