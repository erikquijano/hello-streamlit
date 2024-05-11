import pandas as pd
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

# Function to load data
@st.cache
def load_data():
    return pd.read_csv("auto.csv")

df = load_data()

st.write("### Data Overview")
st.dataframe(df.head())

# User interaction for defining variable types
st.write("## Define variable types.")
if st.button("Show Data Types"):
    st.write(df.dtypes)

# Summary statistics
st.write("## Summary of each variable")
if st.button("Show Summary"):
    st.write(df.describe())

# Most common contact method
st.write("## Most commonly used mode of contact")
if st.button("Calculate Contact Methods"):
    contact_method = df[['ContactByEmail', 'ContactByTelephone']].sum()
    st.write(contact_method)

# Lead time preference
st.write("## Period most leads prefer to buy the car")
if st.button("Calculate Lead Time Preference"):
    lead_period = df[['Within24', 'Within48', 'Within72', 'WithinWeek', 'WithinWeeks', 'WithinMonth']].sum()
    st.write(lead_period)

# Lead providers
st.write("## Best and worst lead provider")
if st.button("Show Lead Providers"):
    lead_provider = df.groupby(['LeadProvider_Id'])['Car Value'].sum()
    st.write(lead_provider)

# New car preference
st.write("## Preference for new cars")
if st.button("Show New Car Preference"):
    st.write(df['Status'].value_counts())

# Most demanded models by state
st.write("## Most demanded car models by state")
if st.button("Show Demanded Models"):
    model_demand = df.groupby(['State', 'Model']).size().reset_index(name='Count')
    most_demanded_models = model_demand.loc[model_demand.groupby('State')['Count'].idxmax()]
    st.write(most_demanded_models)

# Best year for Toyota
st.write("## Best year for Toyota")
if st.button("Show Best Year for Toyota"):
    toyota_df = df[df['Manufacturer'] == 'Toyota']
    yearly_sales = toyota_df.groupby('TradeInModelYear').size().reset_index(name='Count')
    best_year = yearly_sales[yearly_sales['Count'] == yearly_sales['Count'].max()]
    st.write(best_year)

# Adding combined manufacturer and model column
st.write("## Combine manufacturer and model")
df['make_model'] = df['Manufacturer'] + ' ' + df['Model']
st.write(df.head())

# Distance grading
def grade_dist(dist):
    if dist < 10:
        return 'very near'
    elif dist < 50:
        return 'near'
    elif dist < 100:
        return 'far'
    else:
        return 'very far'

df['Distance scale'] = df['DistanceToDealer'].apply(grade_dist)
st.write("## Distance Grading")
st.write(df.head())

# Most common distance
st.write("## Most common distance to dealer")
if st.button("Show Common Distances"):
    st.write(df.groupby('Distance scale').size().reset_index(name='Count'))

# Manufacturer average car value
st.write("## Average car value by manufacturer")
if st.button("Show Average Values"):
    st.write(df.groupby(['Manufacturer'])['Car Value'].mean())

# State with highest leads
st.write("## State with highest number of leads")
df['lead_sum'] = df[['Within24', 'Within48', 'Within72', 'WithinWeek', 'WithinWeeks', 'WithinMonth']].sum(axis=1)
state_sales = df.groupby(['State'])['lead_sum'].size().reset_index(name='Count')
best_state = state_sales[state_sales['Count'] == state_sales['Count'].max()]
st.write(best_state)

# City wise maximum car deal value
st.write("## City wise max value of car deal")
if st.button("Show Max Car Values by City"):
    st.write(df.groupby(['City'])['Car Value'].max().sort_values(ascending=False))

# Manufacturer market share
st.write("## Manufacturer market share")
if st.button("Calculate Market Share"):
    total_market = df['Car Value'].sum()
    df_make = df.groupby('Manufacturer')['Car Value'].sum().reset_index(name='Revenue')
    df_make['Revenue Share %'] = (df_make['Revenue'] / total_market) * 100
    st.write(df_make)
