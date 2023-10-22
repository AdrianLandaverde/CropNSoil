import streamlit as st
from prediction import predict_crops

st.set_page_config(layout="wide")


# Inject the CSS
#st.markdown(page_bg_img, unsafe_allow_html=True)

shapes= {'Row': 'https://cdn.discordapp.com/attachments/1164958184964882462/1165411863694151711/image.png?ex=6546c160&is=65344c60&hm=b2fc61c33670a2dff8b3453b70cc6e1f0fe4235ee2cbbcc12ba37b8fc5406f00&',
        'Strip':'https://cdn.discordapp.com/attachments/1164958184964882462/1165412225054416926/image.png?ex=6546c1b6&is=65344cb6&hm=4d1a65b3df8c7a22822badcffd49cd9b56cdd949bea083e5901f7fb267012af0&',
        'Mixed':'https://cdn.discordapp.com/attachments/1164958184964882462/1165413768642175006/image.png?ex=6546c326&is=65344e26&hm=46eeb84f99adfad1102e040b4e880744d73d6d8d3b1dc2b6ae77218a5121d82f&'}

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpaperaccess.com/full/1155039.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
# Inject the CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

st.title("Dashboard")

nitrogen= st.session_state['nitrogen']
phosphorous= st.session_state['phosphorous']
potassium= st.session_state['potassium']
temperature= st.session_state['temperature']
humidity= st.session_state['humidity']
ph= st.session_state['ph']
rainfall= st.session_state['rainfall']
area= st.session_state['area']


with st.spinner('Computing the best crops for your soil...'):

    result= predict_crops(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall, area)

    print(result)

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(shapes[result['Type']], caption= result['Type'])

    with col2:

        col21, col22 = st.columns([1, 1])

        with col21:

            st.metric(value= result['Crop1'], label="First Crop")

            st.metric(value= result['Crop2'], label="Second Crop")

        with col22:

            st.metric(value= str(result['Crop1 Value']) + " Kg", label="Yield from "+ result['Crop1'])

            st.metric(value= str(result['Crop2 Value']) + " Kg", label="Yield from "+ result['Crop2'])

        st.metric(value=str(result['Revenue']) + " USD", label="Expected Revenue")

    st.title('Upcoming plan of action')

    st.write(result['Advice1'])

    st.write(result['Advice2'])

