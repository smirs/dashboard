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
