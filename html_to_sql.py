import pandas as pd
import sys # for sys.exit()
import os # for running shell commands
import code # for console breakpoint per http://stackoverflow.com/questions/8347636/drop-in-single-breakpoint-in-ruby-code
# code.interact(local=locals())

import re # regexp

# Pretty printing for debugging
import pprint
pp = pprint.PrettyPrinter(indent=4)
# Usage: `pp.pprint(varname)`

import requests
from bs4 import BeautifulSoup

# Need to get mapping of state codes onto 2 letter abbreviations :(
abbrevs = {1: 'al', 2: 'ak', 4: 'az', 5: 'ar', 6: 'ca', 8: 'co', 9: 'ct', 10: 'de', 11: 'dc', 12: 'fl', 13: 'ga', 15: 'hi', 16: 'id', 17: 'il', 18: 'in', 19: 'ia', 20: 'ks', 21: 'ky', 22: 'la', 23: 'me', 24: 'md', 25: 'ma', 26: 'mi', 27: 'mn', 28: 'ms', 29: 'mo', 30: 'mt', 31: 'ne', 32: 'nv', 33: 'nh', 34: 'nj', 35: 'nm', 36: 'ny', 37: 'nc', 38: 'nd', 39: 'oh', 40: 'ok', 41: 'or', 42: 'pa', 44: 'ri', 45: 'sc', 46: 'sd', 47: 'tn', 48: 'tx', 49: 'ut', 50: 'vt', 51: 'va', 53: 'wa', 54: 'wv', 55: 'wi', 56: 'wy'}

# Get list of states and counties
import states_and_counties as stct
states_and_counties = stct.states_and_counties


with open("output/sql_%s.sql" % sys.argv[1], "a") as myfile:
  for i, state_county in enumerate(states_and_counties):
    # Skip the state and county if someone else already has it
    if os.path.exists("lock/%s_%s" % tuple(state_county)):
      print "Skipping %s %s" % tuple(state_county)
      continue
    else:
      os.system("touch lock/%s_%s" % tuple(state_county))


    try:
      url = 'http://tigerweb.geo.census.gov/tigerwebmain/Files/tab10/tigerweb_tab10_tabblock_2010_%s_%03d.html' % (abbrevs[state_county[0]], state_county[1])
      print "Requesting %s..." % url
      r = requests.get(url)
      print "Souping..."
      soup = BeautifulSoup(r.text, "lxml")

      trs = soup.body.table.find_all('tr')
      print "Looping %s rows..." % len(trs)
      for tr in trs:
        # Skip the header row
        if len(tr.find_all('td')) == 0:
          continue

        # Extract values from row
        values = tuple([t.text for t in tr.find_all('td')])
        if len(values) != 21:
          raise Exception('%s values for state %s, county %s' %(len(values), state_county[0], state_county[1]))

        # Write sql to file
        sql = 'insert into pop values("%s", %s, %s, %s, %s, %s, %s, %s, %s, "%s", "%s", "%s", %s, %s, %s, %s, "%s", %s, %s, %s, %s);\n' % values

        myfile.write(sql)
    except:
      os.system("rm lock/%s_%s" % tuple(state_county))
      print "Exception for %s_%s; lock removed" % tuple(state_county)
