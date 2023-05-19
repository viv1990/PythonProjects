import streamlit as st
st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("images/photo.png",width=300)

with col2:
    st.title("Vivek Soni")
    content = """
    My Name is Vivek Soni. I am a seasoned professional into Information Security. 
    I also love coding and this page is all about what I have accomplished till now.
    Look forward for your feedback. Thanks and enjoy this page
    """
    st.info(content)
    # You can also write st.write(content) but info has some good formatting