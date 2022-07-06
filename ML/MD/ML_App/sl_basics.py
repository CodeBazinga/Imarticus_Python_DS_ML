import streamlit as st
from datetime import datetime, date, time

st.title('Streamlit App Demo')

st.header('Header')
st.subheader('Sub Header')

st.text('Welcome to the Streamlit App')

# Create a link
st.markdown("""
[Redirect to google]
(https://www.google.com)
""",True)


## Streamlit widgets
# Widgets in streamlit

# Text Input
st.subheader('Text Input')
name = st.text_input('Enter your name')
st.write('Your name is',name)

st.subheader('Number Input')
num = st.number_input('Enter a number')
st.write('Your number is',num)

st.subheader('Date Input')
d = st.date_input('Enter a date',date(2020,5,7))
st.write('Date is',d)

st.subheader('Time Input')
d = st.time_input('Enter time',time(9,58))
st.write('Time is',d)


# Buttons
st.subheader('Buttons')
if st.button('Click here'):
    st.write('Button has been clicked')
else:
    st.write('Button not clicked')


# Radio Button - Single Selection
st.subheader('Radio Button')
genre = st.radio("Favorite novel genre",('Thriller','Comedy','Drama','Mystery'))
if genre == "Thriller":
    st.write('Thriller selected')
elif genre=="Comedy":
     st.write('Comedy selected')
elif genre=="Drama":
    st.write('Drama selected')
else:
    st.write('Msytery selected')


# Checkbox - Multiple Seletcion
st.subheader('Checkbox')
if st.checkbox('1'):
    st.write('1')
if st.checkbox('2'):
    st.write('2')
if st.checkbox('3'):
    st.write('3')


# Select Box - Drop Down
st.subheader('Select Box- Single Selection')
option = st.selectbox('Enter your credentials',('Adhar','PAN','Passport'))
st.write('You have selected',option)

# Multi Select Box - 
st.subheader('Multi Select Box - Multiple Selection')
option2 = st.multiselect('Enter your credentials',('Adhar','PAN','Passport','VoterID'))
st.write('You have selected',option2)

# Simple Slider
st.subheader('Simple Slider')
age = st.slider('Enter your age',1,100,25)
st.write('Your age is',age)

# Range Slider
st.subheader('Range Slider')
range = st.slider('Select your range',0,100,(45,65))
st.write('Your range selected is',range)

# Date Slider
st.subheader('Date Slider')
dt_range = st.slider('Select date',value=datetime(2020,3,7),
        format='YYYY-MM-DD')
st.write('Your date is',dt_range)

# Time Slider
st.subheader('Time Slider')
tm_range = st.slider('Select time',value=time(14,35,23))
st.write('Your date is',tm_range)
st.write('Todays date is',datetime.today())










