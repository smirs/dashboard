import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(font_scale=4)

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

Address = '1976 Greenglen Dr'
image_address = 'https://photos.zillowstatic.com/fp/466ce188280320fe0767ec885d9773a2-cc_ft_1536.png'
#############[changes with the property]###################
# One-Time Costs
Buying_Cost = 169900 #450000

# Initial Annual Costs [changes with the property]
Maintenance_Annual_Cost = 12*295 #12000

# Initial Annual Gains 
Rental_Annual_Gain = 12 * (1650) #3500

#############[do not change with property]#################
# Rates 
Interest_Rate = 0.05 #0,06
DownPayment_Rate = 1.0 #0.20
Appreciation_Rate = 0.04 # source: https://www.ownerly.com/real-estate/average-home-appreciation/
Depressioation_Rate = 0.03
Closing_Cost_Rate = 0.02

DownPayment_Cost = DownPayment_Rate * Buying_Cost
Loan_Amount = Buying_Cost - DownPayment_Cost
Loan_Cost = Interest_Rate * Loan_Amount
Closing_Cost = Closing_Cost_Rate * Buying_Cost

# Desires
Mortgage_Payment_Desired = 12 * 6000 #6000
Years_ToPayOff_Desired = round((Loan_Cost + Loan_Amount)/Mortgage_Payment_Desired,2)

###########################################################
def Property_Value_Expected(x): 
    return Buying_Cost * (1 + Appreciation_Rate)**x

def Property_Ownership_Rate(x): 
    return (x * Mortgage_Payment_Desired + DownPayment_Cost)/Buying_Cost

# Expected_Payoff_Years = ( (Expected_Loan_Cost + Closing_Cost + Buying_Cost) - (Expected_Property_Value) ) / (Rental_Annual_Gain - Maintenance_Annual_Cost)

def Total_Cost(x):
    return x * Maintenance_Annual_Cost + min(x * Mortgage_Payment_Desired, Buying_Cost - DownPayment_Cost) + Loan_Cost + Closing_Cost + DownPayment_Cost

def Total_Gain(x):
    return x * Rental_Annual_Gain + Property_Ownership_Rate(x) * Property_Value_Expected(x)

# Return On Investment at the Desired Year
ROI = round(Total_Gain(Years_ToPayOff_Desired) / Total_Cost(Years_ToPayOff_Desired) , 3)
ROI3 = round(Total_Gain(3) / Total_Cost(3) , 3)
ROI5 = round(Total_Gain(5) / Total_Cost(5) , 3)
ROI10 = round(Total_Gain(10) / Total_Cost(10) , 3)


fig, ax = plt.subplots(figsize=(22, 12))

for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(20)

for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(20)
    
sns.set(rc={"figure.figsize":(22, 12)})
x = list(np.arange(0,16, 1))

gain = list(map(Total_Gain, x))
cost = list(map(Total_Cost, x))
# fig, ax = plt.subplots()

df = pd.DataFrame({'time':x, 'gain':gain, 'cost':cost})

ax = sns.lineplot(x='time', y='gain', data=df, color = 'green', label = 'gain')
ax = sns.lineplot(x='time', y='cost', data=df, color = 'red', label = 'cost')

###########################################################
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
###########################################################

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')

price = st.slider('Listing Price?', 100000, 200000,)
st.write("I'm ", price, 'years old', txt)

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([10000, 100000, 150000, 200000, price]) 

st.pyplot(ax)
