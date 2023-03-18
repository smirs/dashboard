import pandas as pd
import numpy as np
import seaborn as sns
from noaa_sdk import NOAA
import datetime
import matplotlib.pyplot as plt

import streamlit as st 
plt.xkcd()

indict = {'St. Louis, MO':'63368', 
          'Charlotte, NC':'28277', 
          'Miami, FL':'33178', 
          'San Francisco, CA': '95111', 
          'Brownsville, TX':'78520',
          'New York City, NY': '10001'
          }

n = NOAA()
observations = {}

for i in indict:
    observations[i] = pd.DataFrame(list(n.get_observations(indict[i], 'US')))
    
def get_value(x):
    return x['value']

for i in indict:
    observations[i]['temperature_value'] = observations[i]['temperature'].apply(lambda x: get_value(x))
    observations[i]['temperature_value'] = observations[i]['temperature_value'] * 9/5 + 32

    observations[i]['timestamp'] = pd.to_datetime(observations[i]['timestamp'], infer_datetime_format=True)
    observations[i]['timestamp'] = pd.DatetimeIndex(observations[i]['timestamp']).tz_convert('US/Central')
    
d = str(observations['St. Louis, MO']['timestamp'][0])
today = d[0:10]

ax = plt.figure(figsize=(22, 16))
ax.suptitle('Team Tempreture in the USA @' + today, fontsize=48)
plt.xlabel(' ', fontsize=24)
plt.ylabel(' ', fontsize=52)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=24)

timewin = 10
for i in indict:
    sns.lineplot(x='timestamp', y='temperature_value', data=observations[i][observations[i]['timestamp'] >= (observations[i]['timestamp'][0] - pd.DateOffset(hours=timewin))], label= i)
    plt.annotate(i, xy=(observations[i]['timestamp'][0], observations[i]['temperature_value'][0]), fontsize=24)
    
xlabels = reversed(['Now','2 Hours Ago','4  Hours Ago','6  Hours Ago','8  Hours Ago','10 Hours Ago',
                    '12 Hours Ago','14 Hours Ago','16 Hours Ago','18 Hours Ago','20 Hours Ago'])
xlabels = [x for x in xlabels]

locs, labels=plt.xticks()
x_ticks = []
# new_xticks= ['test' for d in locs]
plt.xticks(locs, xlabels, rotation=90, horizontalalignment='right', fontsize=24)

st.pyplot(ax)
