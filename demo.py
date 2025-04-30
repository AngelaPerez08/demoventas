# prompt: muestra el dataframe con streamlit

import pandas as pd
import streamlit as st

# prompt: arma una grafica de las ventas por region del dataframe df con streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx")

    # Assuming 'Region' and 'Sales' are column names in your DataFrame.
    # Replace with your actual column names if different.
    if 'Region' not in df.columns or 'Sales' not in df.columns:
        st.error("Error: 'Region' or 'Sales' column not found in the DataFrame.")
    else:
        fig = px.bar(df, x='Region', y='Sales', title='Sales por Region')
        st.plotly_chart(fig)

except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# prompt: usando el dataframe df, crea un filtro con streamlit de la columna Region, y otro filtro con los resultados  del filtro Region usando la columna State. Tambien crea una grafica de pastel con los resultados

import pandas as pd
import streamlit as st
import plotly.express as px

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx")
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
    st.stop()  # Stop execution if the file is not found
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# Region filter
if 'Region' in df.columns:
    region_filter = st.selectbox("Select Region", df['Region'].unique())
    filtered_df_region = df[df['Region'] == region_filter]
else:
    st.error("Error: 'Region' column not found in the DataFrame.")
    st.stop()

# State filter based on the selected region
if 'State' in filtered_df_region.columns:
    state_filter = st.selectbox("Select State", filtered_df_region['State'].unique())
    filtered_df_state = filtered_df_region[filtered_df_region['State'] == state_filter]
else:
    st.error("Error: 'State' column not found in the DataFrame.")
    st.stop()

# Display the filtered data
st.write(filtered_df_state)

# Create a pie chart based on the final filtered data
if not filtered_df_state.empty:  # Check if the DataFrame is not empty
    if 'Sales' in filtered_df_state.columns: # Check if 'Sales' column exists
      fig = px.pie(filtered_df_state, names='State', values='Sales', title='Sales Distribution by State')
      st.plotly_chart(fig)
    else:
        st.error("Error: 'Sales' column not found in the DataFrame. Cannot create pie chart.")
else:
    st.warning("The filtered DataFrame is empty. Cannot create a pie chart.")
