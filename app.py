import streamlit as st
import ee

# Authenticate with Google Earth Engine
service_account = "sindhu@imperial-data-453906-t8.iam.gserviceaccount.com"
key_path = "gee_key.json"  # Path to your JSON key file

credentials = ee.ServiceAccountCredentials(service_account)
ee.Initialize(credentials)

st.title("Satellite Image Segmentation")
st.write("Google Earth Engine Initialized Successfully!")
