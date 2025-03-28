import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Remove spaces from column names

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    
    # Debugging
    st.write("Filtered Columns:", filtered_df.columns.tolist())

    if filtered_df.empty:
        st.error("⚠️ No data available after filtering! Try different filters.")
    else:
        st.subheader("Plot Data")
        
        # Check numeric columns for plotting
        num_columns = filtered_df.select_dtypes(include=['number']).columns.tolist()
        
        x_column = st.selectbox("Select x-axis column", filtered_df.columns.tolist())
        y_column = st.selectbox("Select y-axis column", num_columns)

        if x_column not in filtered_df.columns or y_column not in filtered_df.columns:
            st.error("⚠️ Selected columns are not available in filtered data. Please choose again.")
        else:
            filtered_df[y_column] = pd.to_numeric(filtered_df[y_column], errors='coerce')
            filtered_df = filtered_df.dropna(subset=[y_column])

            if st.button("Generate Plot"):
                st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")

