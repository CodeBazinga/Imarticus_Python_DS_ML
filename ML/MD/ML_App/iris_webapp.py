import streamlit as st
import pickle


log_reg = pickle.load(open('log_model.pkl','rb'))
rf = pickle.load(open('rf_model.pkl','rb'))
svc = pickle.load(open('svc_model.pkl','rb'))
dt = pickle.load(open('dt_model.pkl','rb'))

def classify(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return 0

st.title("Iris Classification Web App")
html_temp = """
    <div style="background-color:darkblue ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
activities = ['Log_Reg','DT','RF','SVM']
option = st.sidebar.selectbox('Which model would you like to use?',activities)
st.subheader(option)
sl = st.slider('Select Sepal Length', 0.0, 10.0)
sw = st.slider('Select Sepal Width', 0.0, 10.0)
pl = st.slider('Select Petal Length', 0.0, 10.0)
pw = st.slider('Select Petal Width', 0.0, 10.0)
inputs=[[sl,sw,pl,pw]]

if st.button('Classify'):
    if option=='DT':
        st.success(dt.predict(inputs))
    elif option=='SVM':
        st.success(svc.predict(inputs))
    elif option=='RF':
       st.success(rf.predict(inputs))
    else:
        st.success(log_reg.predict(inputs))
