import streamlit as st


st.set_page_config(layout="wide")


st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

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

st.header("About us")

col1, col2= st.columns([3,2])

with col1:

    col11, col12= st.columns(2)

    with col11:

        st.image('https://cdn.discordapp.com/attachments/1164958184964882462/1165466311552409651/image.png?ex=6546f415&is=65347f15&hm=f0011503b9d4aedbcbd59af5cf006a42b618cbe765ecf64ed83d4725e12b9071&', width=200,
                caption= 'Adrian Landaverde Nava')

        st.image('https://media.discordapp.net/attachments/1164958184964882462/1165477042083594271/IMG_7778.jpg?ex=6546fe14&is=65348914&hm=516636f84405bd46e702b2de08f3f57a24990cd9b2dfcd2a8566457866c7c2d8&=&width=612&height=662', width=200,
                caption='Alim Vasaya')

    with col12:

        st.image('https://media.discordapp.net/attachments/1164958184964882462/1165452315734593547/1694393997669.jpeg?ex=6546e70d&is=6534720d&hm=bda898cc59b65082a2c9239bf09ea0713dd44f3e2a2b428b9e88148c607276b9&=&width=662&height=662', width= 200,
                caption= 'Kanika Gupta')

        st.image('https://cdn.discordapp.com/attachments/1164958184964882462/1165451988683722781/CF52570A-A6EF-4D4F-AB90-6ADC60981557_4_5005_c.jpeg?ex=6546e6bf&is=653471bf&hm=d42ad9da754f58877079baed1862135ce32d6b3eb4f2ff0cd32262c77058cf2d&', width=200,
                caption= 'Surya Patil')

with col2:

    st.image('https://cdn.discordapp.com/attachments/1164958184964882462/1165174616705224704/logo-png.png?ex=6545e46c&is=65336f6c&hm=470bc3f2920067c724732e75affcb2cbe216652b6a273dbf7ab3d9711da48eb5&')