import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('trainedmmodel.sav', 'rb'))

#create function

def health(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    input_data_f=input_data_reshaped
    predictions = loaded_model.predict(input_data_f)
    if predictions==['Normal']:
        return "Your Heartrate and body temperature is Abnormal"
    else:
        return "Your Heartrate and body temperature is Normal"
  

def main():

    #title of webpage
    st.title("Health Monitoring System")

    #getting input data
    HR=st.text_input("Heart Rate")
    TEMP=st.text_input("Body Temperature")

    #code for prediction
    diagnosis= ""

    #button for pred
    if st.button("Submit"):
        diagnosis = health([HR,TEMP])

    #color = "red" if "Abnormal" in diagnosis else "green"
    #styled_diagnosis = f'<div style="color:{color};">{diagnosis}</div>'

    #st.markdown(styled_diagnosis, unsafe_allow_html=True)

    if "Abnormal" in diagnosis:
        st.error(diagnosis)
    else:
        st.success(diagnosis)

    #st.success(diagnosis)


if __name__ == "__main__":
    main()
