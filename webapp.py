import streamlit as st
import requests
import pickle
import numpy as np

def update_text_boxes(data):
    st.write(f"Temperature: {data.get('field1', 'N/A')}")
    st.write(f"Heartrate: {data.get('field2', 'N/A')}")

st.title("HEALTH MONITORING SYSTEM")

# Button to trigger data update
if st.button("Fetch Data"):
    api_url = "https://api.thingspeak.com/channels/2095787/feeds.json?api_key=ZWF9Z0QVSFGLV02H&results=1"
    
    # Fetch data from the server
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        feeds = data.get("feeds", [])
        
        if feeds:
            latest_data = feeds[0]  # Assuming the latest data is the first item in the list
            update_text_boxes(latest_data)
            st.success("Data updated successfully.")
        else:
            st.warning("No data found.")
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")

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
