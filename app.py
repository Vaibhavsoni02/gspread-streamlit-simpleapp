import gspread
import pandas as pd
import streamlit as st

# Retrieve secrets
GCP_SERVICE_ACCOUNT = st.secrets["gcp_service_account"]
GOOGLE_SHEET_ID = st.secrets["google_sheet_id"]

# Authenticate and authorize GCP service account
gc = gspread.service_account_from_dict(GCP_SERVICE_ACCOUNT)

# Connect to Google Sheet
sh = gc.open_by_key(GOOGLE_SHEET_ID)

# Get all data from Google Sheet
worksheet = sh.sheet1
data = worksheet.get_all_values()

# Convert data to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Filter data using query
filtered_data = df.query("Order_Date > '2022-01-01'")

# Display filtered data in Streamlit
st.write(filtered_data)
