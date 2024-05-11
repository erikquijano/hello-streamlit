# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code


# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


st.set_page_config(page_title="Automobile case study", page_icon="🚗")
st.markdown("# Automobile case study")
st.sidebar.header("Automobile case study")
st.write("# Automobile case study 👋")
st.markdown(
        """
        ABC Cardeals Pvt Ltd maintains caller’s data who are looking to buy new or used cars. Prospects can call or write an email and a support is given in terms of choosing the desired cars. 
    """
    )

# Function to load data
#@st.cache
def load_data():
    return pd.read_csv("auto.csv")

df = load_data()

# Summary statistics
st.write("## Summary of each variable")
#if st.button("Show Summary"):
st.write(df.describe())

# Most common contact method
st.write("## Most commonly used mode of contact")
#if st.button("Calculate Contact Methods"):
contact_method = df[['ContactByEmail', 'ContactByTelephone']].sum()
st.write(contact_method)

# Lead time preference
st.write("## Period most leads prefer to buy the car")
#if st.button("Calculate Lead Time Preference"):
lead_period = df[['Within24', 'Within48', 'Within72', 'WithinWeek', 'WithinWeeks', 'WithinMonth']].sum()
st.write(lead_period)

# Lead providers
st.write("## Best and worst lead provider")
##if st.button("Show Lead Providers"):
lead_provider = df.groupby(['LeadProvider_Id'])['Car Value'].sum()
st.write(lead_provider)

# New car preference
st.write("## Preference for new cars")
#if st.button("Show New Car Preference"):
st.write(df['Status'].value_counts())

# Most demanded models by state
st.write("## Most demanded car models by state")
#if st.button("Show Demanded Models"):
model_demand = df.groupby(['State', 'Model']).size().reset_index(name='Count')
most_demanded_models = model_demand.loc[model_demand.groupby('State')['Count'].idxmax()]
st.write(most_demanded_models)

# Best year for Toyota
st.write("## Best year for Toyota")
#if st.button("Show Best Year for Toyota"):
toyota_df = df[df['Manufacturer'] == 'Toyota']
yearly_sales = toyota_df.groupby('TradeInModelYear').size().reset_index(name='Count')
best_year = yearly_sales[yearly_sales['Count'] == yearly_sales['Count'].max()]
st.write(best_year)

# Adding combined manufacturer and model column
st.write("## Combine manufacturer and model")
df['make_model'] = df['Manufacturer'] + ' ' + df['Model']
#st.write(df.head())

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
#st.write("## Distance Grading")
#st.write(df.head())

# Most common distance
st.write("## Most common distance to dealer")
#if st.button("Show Common Distances"):
st.write(df.groupby('Distance scale').size().reset_index(name='Count'))

# Manufacturer average car value
st.write("## Average car value by manufacturer")
#if st.button("Show Average Values"):
st.write(df.groupby(['Manufacturer'])['Car Value'].mean())

# Box plot for Car Value by Manufacturer
st.write("## Box Plot of Car Values by Manufacturer")
#if st.button("Show Box Plot"):
plt.figure(figsize=(12, 6))
sns.boxplot(x='Manufacturer', y='Car Value', data=df)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# State with highest leads
st.write("## State with highest number of leads")
df['lead_sum'] = df[['Within24', 'Within48', 'Within72', 'WithinWeek', 'WithinWeeks', 'WithinMonth']].sum(axis=1)
state_sales = df.groupby(['State'])['lead_sum'].size().reset_index(name='Count')
best_state = state_sales[state_sales['Count'] == state_sales['Count'].max()]
st.write(best_state)

# City wise maximum car deal value
st.write("## City wise max value of car deal")
#if st.button("Show Max Car Values by City"):
st.write(df.groupby(['City'])['Car Value'].max().sort_values(ascending=False))

# Manufacturer market share
st.write("## Manufacturer Market Share")
total_market = df['Car Value'].sum()
df_make = df.groupby('Manufacturer')['Car Value'].sum().reset_index(name='Revenue')
df_make['Revenue Share %'] = (df_make['Revenue'] / total_market) * 100
df_make = df_make.sort_values(by='Revenue Share %', ascending=False)

# Layout for displaying table and pie chart side by side
col1, col2 = st.columns(2)

with col1:
    st.write("### Market Share Table")
    st.dataframe(df_make.style.format({'Revenue Share %': "{:.2f}%"}))

with col2:
    st.write("### Market Share Pie Chart")
    fig, ax = plt.subplots()
    ax.pie(df_make['Revenue Share %'], labels=df_make['Manufacturer'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Manufacturer Market Share')
    st.pyplot(fig)
