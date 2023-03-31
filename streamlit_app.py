import pandas as pd
import numpy as np
import seaborn as sns
sns.set(rc={"figure.figsize":(22, 12)}, font_scale=5) 

import matplotlib.pyplot as plt
import streamlit as st

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

Address = '1976 Greenglen Dr'
image_address = 'https://photos.zillowstatic.com/fp/466ce188280320fe0767ec885d9773a2-cc_ft_1536.png'
#############[changes with the property]###################
# One-Time Costs
Buying_Cost = st.slider('Listing Price', 100000, 300000, 100000, 1000)

# Initial Annual Costs [changes with the property]
HOA = st.slider('HOA Fee', 0, 500, 0, 10)
Maintenance_Annual_Cost = 12*HOA #12000

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


x = list(np.arange(0,16, 1))

gain = list(map(Total_Gain, x))
cost = list(map(Total_Cost, x))

df = pd.DataFrame({'time':x, 'gain':gain, 'cost':cost})

year_of_one_million = list(df.loc[((df['gain']-df['cost'])>1000000),'time'])[0]

ax = plt.figure(figsize=(44, 32))

# plt.axvline(Years_ToPayOff_Desired, 0 ,1)
# plt.axvline(year_of_one_million, 0 ,1)


# ax.text(14, cost[14]+200000,'Cost', fontsize=24, color='red')
# ax.text(14, gain[14]-300000,'Gain', fontsize=24, color='green')
# ax.text(Years_ToPayOff_Desired, 0.5*max(gain),'Expected Time For\nMortgate Payoff ~ ' + str(round(Years_ToPayOff_Desired, 1)) + ' Years', fontsize=24, color='darkblue')
# ax.text(year_of_one_million, 0.5*max(gain),'Expected Time For\nProfit in $1M ' + str(round(year_of_one_million, 1)), fontsize=24, color='darkred')


# ax.text(0, 1.1*max(gain), 'Property = '+ Address, fontsize=28, color='black')

# d = 120000
# ax.text(0, 0.95*max(gain) - 0*d, 'VARIABLES', fontsize=22, color='darkblue')

# ax.text(0, 0.95*max(gain) - 1*d, 'Purchase Price = $'+str(Buying_Cost), fontsize=18, color='black')
# ax.text(0, 0.95*max(gain) - 2*d, 'Annual Maintenance Costs = $'+str(Maintenance_Annual_Cost), fontsize=18, color='black')
# ax.text(0, 0.95*max(gain) - 3*d, 'Monthly Collected Rent = $' + str(Rental_Annual_Gain/12), fontsize=18, color='black')
# ax.text(0, 0.95*max(gain) - 4*d, 'Monthly Mortgage Payment = $' + str(Mortgage_Payment_Desired/12), fontsize=18, color='black')
# ax.text(0, 0.95*max(gain) - 5*d, 'Expected ROI @3 Yr = ' + str(round(ROI3*100,1)) + '%' , fontsize=18, color='darkred')
# ax.text(0, 0.95*max(gain) - 6*d, 'Expected ROI @5 Yr = ' + str(round(ROI5*100,1)) + '%' , fontsize=18, color='darkred')
# ax.text(0, 0.95*max(gain) - 7*d, 'Expected ROI @10 Yr = ' + str(round(ROI10*100,1)) + '%' , fontsize=18, color='darkred')

# ax.text(0, 0.95*max(gain) - 10*d, 'ASSUMPTIONS', fontsize=20, color='darkblue')
# ax.text(0, 0.95*max(gain) - 11*d, 'Down Payment Ratio = ' + str(round(DownPayment_Rate*100,1)) + '%' , fontsize=16, color='grey')
# ax.text(0, 0.95*max(gain) - 12*d, 'Closing Cost Ratio = ' + str(round(Closing_Cost_Rate*100,1)) + '%' , fontsize=16, color='grey')
# ax.text(0, 0.95*max(gain) - 13*d, 'Interest_Rate = ' + str(round(Interest_Rate*100,1)) + '%' , fontsize=16, color='grey')
# ax.text(0, 0.95*max(gain) - 14*d, 'Appreciation Rate = ' + str(round(Appreciation_Rate*100,1)) + '%' , fontsize=16, color='grey')
# # ax.text(0, 0.95*max(gain) - 15*d, 'Depreciation Rate = ' + str(round(Depressioation_Rate*100,1)) + '%' , fontsize=16, color='grey')



# ax.set(ylim=(0, 1.1*max(gain)), xlabel='Years', ylabel='$USD')

# arr_lena = mpimg.imread(image_address)
# imagebox = OffsetImage(arr_lena, zoom=0.25)
# ab = AnnotationBbox(imagebox, (11, 0.95*max(gain)))
# ax.add_artist(ab)

fig = sns.lineplot(x='time', y='gain', data=df, color = 'green', label = 'gain', linewidth=10)
fig = sns.lineplot(x='time', y='cost', data=df, color = 'red', label = 'cost', linewidth=10)
fig.set_title(Address, fontdict={'size': 120, 'weight': 'bold'})
fig.set_xlabel('Year', fontdict={'size': 100})
fig.set_ylabel('USD', fontdict={'size': 100})



st.pyplot(ax)
