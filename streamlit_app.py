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


###########################################################
import streamlit as st
import matplotlib.pyplot as plt
###########################################################

import streamlit as st
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old', txt)

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([1, 2, 3, 4, age]) 

st.pyplot(fig)
