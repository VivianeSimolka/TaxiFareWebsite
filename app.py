import streamlit as st
from datetime import datetime
import pytz
import emoji
import requests
import pandas as pd

'''
# Woop woop! TaxiFareModel front!
'''

st.markdown('''
\U0001F600
''')


day = st.date_input("Day of ride")
time = st.time_input("Time of ride")
date_time = datetime.combine(day,time)

pickup_datetime = str(day) + " " + str(time)

pickup_long = st.text_input("pickup longitude", key=float)
pickup_lat = st.text_input("pickup latitude", key=float)
drop_long = st.text_input("dropoff longitude", key=float)
drop_lat = st.text_input("dropoff latitude", key=float)
passenger_count = st.number_input("passenger count", key=int, min_value=1, value=1, max_value=10, step=1)


url = 'https://taxifare.lewagon.ai/predict'


params = {"key": ["bidule"],
                "pickup_datetime": [date_time],
                "pickup_longitude": [float(pickup_long)],
                "pickup_latitude": [float(pickup_lat)],
                "dropoff_longitude": [float(drop_long)],
                 "dropoff_latitude": [float(drop_lat)],
                "passenger_count": [int(passenger_count)]
}

response = requests.get(url,params =params).json()
fare = round(response['fare'],2)
st.metric('Expected:',fare,delta = None, delta_color ="normal")
