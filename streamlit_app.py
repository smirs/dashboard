import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(font_scale=4)

x = [0,1,2,3,4]
y = [0,1,2,3,4]
ax = sns.lineplot(x,y)

###########################################################

st.pyplot(ax)

###
import streamlit as st
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
