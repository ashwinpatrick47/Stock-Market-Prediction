# Stock-Market-Prediction
Introduction

In today’s world of finance, people are increasingly interested in investing in stocks. With Its potential to generate long term returns, help in portfolio diversification , provision of dividend income etc, investing in stocks helps provide an additional source of income for individuals, thus making it increasingly popular today. 

However, investment in stocks comes with it’s fair share of risks. This makes a stock prediction product a valuable tool in today’s world. By providing users with valuable insights associated with stocks such as the various financial ratios associated with the stock, the trends and future behavior of the stock using stock forecasting and  prediction graphs, this project allows individuals to make informed decisions in the ever changing stock market.

This project demonstrates the application of API integration for data collection, utilizes time series forecasting and analysis techniques to develop a stock prediction model, and employs performance metrics to assess the model's accuracy and efficiency.

During the development of this project, I gained substantial knowledge about the stock market, the decision-making process and strategies involved in stock investments, machine learning concepts and techniques applicable to stock prediction, the significance of financial ratios in context to stocks and investments, diverse forecasting models, their functionality, and importance. This project provided me with extensive insights into model building, performance testing, and the practical utilization of these components in constructing an effective prediction tool.


How Do Individuals Pick A Stock?
Picking the right stock at the right time is crucial in stock investment. It involves making well-informed choices to optimize returns while minimizing risks and losses. To do this, individuals consider various parameters like Company Fundamentals, Industry trends, Risk tolerance, Competitive advantage, Stock Price, Free Cash flow, and economic factors like GDP and interest rates.
 Additionally, financial ratios such as Earnings per Share (EPS), P/E ratio, P/B ratio, Dividend yield, Return on Equity, Return on Assets, and Debt-to-Equity ratio play a significant role in the decision-making process. By carefully assessing these factors, investors can enhance their chances of success in the stock market and make informed decisions on which stock to invest in.
Value Investors VS Traders
Through my research I have learnt that there are in general, two types of investors, value investors and Traders
Value investors, also known as long-term investors, invest in stocks that they believe are undervalued and primarily focus on the company's overall potential, paying little attention to short-term market fluctuations. On the other hand, short-term investors or traders concentrate on the immediate price movements and market trends of a stock, aiming to make quick profits.
Warren Buffet
Warren Buffet, known as the world's greatest stock investor, follows Benjamin Graham's value investing principles, focusing on undervalued stocks. His investment strategy focuses on selecting companies with strong fundamentals and a significant competitive advantage, ensuring long-term growth irrespective of short-term market fluctuations, thus gaining profits by using the power of compounding to his advantage.
To assess a company's potential, Buffet  analyzes a company's performance based on past 5-10 years' return on equity, uses debt-to-equity ratio to assess its debt, and also looks at the company’s profit margin to ensure consistent profitability.
 Buffet's investment rules include never losing money, understanding that if the business does well, the stock will eventually follow, and preferring to buy wonderful companies at fair prices rather than fair companies at wonderful prices which thus ensures a margin of safety against market risks. He also believes in holding onto investments for the long term, often for at least 10 years.

Financial Advisor
During my research on stocks, I encountered another concept that caught my attention—the significance of a financial advisor's role.
A financial advisor is a professional that assists individuals , families and businesses by providing guidance and making informed decisions on their behalf that will help them manage their financial affairs like investment decisions, retirement planning etc.
By thoroughly assessing an individual's financial status and understanding their specific financial objectives, the financial advisor creates a personalized financial plan tailored to help achieve those goals. Their wide range of services includes investment advising, budgetary guidance, estate planning, tax planning, and much more.
A financial advisor becomes particularly important when one lacks investment expertise, experiences consistent financial losses, or requires assistance in devising an estate plan. With their expertise they can help you navigate through these complexities, delivering appropriate solutions that align with your financial needs.

Quant Analyst
While researching on my journey, I was eager to find out about the role of a quant analyst. From my understanding, A quantitative analyst, also known as a quant, is a financial professional who applies mathematical and statistical foundations to analyze and model financial data and other parameters.A Quant ties strong relationships with many agencies including the bank that they use their software principles in order to help their financial situations of their company.
Quants are more experienced programmers whose skills comprise strong mathematical skills, programming concepts and stock making foundations using statistical techniques making them rather reliable and honest in their work.
Many financial based companies nowadays recruit strong quants in order to make better decision making strategies in order to tackle world financial problems and make use of these strategies to give them the optimal approaches and solution.
Application Programming Interface(API)
An API is a set of rules and protocols that allows different applications to communicate and interact with each other. Using an API, an application can access specific functions and data from another application or platform in a standardized and efficient way.
Among the various functions and services provided by API , one of the most important ones is Data Access where in the API provides controlled access to data allowing applications to retrieve and manipulate data from databases and other third party platforms. 
In this project, the Alpha Vantage API is used to gather real-time US stock data. The Alpha Vantage API offers a diverse range of functions and features, thus providing access to a wide range of valuable stock data. This includes daily stock prices, access to company’s balance sheets, income statement, cash flow status and earnings that are released by the company on both yearly and quarterly basis, earnings calendar, and comprehensive company overview through which we can retrieve the various financial ratios associated with the stock.
For our project, we utilized historical stock price data as the training set for our prediction model. Additionally, we made the other financial data that was collected transparent to the user, as these ratios play a pivotal role in assisting individuals in determining whether the stock is a worthwhile investment or not.
Apart from the Alpha Vantage API, the other APIs that I came across are Yahoo Finance, nsetools and Rapid API.
Handling Missing Data
The first step in  building this project was using alpha vantage and collecting all the data related to the stocks. Historical data pertaining to the stock price is then used to train a forecasting model which will then  make future stock price predictions. 
However, to ensure that the predictions are as accurate as possible and that our model is trained well, it is necessary to ensure that the data acquired is clean and free from errors or missing values. If there are any gaps or inconsistencies in the data, it needs to be handled before using it to train the model.
There are two ways to handle missing data: delete the missing values and impute the missing values. In this project, an imputation method, specifically the forward fill method, is used for handling missing data in which the missing value is imputed with the previous value.
Other imputation techniques include replacing missing value with arbitrary value by making an educated guess, replacing value with mean,mode or median, backward fill in which missing data is imputed with next value and lastly the method of interpolation in which missing value is replaced by known value on either side of the missing value to calculate an estimated value that fits the trend.
Once the missing data is handled and we have a clean and complete dataset, the next step is to use this data to train the forecasting model.

Time Series Forecasting and Analysis
A time series forecasting is a statistical technique used to analyze and predict patterns in the data where when an historical data stops at one particular point of time and stockholders have trouble finding or predicting the outcome of tomorrow or day after or a week or a month or even a year, this pivotal technique is used to help them in order to let them know if it is worth investing or not.
We have a dataset and when we take historical data that is plotted against the graph, the graph is stopped at one point of time and it’s really hard for an average human to predict if the stock is worth investable or not. This is where time series forecasting and analysis can help us to understand the data. By using various statistical evaluation and comprehensive analysis, the graph can be weaved further beyond the dates or into the future, allowing stockholders to understand at what level the company/business is thriving and based on these rational information, stakeholders are able to invest in companies or not based on these decisions.	
In order to do TimeSeries forecasting there are various models that we can do TimeSeries Forecasting that includes LSTM MODEL, SARIMAX MODEL, FACEBOOK PROPHET and so on. Using these models, we are able to extract the data, plot the data and finally predict the data given in order to find the graph of the subsequent future years where the stock prices are going. 
In order to find the subsequent years of prediction there are certain factors which we need to analyze and later remove, which impedes the stock prices of the company.
Trends: 
A trend normally represents a direction on a graph when plotted that persists over a set or maybe extended period of time.These normally move in upward direction (growth) or downward direction (decline) where understanding them them allow us to device various criterias including forecasting the time period, finding 6 months later what will happen or take decision based on finance and so on
There are differ types of trends that can be observed in time series data:
Linear Trend: A linear trend is a straight-line movement, which moves either upward direction or downward direction showcasing a consistent rate of change over a set period of time. For example, a linear upward trend could indicate steady growth in sales over a period of time and linear downward trend indicates decline in sales over a period of time.
Non-linear Trend: A non-linear trend shows an irregular pattern in the data, suggesting a changing rate of growth or decline.
Seasonal Trend: A seasonal trend is where there is a pattern over repeating intervals at particular instances of time.For example, retail sales might have higher peaks during holiday seasons than during spring season.
Cyclical Trend: Cyclical trends are similar to seasonal trends but occur over more extended periods. These trends typically do not have fixed periods and can span multiple years.

Why is Seasonality is important:
Knowing cyclic patterns: Understanding seasonal components of the data is crucial to understand what exactly is happening in the data. For instance when there is christmas the sales are proliferated hence high market and low market during spring season. Understanding this will improve the understanding of our model
Predicting: Seasonality helps in identifying unusual events in the time series data. An unexpected deviation from the seasonal pattern could indicate an impeding issue or event that requires extra attention. By predicting or forecasting the data we’re able to find out what will happen in the data by predicting on plot graph and evaluating what we need to be doing much later
Data decomposition: This is the process where data scientist evaluate the stocks of the model by decomposing the data into trends, seasonality and residual. With these information, people can identify and start working out on the data that needs to be evaluated
Modeling: Models like seasonal autoregressive integrated moving average (SARIMA) and seasonal autoregressive integrated moving average with exogenous factor (SARIMAX) are specifically designed to handle situations of seasonality in data in the above methods and able to forecast the value and able to make decision making strategies.

Time Series Forecasting Considerations and Applications
The effectiveness of time series forecasting heavily relies on the volume of available data given. With more data points, the accuracy of predictions improves, and a better understanding of the underlying patterns emerges. 
Forecasting a shorter time horizon is relatively easier, but the quality of the data plays a vital role. It is crucial to ensure that the collected data is comprehensive, consistent, free from redundancy, and uniform across different datasets. These considerations are essential for successful time series forecasting
Time series forecasting is widely used in machine learning and has a number of useful practical applications such as demand forecasting for retail and dynamic pricing, detecting anomalies in cybersecurity and fraud prevention, and price prediction for customers.
In this project, we use the prophet tool developed by facebook for  time series forecasting to predict future stock prices, providing valuable insights to customers about the potential behavior of a stock in the coming days. Using this information, customers can then make informed decisions about whether investing in a specific stock aligns with their interests and financial goals.
Prophet
In our project, we chose the Prophet library for forecasting data due to its numerous advantages. It offers both accuracy and speed, providing forecasts that can be finely tuned to enhance prediction accuracy. Moreover, the Prophet library is readily available in Python, making it easy to implement in our code.
 Another notable feature is its ability to accommodate seasonality, making it well-suited for time series forecasting. Additionally, Prophet handles outliers by automatically identifying and removing them, further enhancing the reliability of its predictions.
The Prophet has a number of hyperparameters that it takes. We have focused on 4 main hyperparameters in this project and tuned them and selected their values such that it fits our model best. These parameters are :
Changepoint_prior_scale: Determines how sensitive the model is to changes in trend
 Seasonality_prior_scale: controls the extent of the influence of seasonal patterns in the model 
 Seasonality_mode: In our model, we set the seasonality_mode to multiplicative, as it accurately represents the seasonal components of the data.
 Daily_seasonality: This parameter was set to true in order to incorporate daily patterns into the model to make forecasts more efficient.
We have also added holidays specific to the US to our model which additionally helps in capturing seasonality and other effects related to holidays.
Once the essential hyperparameters and the country-specific holidays are included, the Prophet model is then fitted to the historical data, which serves as the training set. During the fitting process, the model learns from the historical patterns and trends in the data
The model will then use this information to make future predictions. In this project, the model predicts the expected behavior of the stock prices the next three months.

ARIMA:
ARIMA MODEL or AutoRegression Integrated Moving Average is a TimeSeries model used to identify and forecast the data based on the data given. This model is based on the ARMA model but due to the issues of stationarity which is predominantly needed to check the timeSeries forecasting, the use of differencing is utilized. Unlike the Prophet model which can handle outliers and seasonality, this model is rather traditional and needs fundamental parameters that need to be utilized in order to predict the model. As the name suggests we need to do 3 parameters in order to build the ARIMA Model.
AR: The autoregressive component involves using lags to predict future values. The “p” represents the number of lags. 
I: The integrated component refers to the differencing of the time series data to make it stationary. [Stationarity are properties of the time series (e.g., mean, variance)that are not arbitrary or do not change over time]. Differencing involves subtracting the current observation from the previous one to remove trends or seasonality; they denote the “d” order.
MA: The moving average component uses past forecast errors to predict future values. They denote “q” order 
The ARIMA model notation ARIMA(p, d, q):
“p” is the order of the autoregressive (AR) component.
“d” is the order of differencing applied to achieve stationarity - (I) component
“q” is the order of the moving average (MA) component.
To apply the ARIMA model, the following steps be typically follow:
Resample The data: Ensure to resample the data to fill in the missing value either by using ffill() or bfill() or extrapolate the data to make sure the dataset is filled with missing values.
Preprocessing the data: Check for stationarity in the time series data. If the data are not stationary, apply differencing until stationarity is achieved.
Identify Parameters: Find the values of “p,” “d,” and “q” for this model. This is often done using techniques like the autocorrelation function (ACF) and partial autocorrelation function (PACF) plots for smaller datasets but huge datasets we can use the auto_arima function to get the values.
Forecast the Model: After getting p,d,q add them to the ARIMA model for training data.
Forecasting: Use it to make predictions for future time steps.
Evaluate the model: Evaluate the performance of the ARIMA model using mean squared error (MSE) or mean absolute error (MAE).
ACF FUNCTION:
AutoCorrelation Function (ACF) measures the correlation between a time series and its lagged values. It helps to identify the presence of any significant autocorrelation in the data. The ACF be calculated for different lags (time lags) and plotted as a function of the lag.
The ACF plot is a bar chart where the x-axis denotes the lag, and the y-axis denotes the correlation coefficient. The correlation coefficient ranges from -1 to 1. A positive value indicates a positive correlation, a negative value indicates a negative correlation, and a value close to 0 indicates little or no correlation.
In the ACF plot, the significant spikes or bars above the horizontal confidence interval bands (often represented by dashed lines) indicate the presence of autocorrelation at those specific lags. If there are spikes outside the confidence intervals, it suggests that the data have significant autocorrelation at those lags.
By using this function we’re able to determine the value of order “p” for the use of ARIMA model
PACF FUNCTION:
Partial Autocorrelation Function (PACF) measures the correlation between a time series and its lagged values.It helps identify the direct relationship between a data point and its lagged values, excluding the influence of the intervening lags.
The PACF plot is similar to the ACF plot, with the x-axis representing the lag and the y-axis representing the correlation coefficient. However, in the PACF plot, only the direct relationship between a data point and its lagged values be shown, and the correlation coefficients for the intermediate lags be set to zero.
In the PACF plot, significant spikes or bars above the confidence intervals indicate a strong direct relationship between the data point and its lagged values at those specific lags.
By using this function we’re able to determine the value of order “q” for the use of ARIMA model
Issues with ARIMA MODEL:
Since this model can predict the future sales of the upcoming months the biggest drawback is it doesn’t factor the use of seasonality as mentioned seasonality is a component that extrapolates the sales of a company. Since the model doesn’t take this factor the model we’re able to predict will throw false information which inhibits the decision making strategies for money making profits. Hence the most solid factor here is SARIMA Model
SARIMA:
SARIMA (Seasonal AutoRegressive Integrated Moving Average) is a model that combines the ARIMA model with seasonal effects. It is a powerful time series forecasting model used to predict future values in time series data that exhibit both non-seasonal and seasonal patterns.
It includes most of the things in what discussed in ARIMA model but there are extra parameters utilized on this model:-
Seasonal AutoRegressive (SAR) Component:The seasonal autoregressive component models the relationship between the time series and its past seasonal values (lags). The “P” parameter represents the number of seasonal lagged terms used.
Seasonal Integrated (SI) Component: The seasonal integrated component deals with seasonal differencing to achieve seasonal stationarity in data. The “D” parameter represents the number of times seasonal differencing can be applied.
 Seasonal Moving Average (SMA) Component: The seasonal moving average component models the relationship between the time series and its past seasonal forecast errors (residuals). The “Q” parameter represents the number of past seasonal forecast errors.
SARIMA model be denote by de notation SARIMA(p, d, q)(P, D, Q, s), where:
 “p” is the order of the AR component.
 “d” is in the order of non-seasonal differencing.
 “q” is the order of the MA component.
 “P” is the order of the seasonal AR component.
 “D” is the order of seasonal differencing.
 “Q” is the order of the seasonal MA component.
 “s” is the length of the seasonal period (e.g., 12 for monthly data with yearly seasonality).
SARIMA models are particularly useful for time series data with clear seasonal patterns. By incorporating seasonal components, it can account for the seasonal variations and make more accurate forecasts. The parameters of the SARIMA model are typically determined using techniques like ACF (Autocorrelation Function), PACF (Partial Autocorrelation Function), information criteria (AIC, BIC), and cross-validation.
AIC stands for Akaike Information Criterion. It is a statistical measure used in model selection to compare different models and choose the best-fitting model for a given dataset. The AIC is particularly useful when dealing with models that involve some form of parameter estimation, such as regression models and time series models like ARIMA and SARIMA.
BIC stands for Bayesian Information Criterion.. Like AIC (Akaike Information Criterion), BIC is a statistical measure used for model selection and comparison. It is particularly useful when dealing with models that involve parameter estimation, such as regression models and time series models like ARIMA and SARIMA.
We use AIC, BIC in autoArima function from import pmdarima to get the values of (p, d, q)(P, D, Q, s)
SARIMAX:
SARIMAX (Seasonal AutoRegressive Integrated Moving Average with eXogenous variables) model is an additional component of the SARIMA (Seasonal AutoRegressive Integrated Moving Average) model that adds exogenous factors into considerations. Exogenous variables are external factors or predictors that are not part of the time series but may have an influence on it.
Additionally, de SARIMAX model include the following components for exogenous variables similar to SARIMAX MODEL:
Exogenous (X) Component: The exogenous component represents the influence of external predictors or exogenous variables on the time series. These variables are not part of the time series but are believed to have a relationship with dependent variables. De exogenous variables are included in the model as additional regressors.

Performance Metrics
Performance metrics are vital in assessing the effectiveness and efficiency of forecasting models. These metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), Median Absolute Percentage Error (MdAPE), Symmetric Mean Absolute Percentage Error (SMAPE), and others. A clear understanding of these metrics helps us to evaluate the  time-series forecasting model's performance and make necessary adjustments for improvement.
Some of the performance metrics that I came across during my research are as follows:
MAE- shows us the extent of inaccuracy to expect from the forecast on an average
MAPE- lower the MAPE value, better is the model. This metric works better with data that is devoid of zeros and extreme values.
MSE- defined as the average of error squares. This metric helps to evaluate the quality of the forecasting model. Closer the MSE is to 0, better is the model.
RMSE- This metric is in the same unit as projected value, making it easier to comprehend.  Lower the value, higher is the performance of a model.
MdAPE- Uses median instead of mean, to reduce the influence of outlier and extreme values on the forecast. Especially useful in cases when the training data contains substantial outliers, thus providing an efficient way to measure forecast accuracy compared to other models.
SMAPE- It is a symmetric metric which treats positive and negative percentage errors equally. This is beneficial for analyzing forecast accuracy and avoiding any directional bias in error calculation.

In this project, we utilized cross_validation and performance_metrics, which are built-in functions in Prophet, to evaluate the performance and prediction accuracy of our model across multiple time periods, thereby determining the overall stability of the model. By leveraging the performance_metrics function, we obtained a list of performance metric values applied to specific data, allowing us to gauge the model's performance against actual data. This, in turn, enabled us to fine-tune the hyperparameters accordingly , leading to improved results and a more accurate forecasting.

STREAMLIT:
Streamlit is a Python library that allows us to build custom web apps which we have implemented in our project to showcase what we’ve done .Using this library we were able to curate and build a foundation of this project.
They’re designed to be beginner-friendly and require minimal requiremental code to get started. These offer a wide range of features which includes include:
Easy-to-use: Streamlit is easy to use, hence helping us bind our model with the web UI.
Data visualization: Streamlit integrates seamlessly with popular data visualization libraries like Matplotlib, Plotly, and Altair. Since our model required heavy usages of parameters that can’t be displayed easily, this library gives us enough tools to display them on screen
Machine learning integration: Streamlit in our case would be to use fbprophet,alpha_vantage,altair,plotlib and other libraries integrated with streamlit.
Customization: Streamlit offers a wide range of customization options that makes our project look appealing and nuanced.
Sharing and deployment: Streamlit apps can be easily shared and deployed easily through a web browser.
In order to install streamlit,
To get started with Streamlit, You can install Streamlit using pip, run the following command in your terminal or command prompt:
pip install streamlit or !pip install streamlit
Basic Usage:
Streamlit works by turning Python scripts into interactive web apps. To create a Streamlit app, you typically write a Python script which also includes various Streamlit commands to build the app's layout, add widgets, and display data visualizations. The script is saved with a .py extension.
Import streamlit as st —> importing streamlit library
In order to run this web-based UI we need to execute this command on the terminal section in order for the web UI to be displayed on our browser
syntax : /path/folder streamlit run python_file.py
This will launch a local web server, and you can access your app in your web browser at http://localhost:8501.

Working:
In this project, the Streamlit UI is used to develop a stock prediction web application. The code developed imports the Streamlit library and makes use of it’s various functions and methods to develop a user-friendly, easy to access and understandable web application.
Among the various functions provided by Streamlit, we have used the st.markdown() function with the help of which, we have used  HTML and CSS to help format and style the layout of the web application.
st.text_input()  function is also used to take user input for the stock they wish to analyze and get the prediction and relevant information for.
After the user inputs the stock name, the code then maps the stock name to it’s relevant ticker symbol and then proceeds to retrieve important financial data and historical data pertaining to the stock from the alpha vantage api. 
Based on the financial data retrieved and upon comparison to the threshold values of what a good stock’s financial ratios should be like, the UI then displays if the stock is a good investment or not. This is followed by displaying the various company financial ratios, balance statement, income statement, cashflow statement and stock prediction graph for the next three months for user reference. The code uses the Prophet library to predict the stock prices.
The results and graph visualization is displayed using the Streamlit function st.plotly_chart(). Additionally, st.write() function is used for all the printed statements.
The webpage developed looks as follows:








Conclusion:
The combination of the time series model Prophet and the user-friendly Streamlit UI app offers a powerful and accessible solution for building interactive and dynamic web applications for time series analysis and forecasting.
Prophet is a robust time series forecasting model developed by Facebook that simplifies the process of creating accurate predictions for time-dependent data. Its ability to handle various time series patterns, such as seasonality and holidays, makes it a popular choice for both beginners and experienced data scientists in the field of time series analysis.
Streamlit, on the other hand, complements Prophet by providing a simple and straightforward framework for creating web applications. With Streamlit's easy-to-use API, users can quickly prototype and deploy data-driven apps without the need for extensive web development expertise. Its seamless integration with data visualization libraries and machine learning frameworks makes it an ideal choice for showcasing the results of FBProphet's predictions in an interactive and visually appealing manner.
When combined, Prophet and Streamlit empower users to build end-to-end time series analysis applications with ease. Data scientists and analysts can leverage the power of FBProphet to generate accurate forecasts, while the Streamlit UI app enables them to share their findings and insights with stakeholders or the wider public through a web browser.
Overall, the integration of Prophet and Streamlit provides a simple yet effective way to leverage the power of time series forecasting in a user-friendly web application, making it accessible to a broader audience and facilitating data-driven decision-making in various industries and domains.
References:
1. Stock Market Foundations - Amateur to Wizard in 3 Hours. https://courses.10baggerstocks.com/courses/optionstraderpro
2. When the best insights in the room may not be yours.. https://doublingdown.wordpress.com/2017/02/18/when-the-best-insights-in-the-room-may-not-be-yours/
3. What is a Financial Advisor? - Best Accounting Schools. https://www.bestaccountingschools.net/faq/financial-advisor/
4. Blogs - Insight, advice, news, and solutions | Syncloop. https://syncloop.com/blog.html
5. The Complete Guide to Training MTE with TMs - Contentech. https://contentech.com/the-complete-guide-to-training-mte-with-tms/
6. Yu, G., Feng, H., Feng, S., Zhao, J., & Xu, J. (2021). Forecasting hand-foot-and-mouth disease cases using wavelet-based SARIMA–NNAR hybrid model. PLoS One, 16(2), e0246673.
7. Appendix A. List of acronyms | Forecasting: theory and practice. https://forecasting-encyclopedia.com/acronyms.html 






























