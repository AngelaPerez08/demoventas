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

# prompt: usando el dataframe df, crear un filtro con la columna Region, y dentro de ese filtro crear otro filtro con la columna State

# Assuming 'Region' and 'State' are column names in your DataFrame.
# Replace with your actual column names if different.
if 'Region' in df.columns and 'State' in df.columns:
    region_filter = st.selectbox("Select Region", df['Region'].unique())
    filtered_df_region = df[df['Region'] == region_filter]

    state_filter = st.selectbox("Select State", filtered_df_region['State'].unique())
    filtered_df_state = filtered_df_region[filtered_df_region['State'] == state_filter]

    st.write(filtered_df_state)
else:
    st.error("Error: 'Region' or 'State' column not found in the DataFrame.")

# prompt: Con la columa Category y los filtros ya creados previamente, imprime una grafica de pastel donde se muestren los resultados de los filtros

# Assuming 'Category' is a column in your DataFrame.
# Replace 'Category' with the actual column name if different.
if 'Category' in df.columns:
    category_filter = st.selectbox("Select Category", df['Category'].unique())
    filtered_df_category = df[df['Category'] == category_filter]

    # Create the pie chart
    if not filtered_df_category.empty:
      fig = px.pie(filtered_df_category, names='Category', title='Category Distribution')
      st.plotly_chart(fig)
    else:
      st.write("No data available for the selected filters.")
else:
    st.error("Error: 'Category' column not found in the DataFrame.")
# prompt: crea una grafica de las ventas acumuladas por año, pero que esten divididas por categoria y subcategoria

import pandas as pd
import plotly.express as px
import streamlit as st

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx")
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# Check for necessary columns
required_cols = ['Año', 'Categoría', 'Subcategoría', 'Ventas']
if not all(col in df.columns for col in required_cols):
    st.error(f"Error: The DataFrame is missing one or more of these required columns: {', '.join(required_cols)}")
    st.stop()

# Convert 'Año' to datetime if it's not already
if not pd.api.types.is_datetime64_any_dtype(df['Año']):
    try:
        df['Año'] = pd.to_datetime(df['Año']).dt.year  # Extract year
    except:
        st.error(f"Could not convert 'Año' column to datetime. Check its format.")
        st.stop()

# Calculate cumulative sales
df['Ventas Acumuladas'] = df.groupby(['Año', 'Categoría', 'Subcategoría'])['Ventas'].cumsum()


# Plotting
fig = px.line(df, 
              x='Año', 
              y='Ventas Acumuladas', 
              color='Categoría', 
              line_dash='Subcategoría',
              title='Ventas Acumuladas por Año, Categoría y Subcategoría',
              labels={'Ventas Acumuladas': 'Ventas Acumuladas', 'Año': 'Año'},  # More descriptive labels
              )
st.plotly_chart(fig)
