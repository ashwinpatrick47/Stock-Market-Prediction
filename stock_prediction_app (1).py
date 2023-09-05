import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import numpy as np
from prophet import Prophet
import pandas as pd
import os
import requests
import csv


from alpha_vantage.timeseries import TimeSeries

api_key= "LS36RK149XMJNJAX"                      


# CSS styling
st.markdown(
    """
    <style>
    body {
        background-color: beige;
    }
    .centered-title {
        color: white;
        text-align: center;
    }
    .subtitle {
        font-style: italic;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title with CSS class
st.markdown('<h1 class="centered-title">STOCK PREDICTION MODEL</h1>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">Welcome to our stock prediction model! Kindly enter the name of your stock  to get relevant stock related information and the prediction of stock prices for the next few months.</p>', unsafe_allow_html=True)

# User input
stock= st.text_input("Enter the name of the stock")

st.write("The stock entered is",stock)

mapping = {
    'apple': 'AAPL',
    'microsoft': 'MSFT',
    'amazon': 'AMZN',
    'google': 'GOOGL',
    'tesla': 'TSLA',
    'jpmorgan': 'JPM',
    'nvidia': 'NVDA',
    'homedepot': 'HD',
    'visa': 'V',
    'johnsonjohnson': 'JNJ',
    'proctergamble': 'PG',
    'exxonmobil': 'XOM',
    'amd': 'AMD',
    'oracle': 'ORCL',
    'mastercard': 'MA',
    'agilent': 'A',
    'nasdaq': 'NDAQ',
    'berkshirehathaway': 'BRK.A',
    'taiwansemiconductor': 'TSM',
    'alcoa': 'AA',
    'albertsons': 'ACI',
    'novonordisk': 'NVO',
    'acertherapeutics': 'ACER',
    'align': 'ALGN',
    'automaticdataprocessing': 'ADP',
    'abbottlaboratories': 'ABT',
    'asml': 'ASML',
    'atacregistration': 'AACG',
    'americanactors': 'AACT',
    'adobe': 'ADBE',
    'americanelectricpower': 'AEP',
    'appliedmaterials': 'AMAT',
    'americaninternationalgroup': 'AIG',
    'american tower': 'AMT',
    'amphenol': 'APH',
    'aac': 'AAC',
    'panamericansilver': 'PCGU',
    'analogdevices': 'ADI',
    'ansys': 'ANSS',
    'autodesk': 'ADSK',
    'accenture': 'ACN',
    'abbvie': 'ABBV',
    'arcbest': 'ARBK',
    # Add more stocks and ticker symbols here
}

# Convert the stock name to ticker symbol
stock_ticker = mapping.get(stock.lower())

if stock_ticker:
   st.write("The stock ticker symbol is:", stock_ticker)
else:
    st.write("Invalid stock entered. Please try again.")
    
    
#collecting time series data from alpha vantage
ts = TimeSeries(key=api_key, output_format='pandas')

stock, meta_data = ts.get_daily(symbol=stock_ticker, outputsize='full') 


# Specify the directory path for saving the CSV file
directory_path = "C:/User/DELL/Desktop/STREAMLIT/"

# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

# Set the file path for saving the CSV file
csv_file_path = os.path.join(directory_path, "dataset.csv")



# Save the stock DataFrame to the CSV file
stock.to_csv(csv_file_path, index_label='Date')  # Labeling index column as "Date"

# Read the CSV file into a new DataFrame
df = pd.read_csv(csv_file_path)

#to get reference value
# Take the first 10 rows and consider only the '4. close' column
selected_data = df.head(10)['4. close']

# Calculate the sum of the '4. close' column for the first 10 rows
sum_of_closes = selected_data.sum()

# Calculate the mean of the '4. close' column for the first 10 rows
reference = selected_data.mean()

#st.write("Sum of '4. close' for the first 10 rows:", sum_of_closes)
#st.write("Mean of '4. close' for the first 10 rows:", reference)

df1=df

df['Date'] = pd.to_datetime(df['Date'], dayfirst=False)  

df['ds'] = pd.DatetimeIndex(df['Date'])

columns_to_keep = ['Date', '4. close']

df = df[columns_to_keep]


# Rename the columns
df.columns = ['ds', 'y']

# Print the modified DataFrame
#st.write(df)#delete this

#to handle missing data
df = df.set_index('ds')#By setting the index, you are specifying which column should be used as the index for the DataFrame
df = df.asfreq('D')  # Set the desired frequency (e.g., daily)

# Forward-fill missing values
df['y'] = df['y'].fillna(method='ffill')

# Backward-fill missing values
#df['y'] = df['y'].fillna(method='bfill')

# Interpolate missing values
#df['y'] = df['y'].interpolate()

# Reset index
df = df.reset_index()#revert the DataFrame to its original state with the default index.

# Check the updated dataset
#st.write(df)#delete this 

#train the model
#When daily_seasonality=True, it indicates that the Prophet model should consider daily patterns and variations when making forecasts.
df_prophet = Prophet(changepoint_prior_scale= 0.003, seasonality_prior_scale=0.01, seasonality_mode='multiplicative', daily_seasonality=True,changepoint_range=0.404,interval_width=0.15)
df_prophet.add_country_holidays(country_name='US')
df_prophet.fit(df)


# API URL to fetch company overview data

url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_ticker}&apikey={api_key}'

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response content
    data = response.json()
    
     # Store specific data into separate variables
    eps = data.get('EPS')
    return_on_equity_ttm = data.get('ReturnOnEquityTTM')
    pe_ratio = data.get('PERatio')
    price_to_book_ratio = data.get('PriceToBookRatio')
    

    # Select specific columns from the data
    selected_columns_col1 = [
        'MarketCapitalization',
        'PERatio',
        'PEGRatio',
        'PriceToSalesRatioTTM',
        'PriceToBookRatio',
        'DividendPerShare',
        'DividendYield',
        'EBITDA', # Use 'EVToRevenue' instead of 'EBITDA'
    ]

    selected_columns_col2 = [
        'ProfitMargin',
        'ReturnOnEquityTTM',
        'ReturnOnAssetsTTM',
        'EVToRevenue',
        'EVToEBITDA',
        'Beta',
        'RevenuePerShareTTM',
        'EPS',
    ]

    # Create the content for the table in column 1
    table_data_col1 = []
    for column in selected_columns_col1:
        value = data.get(column)
        if value is not None:
            table_data_col1.append((column, value))

    # Create the content for the table in column 2
    table_data_col2 = []
    for column in selected_columns_col2:
        value = data.get(column)
        if value is not None:
            table_data_col2.append((column, value))

    
    company_overview_data = {
        'eps': eps,
        'return_on_equity_ttm': return_on_equity_ttm,
        'pe_ratio': pe_ratio,
        'price_to_book_ratio': price_to_book_ratio,
        
    }
else:
    st.write("Invalid stock ticker or an error occurred. Please try again.")
    
    
#balance sheet


# API URL to fetch balance sheet data
balance_sheet_url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={stock_ticker}&apikey={api_key}'

# Make a GET request to the API endpoint for balance sheet data
response_balance_sheet = requests.get(balance_sheet_url)

working_capital_ratio_calculated = None

# Check if the request was successful
if response_balance_sheet.status_code == 200:
    # Parse the JSON data from the response content
    data_balance_sheet = response_balance_sheet.json()

    # Function to extract specific fields from the balance sheet data
    def extract_fields(report, field_names):
        extracted_data = []
        for field in field_names:
            value = report.get(field)
            if value is not None:
                extracted_data.append((field, value))
        return extracted_data

    # Select specific columns from the balance sheet data
    selected_balance_sheet_fields = [
        'fiscalDateEnding',
        'totalShareholderEquity',
        'totalCurrentAssets',
        'totalCurrentLiabilities',
        'longTermDebt',
        
    ]

    # Extract data for the latest available report (2023) from the balance sheet
    table_data_balance_sheet = []
    if 'quarterlyReports' in data_balance_sheet and data_balance_sheet['quarterlyReports']:
        latest_balance_sheet_report = data_balance_sheet['quarterlyReports'][0]
        table_data_balance_sheet = extract_fields(latest_balance_sheet_report, selected_balance_sheet_fields)

        # Calculate working capital ratio
        total_current_assets = float(table_data_balance_sheet[2][1])
        total_current_liabilities = float(table_data_balance_sheet[3][1])
        working_capital_ratio = total_current_assets / total_current_liabilities if total_current_liabilities != 0 else None

        # Calculate debt-to-equity ratio
        long_term_debt = float(table_data_balance_sheet[4][1])
        shareholder_equity = float(table_data_balance_sheet[1][1])
        debt_to_equity_ratio = long_term_debt / shareholder_equity if shareholder_equity != 0 else None

        # Store calculated ratios into separate variables
        debt_equity_ratio_calculated = debt_to_equity_ratio
        working_capital_ratio_calculated = working_capital_ratio
    
    


else:
    st.write("Invalid stock ticker or an error occurred while fetching balance sheet data. Please try again.")
    
eps = float(data.get('EPS')) if data.get('EPS') else None
return_on_equity_ttm = float(data.get('ReturnOnEquityTTM')) if data.get('ReturnOnEquityTTM') else None
pe_ratio = float(data.get('PERatio')) if data.get('PERatio') else None
price_to_book_ratio = float(data.get('PriceToBookRatio')) if data.get('PriceToBookRatio') else None



#st.write('eps percentage will be',eps*reference/100)

eps_percent= eps*reference/100


#st.write(debt_equity_ratio_calculated,working_capital_ratio_calculated,eps,return_on_equity_ttm*100,pe_ratio,price_to_book_ratio,eps_percent)

# Check if the values are not None before performing the comparisons
if (
    eps_percent is not None and eps_percent>= 5 and
    return_on_equity_ttm is not None and return_on_equity_ttm*100 >= 10 and
    pe_ratio is not None and pe_ratio <= 45 and
    price_to_book_ratio is not None and price_to_book_ratio < 15 and
    debt_equity_ratio_calculated is not None and debt_equity_ratio_calculated < 2 and
    working_capital_ratio_calculated is not None and 1.2 <= working_capital_ratio_calculated <= 2 
    #sharpe_ratio>1
):
        st.write('<p style="font-size: 22px; font-weight: bold; font-style: italic; text-decoration: underline; color: lightblue;">This stock is investible.</p>', unsafe_allow_html=True)
else:
        st.write('<p style="font-size: 22px; font-weight: bold; font-style: italic; text-decoration: underline; color: lightblue;">This stock is not investible.</p>', unsafe_allow_html=True)


st.write('<p style="font-size: 24px; font-weight: bold; font-style: italic; text-decoration: underline; ">RATIONALE:</p>', unsafe_allow_html=True)
# Display both tables inside a single rectangle with CSS styling(OVERVIEW)
# Ensure table_data_col1 and table_data_col2 have data
if table_data_col1:
    table_data_html_col1 = "".join(f"<tr><td style='padding: 8px; border-bottom: 1px solid #e0e0e0;'>{row[0]}</td><td style='padding: 8px; border-bottom: 1px solid #e0e0e0; color: lightblue;'>{row[1]}</td></tr>" for row in table_data_col1)
else:
    table_data_html_col1 = "<tr><td colspan='2'>No data available.</td></tr>"

if table_data_col2:
    table_data_html_col2 = "".join(f"<tr><td style='padding: 8px; border-bottom: 1px solid #e0e0e0;'>{row[0]}</td><td style='padding: 8px; border-bottom: 1px solid #e0e0e0; color: lightblue;'>{row[1]}</td></tr>" for row in table_data_col2)
else:
    table_data_html_col2 = "<tr><td colspan='2'>No data available.</td></tr>"

# Combine the table HTML code into the markdown
table_html = (
    '<div style="border: 3px double lightblue; padding: 10px; border-radius: 5px;">'
    '<h4 style="color: lightblue; margin-bottom: 10px; text-align: center;">Company Overview Data</h4>'
    '<div style="display: flex; justify-content: space-between;">'
    '<div style="width: 48%; padding-right: 2%;">'
    '<table style="width: 100%; border-collapse: collapse;">'
    '<tr style="background-color: #f5f5f5; color: lightblue;">'
    '<th style="padding: 8px; text-align: left; border-bottom: 1px solid #e0e0e0;">Financial Ratio</th>'
    '<th style="padding: 8px; text-align: left; border-bottom: 1px solid #e0e0e0;">Value</th>'
    '</tr>'
    + table_data_html_col1
    + '</table>'
    '</div>'
    '<div style="width: 48%; padding-left: 2%;">'
    '<table style="width: 100%; border-collapse: collapse;">'
    '<tr style="background-color: #f5f5f5; color: lightblue;">'
    '<th style="padding: 8px; text-align: left; border-bottom: 1px solid #e0e0e0;">Financial Ratio</th>'
    '<th style="padding: 8px; text-align: left; border-bottom: 1px solid #e0e0e0;">Value</th>'
    '</tr>'
    + table_data_html_col2
    + '</table>'
    '</div>'
    '</div>'
    '</div>'
)

# Display the combined HTML
st.markdown(table_html, unsafe_allow_html=True)


 # Display both tables and additional data inside a single rectangle with CSS styling(BALANCE SHEET)
st.markdown(
            '<div style="border: 3px double lightblue; padding: 10px; border-radius: 5px;">'
            # ... (Previous code for displaying company overview data remains unchanged) ...
            '<h4 style="color: lightblue; margin-top: 20px; text-align: center;">Balance sheet data</h4>'
            '<table style="width: 100%; border-collapse: collapse;">'
            '<tr style="background-color: #f5f5f5; color: lightblue;">'
            '<th style="padding: 8px; text-align: left; border-bottom: 1px solid #e0e0e0;">Field</th>'
            '<th style="padding: 8px; text-align: left; border-bottom: 1px solid #e0e0e0;">Value</th>'
            '</tr>'
            + "".join(f"<tr><td style='padding: 8px; border-bottom: 1px solid #e0e0e0;'>{row[0]}</td><td style='padding: 8px; border-bottom: 1px solid #e0e0e0; color: lightblue;'>{row[1]}</td></tr>" for row in table_data_balance_sheet)
            + f'</table><p style="color: lightblue; margin-top: 10px; text-align: center;">Working Capital Ratio: {working_capital_ratio_calculated:.2f}</p>'
            + f'<p style="color: lightblue; margin-top: 5px; text-align: center;">Debt-to-Equity Ratio: {debt_equity_ratio_calculated:.2f}</p>'
            #+ f'<p style="color: lightblue; margin-top: 5px; text-align: center;">Sharpe Ratio: {sharpe_ratio:.2f}</p>'
            '</div>',
            unsafe_allow_html=True
)

   


#FOR INCOME STATEMENT

# Function to fetch data from the Alpha Vantage API
def fetch_income_statement_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={stock_ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data



# Fetch data from the Alpha Vantage API
data = fetch_income_statement_data(stock_ticker, api_key)

# Check if the API response contains 'quarterlyReports' and 'annualReports'
quarterly_data = data.get('quarterlyReports', [])
annual_data = data.get('annualReports', [])

# Convert the fetched data to DataFrames
if quarterly_data:
    quarterly_df = pd.DataFrame(quarterly_data)
    quarterly_df = quarterly_df[['fiscalDateEnding', 'grossProfit', 'totalRevenue', 'costofGoodsAndServicesSold','netIncome', 'ebit']]
    quarterly_df['fiscalDateEnding'] = pd.to_datetime(quarterly_df['fiscalDateEnding'])

    # Filter and display the quarterly reports for 2023 and 2022
    quarterly_reports_2023_2022 = quarterly_df[quarterly_df['fiscalDateEnding'].dt.year.isin([2023, 2022])]
    if not quarterly_reports_2023_2022.empty:
        st.markdown(
            f"""
            <div style="border: 3px double lightblue; padding: 10px; max-height: 400px; overflow-y: auto;">
                <h4 style="background-color: lightblue; padding: 5px; border-radius: 5px; color: white;">
                    Quarterly Income Reports for 2023 and 2022
                </h4>
                {quarterly_reports_2023_2022.to_html(index=False)}
            </div>
            """,
            unsafe_allow_html=True
        )

if annual_data:
    annual_df = pd.DataFrame(annual_data)
    annual_df = annual_df[['fiscalDateEnding', 'grossProfit', 'totalRevenue', 'costofGoodsAndServicesSold', 'netIncome', 'ebit']]
    annual_df['fiscalDateEnding'] = pd.to_datetime(annual_df['fiscalDateEnding'])

    # Filter and display the annual reports for 2021, 2020, and 2019
    annual_reports_2021_2020_2019 = annual_df[annual_df['fiscalDateEnding'].dt.year.isin([2021, 2020, 2019])]
    if not annual_reports_2021_2020_2019.empty:
        st.markdown(
            f"""
            <div style="border: 3px double lightblue; padding: 10px; max-height: 400px; overflow-y: auto;">
                <h4 style="background-color: lightblue; padding: 5px; border-radius: 5px; color: white;">
                    Yearly Income Reports for 2021, 2020, and 2019
                </h4>
                {annual_reports_2021_2020_2019.to_html(index=False)}
            </div>
            """,
            unsafe_allow_html=True
        )
        

#cashflow


# Function to fetch data from the Alpha Vantage API for the 'CASH_FLOW' function
def fetch_cash_flow_data(stock_ticker, api_key):
    url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={stock_ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data

# Fetch data from the Alpha Vantage API for the 'CASH_FLOW' function
data = fetch_cash_flow_data(stock_ticker, api_key)

# Check if the API response contains 'quarterlyReports'
quarterly_data = data.get('quarterlyReports', [])

# Extract data from the most recent fiscal quarter
if quarterly_data:
    latest_quarter_data = quarterly_data[0]  # Data from the most recent fiscal quarter

    # Convert the data to a DataFrame
    cash_flow_df = pd.DataFrame([latest_quarter_data])
    cash_flow_df = cash_flow_df[['fiscalDateEnding', 'operatingCashflow','changeInCashAndCashEquivalents' ,'netIncome']]
    cash_flow_df['fiscalDateEnding'] = pd.to_datetime(cash_flow_df['fiscalDateEnding'])

    # Display the DataFrame
    if not cash_flow_df.empty:
        st.markdown(
            f"""
            <div style="border: 3px double lightblue; padding: 10px; max-height: 400px; overflow-y: auto;">
                <h4 style="background-color: lightblue; padding: 5px; border-radius: 5px; color: white;">
                    Latest Quarterly Cash Flow Report
                </h4>
                {cash_flow_df.to_html(index=False)}
            </div>
            """,
            unsafe_allow_html=True
        )

# CODE   for historical data display 


#st.write('<p style="font-size: 20px; font-weight: bold; font-style: italic; text-decoration: underline; color: white;">The Historical data pertaining to your stock:</p>', unsafe_allow_html=True)

#display historical data
#st.write(df1)#


st.write("**_Fetching stock price prediction for the next three months....._**")


#for predicting for the next 3 months starting from today
# Define the date range for the next 3 months
today = pd.Timestamp(datetime.now().date())
future = pd.date_range(start=today, periods=3*30, freq='D')

# Make future dataframe
future_df = pd.DataFrame({'ds': future})

forecast = df_prophet.predict(future_df)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

# Display the forecasted data for the next 3 months
#st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])



# Plot the forecasted data using Prophet's built-in plot function(

st.write('<p style="font-size: 20px; font-weight: bold; font-style: italic; text-decoration: underline;">The Prediction Graph for your stock looks as follows:...</p>', unsafe_allow_html=True)



# Create a figure for yhat (predicted values)
fig_yhat = go.Figure()
fig_yhat.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Predicted'))

# Update the figure layout for yhat
fig_yhat.update_layout(title='Stock Price Prediction  for the Next 3 Months',
                       xaxis_title='Date',
                       yaxis_title='Stock Price')



# Display the figures
st.plotly_chart(fig_yhat)