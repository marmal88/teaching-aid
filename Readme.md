# Teaching Aid for Machine Learning

This teaching aid is a python refactoring project based upon a previous project done for AN8005 Machine Learning Methodology. 

The aims of this mini project is to:
* Implement a front end UI for different ML methods utilized
* Experiment with class objects and functions in ML setting
* Implement project documentation practices


## Deployment
To utlize the project from main please run the following
```bash
conda create --name teaching-aid python=3.9
conda activate teaching-aid
```
Install packages by
```bash
pip install -r requirements.txt
```

To directly deploy the interface:
```bash
cd src
streamlit run main.py
```

## File structure
A simplified file structure is state below with essential details. 
```bash
.
├───data
├───src
│   ├───app_func
│   │   └───models.py
|   |   |___preprocess.py
│   └───main.py
├───test
└───test_preprocess.py
```

## Authors
The original code (Jupyter Notebook) was worked on by Peiyu, Hanwen, YangHang and Daniel Low
Refactoring work was done by Daniel Low 