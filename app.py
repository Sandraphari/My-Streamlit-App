#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import matplotlib.patches as mpatches
import plotly_express as px
import plotly.figure_factory as ff

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    # st.header('Plot of Data')
    # fig, ax = plt.subplots(1,1)
    # plt.figure(figsize=(10,5))
    # plt.xticks(rotation=90)
    # sns.set_style('dark')
    # sns.set_palette('Set2')
    # ax.hist(x=df['College Sector'])
    # plt.title('College Sectors') 
    # st.pyplot(fig)


    # fig, ax = plt.subplots(1,1)
    # sns.set_style('dark')
    # sns.set_palette('Set2')
    # plt.figure(figsize=(10,5))
    # plt.xticks(rotation=90)
    # ax.hist(df['Course Sector'])  
    # plt.title('Course Sectors')
    # st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    plt.pie(df['College Sector'].value_counts().to_frame()['College Sector'],labels=df['College Sector'].value_counts().to_frame().index,autopct='%1.1f%%',shadow=True)
    plt.title('College Sectors')
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    plt.pie(df['Course Sector'].value_counts().to_frame()['Course Sector'],labels=df['Course Sector'].value_counts().to_frame().index,autopct='%1.1f%%',shadow=True)
    plt.title('Course Sectors')
    st.pyplot(fig)


    # colors = {'Aided':'red', 'Self Financing':'green', 'Private':'blue', 'Government':'yellow','Government Self Financing':'pink'}
    # colors = ['red', 'green', 'blue', 'yellow','pink']
    # fig, ax = plt.subplots(1,1)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(35, 20))
    fig.tight_layout() 
    frame1 = plt.gca()
    # frame1.axes.xaxis.set_ticklabels([])
    # plt.title('Number of vacant seats in different course sectors')
    # Alappuzha
    plt.subplot(2,2,1)
    plt.xticks(rotation=90)
    plt.bar(x="Course Sector", height="Vacant Seats", data=df[df['District']=='Alappuzha'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="Course Sector", height="Differently Abled", data=df[df['District']=='Alappuzha'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(),  color='lightblue')
    plt.title('Alappuzha')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    # Trivandrum
    plt.subplot(2,2,2)
    plt.xticks(rotation=90)
    plt.bar(x="Course Sector", height="Vacant Seats", data=df[df['District']=='Thiruvananthapuram'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="Course Sector", height="Differently Abled", data=df[df['District']=='Thiruvananthapuram'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(),  color='lightblue')
    plt.title('Trivandrum')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    # Kollam
    plt.subplot(2,2,3)
    plt.xticks(rotation=90)
    plt.bar(x="Course Sector", height="Vacant Seats", data=df[df['District']=='Kollam'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="Course Sector", height="Differently Abled", data=df[df['District']=='Kollam'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(),  color='lightblue')
    plt.title('Kollam')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    # Pathanamthitta
    plt.subplot(2,2,4)
    plt.xticks(rotation=90)
    plt.bar(x="Course Sector", height="Vacant Seats", data=df[df['District']=='Pathanamthitta'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="Course Sector", height="Differently Abled", data=df[df['District']=='Pathanamthitta'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(),   color='lightblue')
    plt.title('Pathanamthitta')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    fig.suptitle(' Number of vacant and diffrently abled seats in different course sectors ', fontsize=35)

    # plt.hist(df.groupby(['District','College Sector']).count().reset_index()['College Sector'])
    # plt.title('College sectors by district')
    # plt.xlabel('District')
    # plt.ylabel('No. of college sectors')
    # fig=sns.countplot(data=df, x="District", hue='College Sector')
    st.pyplot(fig)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(35, 20))
    fig.tight_layout() 
    frame1 = plt.gca()
    # frame1.axes.xaxis.set_ticklabels([])
    # plt.title('Number of vacant seats in different course sectors')
    # Alappuzha
    plt.subplot(2,2,1)
    plt.xticks(rotation=90)
    plt.bar(x="College Sector", height="Vacant Seats", data=df[df['District']=='Alappuzha'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="College Sector", height="Differently Abled", data=df[df['District']=='Alappuzha'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(),  color='lightblue')
    plt.title('Alappuzha')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    # Trivandrum
    plt.subplot(2,2,2)
    plt.xticks(rotation=90)
    # plt.bar(x="Course Sector", height="Vacant Seats", data=df[df['District']=='Thiruvananthapuram'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(), color='darkblue')
    # plt.bar(x="Course Sector", height="Differently Abled", data=df[df['District']=='Thiruvananthapuram'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(),  color='lightblue')
    plt.bar(x="College Sector", height="Vacant Seats", data=df[df['District']=='Thiruvananthapuram'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="College Sector", height="Differently Abled", data=df[df['District']=='Thiruvananthapuram'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(),  color='lightblue')
    plt.title('Trivandrum')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    # Kollam
    plt.subplot(2,2,3)
    plt.xticks(rotation=90)
    # plt.bar(x="Course Sector", height="Vacant Seats", data=df[df['District']=='Kollam'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(), color='darkblue')
    # plt.bar(x="Course Sector", height="Differently Abled", data=df[df['District']=='Kollam'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(),  color='lightblue')
    plt.bar(x="College Sector", height="Vacant Seats", data=df[df['District']=='Kollam'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="College Sector", height="Differently Abled", data=df[df['District']=='Kollam'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(),  color='lightblue')
    plt.title('Kollam')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    # Pathanamthitta
    plt.subplot(2,2,4)
    plt.xticks(rotation=90)
    # plt.bar(x="Course Sector", height="Vacant Seats", data=df[df['District']=='Pathanamthitta'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(), color='darkblue')
    # plt.bar(x="Course Sector", height="Differently Abled", data=df[df['District']=='Pathanamthitta'].drop(['Slno','College','Course','District','College Sector'],axis=1).groupby('Course Sector').sum().reset_index(),   color='lightblue')
    plt.bar(x="College Sector", height="Vacant Seats", data=df[df['District']=='Pathanamthitta'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(), color='darkblue')
    plt.bar(x="College Sector", height="Differently Abled", data=df[df['District']=='Pathanamthitta'].drop(['Slno','College','Course','District','Course Sector'],axis=1).groupby('College Sector').sum().reset_index(),  color='lightblue')
    plt.title('Pathanamthitta')
    top_bar = mpatches.Patch(color='darkblue', label='Vacant Seats')
    bottom_bar = mpatches.Patch(color='lightblue', label='Differently Abled')
    plt.legend(handles=[top_bar, bottom_bar])

    fig.suptitle(' Number of vacant and diffrently abled seats in different college sectors ', fontsize=35)

    # plt.hist(df.groupby(['District','College Sector']).count().reset_index()['College Sector'])
    # plt.title('College sectors by district')
    # plt.xlabel('District')
    # plt.ylabel('No. of college sectors')
    # fig=sns.countplot(data=df, x="District", hue='College Sector')
    st.pyplot(fig)

    
    # plt.title('Vacant seats in different college sectors in each district')
    fig=px.sunburst(df, path=['District', 'College Sector','Course Sector'], 
                    values='Vacant Seats',title='Vacancies in different course sectors in each college sector in each district')
    # fig.show()
    st.plotly_chart(fig)

    fig=px.sunburst(df, path=['District', 'College Sector','Course Sector'], 
                    values='Differently Abled',title='Seats for differently abled in different course sectors in each college sector in each district')
    # fig.show()
    st.plotly_chart(fig)

   


# Add a title and intro text
st.title('College Vacancies')
st.text("Let's explore data")

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Plots'])


# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Plots':
    displayplot()

