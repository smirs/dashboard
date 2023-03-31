import streamlit as st
import matplotlib.pyplot as plt

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([1, 2, 3, 4, 5]) 

st.pyplot(fig)

###########################################################

import streamlit as st
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
