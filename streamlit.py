# path = /OneDrive - Nanyang Technological University/NTU MSBA/AN8005 - Machine Learning Methodology/Project

import plotly.express as px
import seaborn as sns
import pandas as pd
import streamlit as st


#################### CODE ###################


@st.cache
def file_selector(dsname):
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

st.sidebar.header("Group Project AN8005: Machine Methodology")
st.sidebar.selectbox("Select an example dataset", ["Penguins", "Iris"])
st.sidebar.selectbox("Select a parameter", ["Penguins", "Iris"])

with header:
    st.title('Hooray')
    st.text('some description')
    st.text('some other description')


dataset.title("dataset")


with features:
    st.text("Here are some features")
