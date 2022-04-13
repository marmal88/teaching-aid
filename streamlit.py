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
MLmethod = st.sidebar.selectbox("Select a Machine Learning Method", ["Support Vector Machines", "Decision Tree", "Neural Network", "K-Nearest Neighbours"])
st.sidebar.selectbox("Select a parameter", ["Penguins", "Iris"])

with header:
    st.title(f"Example: *{MLmethod}*")
    if str(MLmethod)[0] == "S":
        st.write(f"Support Vector Machine (SVM) is one of the most popular Machine Learning Classifier.\nIt falls under the category of Supervised learning algorithms and uses the concept of Margin to classify between classes.\nIt gives better accuracy than KNN, Decision Trees and Naive Bayes Classifier and hence is quite useful")
    elif str(MLmethod)[0] == "D":
        st.write(f"Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression.\nThe goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.")
    elif str(MLmethod)[0] == "N":
        st.write(f'Neural networks, also known as artificial neural networks (ANNs) or simulated neural networks (SNNs), are a subset of machine learning and are at the heart of deep learning algorithms.\nTheir name and structure are inspired by the human brain, mimicking the way that biological neurons signal to one another.')
    else:
        st.write(f"k-NN is a type of classification where the function is only approximated locally and all computation is deferred until function evaluation.\nThe neighbors are taken from a set of objects for which the class (for k-NN classification) or the object property value (for k-NN regression) is known.\nThis can be thought of as the training set for the algorithm, though no explicit training step is required.")

dataset.title("dataset")


with features:
    st.text("Here are some features")
