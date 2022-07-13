import streamlit as st
import joblib

# load the previously dumped joblib model
model_nb = joblib.load(Store_Sales)

st.title(" STORE SALES PREDICT")
ip1 = st.text_input("Store_Area")   
#taking the 3 inputs
ip2 = st.text_input("Items_Available")
ip3 = st.text_input("Daily_Customer_Count")
   # predicting the store sales
op = model.predict([[op1,op2,op3]])  
if st.button('Predict'):
  st.title(op[0])
