# Option-Chain-Analysis
## Description:

This repository contains the code for an interactive web application that allows users to build options trading strategies for the Indian stock market using the Dash framework. The app provides a user-friendly interface with dropdown menus and input fields for selecting the underlying asset, strike prices, option types, expiration dates, and other parameters of the strategy. The app also visualizes the potential profit and loss (P&L) of the strategy using plotly charts and tables.

The code uses the StrategyBuilder and StratergyPlot1 Python modules to generate the strategy and plot the P&L, respectively. The StrategyBuilder module includes functions to retrieve options chain data from the National Stock Exchange (NSE) website and calculate the P&L of various option strategies, such as Iron Condors, Straddles, and Strangles. The StratergyPlot1 module includes functions to plot the P&L of the strategy using plotly and seaborn libraries.

The app is built using the Dash framework, which is a Python library for building web applications with interactive user interfaces. The app uses the Bootstrap theme from the dash_bootstrap_components library to style the components and layout of the app. The app also uses the sklearn and pandas libraries for data processing and the matplotlib and seaborn libraries for data visualization.

The repository includes a requirements.txt file with the required dependencies and a Procfile for deploying the app on Heroku. The app is deployed on the Heroku platform at . The app is for educational and experimental purposes only and should not be used for actual trading without consulting a financial advisor.




