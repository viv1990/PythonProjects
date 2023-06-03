import streamlit as st
import pandas as pd
from Send_Email import Send_Email

st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to",("Home","Our Team", "Contact Us"))

# The above two line also has an alternate, we can create 'pages' folder in the same root folder as our main.py
# And add the other pages as .py files in the 'pages' folder. It will automatically show in the navigation
# keep in mind to add import streamlit as st in all those pages

col1,col2=st.columns(2)

# col1 and col2 are objects of columns method in streamlit

if(page=="Home"):

    with col1:
        st.image("images/photo.jpg",width=400)

    with col2:
        st.header("Vivek Soni")
        st.subheader("CISA,CRISC,CCSP,CDPSE,CIPM")
        content = """
        My Name is Vivek Soni. I am a seasoned professional into Information Security. 
        I also love coding and this page is all about what I have accomplished till now.
        Look forward for your feedback. Thanks and enjoy this page
        """
        st.info(content)
        # You can also write st.write(content) but info has some good formatting

    st.write("Below you can find some of the apps I have worked upon, feel free to get in touch")

    data = pd.read_csv("venv/data.csv",delimiter=';')
    col4,empty_col,col5 = st.columns([1.5,0.5,1.5])
    for index,row in data.iterrows():

        title = row['title']
        desc = row['description']
        url = row['url']
        image = row['image']
        image_path = "images/"+image

        if(index%2==0):
            with col4:
                st.info(title)
                st.write(desc[:70]+"..")
                st.write(url)
                st.image(image_path,width=300)

        else:
            with col5:
                st.info(title)
                st.write(desc[:70]+"..")
                st.write(url)
                st.image(image_path,width=300)

elif (page=="Our Team"):
    st.header("The Best Company")
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
     ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
     fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
     mollit anim id est laborum"""
    st.write(content)
    st.subheader("Our Team")
    col8,empty_col1,col9,empty_col2,col10 = st.columns([1.5,0.5,1.5,0.5,1.5])
    df=pd.read_csv("venv/OurTeam.csv")


    for index, row in df[:4].iterrows():
        firstname = row["first name"]
        lastname=row["last name"]
        role = row["role"]
        image=row["image"]
        team_image_path = "images_Our Team/"+image
        with col8:
            st.info(firstname.title()+" "+lastname.title())
            st.write(role)
            st.image(team_image_path,use_column_width=True)


    for index, row in df[4:8].iterrows():
        firstname = row["first name"]
        lastname = row["last name"]
        role = row["role"]
        image = row["image"]
        team_image_path = "images_Our Team/" + image
        with col9:
            st.info(firstname.title()+" "+lastname.title())
            st.write(role)
            st.image(team_image_path,use_column_width=True)

    for index, row in df[8:12].iterrows():
        firstname = row["first name"]
        lastname = row["last name"]
        role = row["role"]
        image = row["image"]
        team_image_path = "images_Our Team/" + image
        with col10:
            st.info(firstname.title() + " " + lastname.title())
            st.write(role)
            st.image(team_image_path,use_column_width=True)

elif (page=="Contact Us"):
    with st.form(key="form1",clear_on_submit=True):
        st.header("Contact Us")
        user_email=st.text_input("Enter your email address")
        # This is for single line text
        topics = pd.read_csv("venv/topics.csv")

        options = []

        for index, row in topics.iterrows():
            topic = row["topic"]
            options.append(topic)



        Topic = st.selectbox("Select from these",options)

        raw_message=st.text_area("Your Message")
        message= f"""
        Subject: New email from {user_email}
        From:{user_email}
        It is in regards to: {Topic}
        The message says: {raw_message}
           """
        # This is for multi-line text
        button=st.form_submit_button("Send")
        # Button is a boolean value , if you press the button, the object will contain True otherwise False
        if(button):
            Send_Email(message)
            st.info("Email successfully sent")

        # This can be seen in the terminal
