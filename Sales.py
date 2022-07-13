import streamlit as st 
import joblib 

#load the already uploaded joblib model 
model_nb = joblib.load('Store_Sales')

# 3 user input 
st.title("Store Sales Predict")
ip1 = st.number_input("Store_Area")
ip2 = st.number_input("Items_Available")
ip3 = st.number_input("Daily_Customer_Count")


op = model_nb.predict([[ip1,ip2,ip3]])
if st.button('PREDICT'):
  st.title(op[0])  #prints predicted store sales
