import streamlit as st 
from  joblib import load 
import numbers as np

## load the model from disk 
model = load('iris_model.joblib')
st.title('Iris Flower Prediction App')

### Create streamlit UI 
#species_name = ['Setosa', 'Versicolor', 'Virginica']
sepal_length = st.slider("sepal Lenght", 4.3, 7.9, 5.4)
sepal_width = st.slider("sepal width", 2.0, 4.4, 3.4)
petal_length = st.slider("petal Lenght", 1.0, 6.9, 1.4)
petal_width = st.slider("petal width", 0.3, 2.5, 0.2)

features = [[sepal_length, sepal_width, petal_length, petal_width]]

if st.button('Predict'): 
    prediction = model.predict(features)

    st.write(f"Prediction Species:  {prediction[0]}")