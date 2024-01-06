import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))
st.title('Fraud Detection ')

AM=st.text_input('Enter the Amount: ')
HD=st.text_input('Enter the HoursofDay: ')
DW=st.text_input('Enter the DayOfWeak: ')
MC=st.text_input('Enter the MerchantCategory : ')
IN=st.text_input('Enter it is international fraud or not : ')



if st.button('Predict'):
    Type=float(AM)
    AT=float(HD)
    PT=float(DW)
    RPM=int(MC)
    Torque=int(IN)
   
    data=[[AM,HD,DW,MC,IN]]
    result=model.predict(data)
    st.success(result)

    if result[0]==0:
        st.write("Fraud is not detected")


    else :
        st.write("fraud is detected")

