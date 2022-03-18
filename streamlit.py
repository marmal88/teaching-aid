# path = /OneDrive - Nanyang Technological University/NTU MSBA/AN8005 - Machine Learning Methodology/Project

import plotly.express as px
import seaborn as sns
import pandas as pd
import streamlit as st


#################### CODE ###################


@st.cache
def get_data(filename):
    df1 = sns.load_dataset('penguins')
    df1.dropna(how='any', inplace=True)
    df2 = sns.load_dataset('iris')


#################### STREAMLIT FRONTEND ###################
header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

st.markdown(


    """
    <style>
    .main{background-color: #F5F5F5}
    </style>
    """,
    unsafe_allow_html=True
)

with header:
    st.title('Hooray')
    st.text('some description')
    st.text('some other description')


dataset.title("dataset")
st.sidebar.selectbox("Select a number", [1, 2, 3, 4])

with features:
    st.text("Here are some features")
