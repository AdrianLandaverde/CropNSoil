import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd

st.session_state.login= False
st.session_state.register= False

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

st.title("My Info")


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')


if authentication_status:
    st.subheader(f'Welcome *{name}*')
    authenticator.logout('Logout', 'main', key='unique_key')
    col1, col2, col3,= st.columns(3)

    with col1:
        st.markdown('### Soil Data')

        st.session_state.nitrogen = st.number_input('Nitrogen values', value= 85)

        st.session_state.phosphorous = st.number_input('Phosphorous values', value= 58)

        st.session_state.potassium = st.number_input('Potassium values', value= 41)

        st.session_state.ph = st.number_input('PH values', value= 7.038096)

    with col2:
        st.markdown('### Climate Data')

        st.session_state.temperature = st.number_input('Temperature values', value= 21.770462)

        st.session_state.humidity = st.number_input('Humidity values', value= 80.319644)

        st.session_state.rainfall = st.number_input('Rainfall values', value= 226.655537)

    with col3:
        st.markdown('### Personal Data')
        st.session_state.area= st.number_input('Area', value= 100)
        st.selectbox(label="Location", options= pd.read_csv('yields.csv')['Dist Name'].unique()) 
    
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')


