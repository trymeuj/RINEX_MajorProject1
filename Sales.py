import streamlit as st 
import joblib 
import MinMaxScaler
scaling = MinMaxScaler()

#load the already uploaded joblib model 
model_nb = joblib.load('Store_Sales')

# 3 user input 
st.title("Store Sales Predict")
ip1 = st.number_input("Store_Area")
ip2 = st.number_input("Items_Available")
ip3 = st.number_input("Daily_Customer_Count")
a = scaling.fit_transform([[ip1,ip2,ip3]]

op = model_nb.predict(a)
if st.button('PREDICT'):
  st.title(op[0])  #prints predicted store sales
