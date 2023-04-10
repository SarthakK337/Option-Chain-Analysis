# Option-Chain-Analysis
## Description:

This repository contains the code for an interactive web application that allows users to build options trading strategies for the Indian stock market using the Dash framework. The app provides a user-friendly interface with dropdown menus and input fields for selecting the underlying asset, strike prices, option types, expiration dates, and other parameters of the strategy. The app also visualizes the potential profit and loss (P&L) of the strategy using plotly charts and tables.

The code uses the StrategyBuilder and StratergyPlot1 Python modules to generate the strategy and plot the P&L, respectively. The StrategyBuilder module includes functions to retrieve options chain data from the National Stock Exchange (NSE) website and calculate the P&L of various option strategies, such as Iron Condors, Straddles, and Strangles. The StratergyPlot1 module includes functions to plot the P&L of the strategy using plotly and seaborn libraries.

If you run main.py in desktop you will get this interface.
### Iron Condor Strategy on Desktop App:
![image](https://user-images.githubusercontent.com/90543827/230886091-8a13229a-b946-4f94-903f-a7285ae334b4.png)

you can run App.py in local environment and you will get this kind of interface.
### Iron Condor Strategy on Web App:
![image](https://user-images.githubusercontent.com/90543827/230884839-8fd0570b-00ba-4b21-9293-8007bc6eae02.png)



