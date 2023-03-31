

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

price = st.slider('Listing Price?', 100000, 200000, 100)
st.write("I'm ", price, 'years old', txt)

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([10000, 100000, 150000, 200000, price]) 

st.pyplot(fig)
