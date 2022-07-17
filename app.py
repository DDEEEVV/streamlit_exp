# @TODO: Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd
from matplotlib import Path

# @TODO: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
st.write("# Creating a Website with python streamlit library")

# @TODO: Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
st.write("Hi, Welcome to the platform. Please add your date of birth!")

# @TODO: Create a Pandas dataframe
covid_df = pd.read_csv(Path("//Users/ddevii/Rutgers/Project_2/Resources/WHO-COVID-19-global-data.csv"))

# @TODO: Write the Pandas dataframe to the page
st.write(covid_df)

# @TODO: Create a text input box using the Streamlit `text_input` function.
# @TODO: Save the input as a variable.
input_value = st.text_input("What would be interesting to collect from this data, and what that will be useful for?")

# @TODO: Utilize the Streamlit `button` function to display the text input
# variable created in the prior step to the page.
if st.button("Display Message"):
    st.write(input_value)

# Bonus
# wtf
