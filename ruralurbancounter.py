#-------------------------------------------------------------------------------
# Name:        RuralUrbanCounter
# Purpose:
#
# Author:      simon
#
# Created:     10/07/2017
# Copyright:   (c) simon 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import pandas as pd
from pandas import Series
import csv
import glob
import json

def file_to_str(fn, dt, sepp, headerl=None, lterminator='\n'):
    #dateparser = lambda dates: [pd.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]
    """
    Loads the content of a text file into a DataFrame, where datetimes in columns dt are converted to timestamps
    @return a string
    """
    content = pd.read_csv(fn, index_col=False, lineterminator='\n', header = headerl, parse_dates=dt, dayfirst=True, sep=sepp)
    content = content.drop_duplicates()
    #print content[0:10]
    #with open(fn, 'r') as f:
    #    content=f.read()
    return content



def main():
    personstats = {}
    i = 0
    out = "C:/Temp/Joinedtracks/Joinedtracks/Cities/stats.json"
    with open(out, 'w') as fp:
        for f in glob.glob("C:/Temp/Joinedtracks/Joinedtracks/Cities/*.csv"):
            l = file_to_str(f, [2], ';', headerl = 0)
            numberoftracks = l.track.value_counts().size
            #print numberoftracks
            durationtable = l.groupby(['track'])['datetime'].agg(['min','max'])
            durationtable['difference']= durationtable['max']-durationtable['min']
            #print durationtable
            #print durationtable.difference.value_counts()
            #This extracts and counts the purposes of a track
            purposestats = (l.groupby('track')['purto'].agg('max')).value_counts()
            #print(purposestats)
            person = str(l['person'].iloc[0])
            personstats[person]={'numberoftracks': numberoftracks, 'purposestats': purposestats, 'durationtable': durationtable}
            #Getting lengths
            for row in l.itertuples():
                print row.X
                print row.Y
            i+= 1
            if i == 1:
                print personstats
                #json.dump(personstats,fp)
                break



  # for row in durationtable.itertuples():
  #  print(row.max -row.min)


   #for row in l.itertuples():
   # track_id = row[2]
   # print(track_id)
   # break




if __name__ == '__main__':
    main()
