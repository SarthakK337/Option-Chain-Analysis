import numpy as np #The Numpy numerical computing library
import pandas as pd #The Pandas data science library
import requests #The requests library for HTTP requests in Python
import xlsxwriter #The XlsxWriter libarary for
import math #The Python math module
import pandas as pd
import json
from pandas import json_normalize

class Strategys:
    def __init__(self):
        self.headers={ 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        self.session=requests.session()
        self.session.get("http://nseindia.com", headers = self.headers,verify=False)

    def option_chain_data(self,symbol, indices=True):
        symbol = symbol.replace(',', '%20').replace('&', '%26')
        if not indices:
            url = 'https://www.nseindia.com/api/option-chain-equities?symbol=' + symbol
        else:
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol=' + symbol
        json_obj = self.session.get(url, headers=self.headers).json()
        data = json_normalize(json_obj["records"]["data"])
        # data["expiryDate"] = pd.to_datetime(data["expiryDate"])
        return data


    def option_data(self, symbol, Expiry, indices=True):
        symbol=symbol.replace(',' ,'%20').replace('&', '%26')
        if not indices:
            url = 'https://www.nseindia.com/api/option-chain-equities?symbol=' + symbol
        else:
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol=' + symbol
        json_obj = self.session.get(url, headers=self.headers, verify=False).json()
        # data = self.session.get(url, headers =self.headers).json()["records"]["data"]
        # my_df = []
        # for i in data:
        #     for k, v in i.items():
        #         if k =="CE" or k == "PE":
        #             info = v
        #             info["instrumentType"] = k
        #             my_df.append(info)
        # df = pd.DataFrame(my_df)
        # df = df.set_index("identifier", drop=True)
        data = json_normalize(json_obj["records"]["data"])
        data["expiryDate"]= pd.to_datetime(data["expiryDate"])
        df=data[data["expiryDate"]==Expiry]
        return df

    def StrikePrice(self, symbol , Expiry):
        try:
            Data = self.option_data(symbol, Expiry)
            df = Data["PE.underlyingValue"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def StrikePrice1(self, symbol):
        try:
            Data = self.option_chain_data(symbol)
            df = Data["PE.underlyingValue"].iloc[0]
        except Exception as e:
            return e
        else:
            return df


    def CallPrice(self, symbol , Expiry, StrikePrice):
        try:
            Data=self.option_data(symbol, Expiry)
            df = Data[Data["CE.strikePrice"] == StrikePrice]["CE.lastPrice"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def PutPrice(self, symbol , Expiry, StrikePrice):
        try:
            Data = self.option_data(symbol, Expiry)
            df = Data[Data["PE.strikePrice"] == StrikePrice]["PE.lastPrice"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def CE_OpenInterest(self, symbol , Expiry, StrikePrice):
        try:
            Data = self.option_data(symbol, Expiry)
            df = Data[Data["CE.strikePrice"] == StrikePrice]["CE.openInterest"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def PE_OpenInterest(self, symbol , Expiry, StrikePrice):
        try:
            Data = self.option_data(symbol, Expiry)
            df = Data[Data["PE.strikePrice"] == StrikePrice]["PE.openInterest"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

class ShortIronCondor(Strategys):

    def MaxProfit(self, symbol , Expiry, CE_strikePrice_Sell,PE_strikePrice_Sell,CE_strikePrice_Buy,PE_strikePrice_Buy):
        try:
            self.CE_Sell = self.CallPrice(symbol, Expiry, CE_strikePrice_Sell)
            self.PE_Sell = self.PutPrice(symbol, Expiry, PE_strikePrice_Sell)
            self.CE_Buy = self.CallPrice(symbol, Expiry, CE_strikePrice_Buy)
            self.PE_Buy = self.PutPrice(symbol, Expiry, PE_strikePrice_Buy)
            self.max=round((self.CE_Sell+self.PE_Sell-self.CE_Buy-self.PE_Buy)*50,2)
        except Exception as e:
            return str(e)
        else:
            return self.max

    def MaxLoss(self, symbol , Expiry, CE_strikePrice_Sell,PE_strikePrice_Sell,CE_strikePrice_Buy,PE_strikePrice_Buy):
        try:
            self.CE_Sell = self.CallPrice(symbol, Expiry, CE_strikePrice_Sell)
            self.PE_Sell = self.PutPrice(symbol, Expiry, PE_strikePrice_Sell)
            self.CE_Buy = self.CallPrice(symbol, Expiry, CE_strikePrice_Buy)
            self.PE_Buy = self.PutPrice(symbol, Expiry, PE_strikePrice_Buy)
            self.PointDIff= max(CE_strikePrice_Buy-CE_strikePrice_Sell,PE_strikePrice_Buy-PE_strikePrice_Sell)
            self.max= round((self.CE_Sell + self.PE_Sell - self.CE_Buy - self.PE_Buy - self.PointDIff) * 50, 2)

        except Exception as e:
            return str(e)

        else:
            return self.max

    def RiskReward(self, symbol , Expiry, CE_strikePrice_Sell, PE_strikePrice_Sell, CE_strikePrice_Buy, PE_strikePrice_Buy):
        try:
            self.ans=round(-(self.MaxLoss(symbol , Expiry, CE_strikePrice_Sell, PE_strikePrice_Sell, CE_strikePrice_Buy, PE_strikePrice_Buy))
                           /self.MaxProfit(symbol , Expiry, CE_strikePrice_Sell, PE_strikePrice_Sell, CE_strikePrice_Buy, PE_strikePrice_Buy)
                           ,2)
        except Exception as e:
            return str(e)

        else:
            return self.ans

    def OverView(self, Index, CE_Sell, PE_Sell, CE_Buy, PE_Buy):
        try:
            mul=50
            if Index=="NIFTY":
                mul=50
            if Index=="BANKNIFTY":
                mul=25
            Max_Profit = round((CE_Sell + PE_Sell - CE_Buy - PE_Buy) * mul, 2)
            Max_Loss = round((CE_Sell + PE_Sell - CE_Buy - PE_Buy - 200) * mul, 2)
            List = [Max_Profit, Max_Loss, round(-Max_Loss / Max_Profit, 2)]
        except Exception as e:
            return [str(e), str(e), str(e)]
        else:
            return List

    def Callprice(self, StrikePrice, Data):
        try:
            df = Data[Data["CE.strikePrice"] == StrikePrice]["CE.lastPrice"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def Putprice(self, StrikePrice, Data):
        try:
            df = Data[Data["PE.strikePrice"] == StrikePrice]["PE.lastPrice"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def CE_Openinterest(self, StrikePrice, Data):
        try:
            df = Data[Data["CE.strikePrice"] == StrikePrice]["CE.openInterest"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def PE_Openinterest(self, StrikePrice, Data):
        try:
            df = Data[Data["PE.strikePrice"] == StrikePrice]["PE.openInterest"].iloc[0]
        except Exception as e:
            return e
        else:
            return df

    def OptionCombination(self,symbol , Expiry, PointDiff):
        df=self.option_data(symbol,Expiry)
        df["Difference"] = df["CE.underlyingValue"] - df["CE.strikePrice"]
        df["Ratio"] = df["CE.openInterest"] / df["PE.openInterest"]

        df_call = df[df["Difference"] < 0].iloc[3:]
        df_put = df[df["Difference"] > 0].iloc[:-3]

        df_call_1 = df_call.sort_values(by=["CE.openInterest"], ascending=False).iloc[:13].sort_values(by=['Ratio'], ascending=False)
        df_put_1 = df_put.sort_values(by=["PE.openInterest"], ascending=False).iloc[:13].sort_values(by=['Ratio'])

        my_columns = ["CE StrikePrice", "CE OpenInterest", 'PE StrikePrice', "PE OpenInterest", "CE StrikePrice 1",
                      "CE OpenInterest 1", 'PE StrikePrice 1', "PE OpenInterest 1", 'Max Profit', 'Max Loss',
                      "Risk/Reward"]
        final_dataframe = pd.DataFrame(columns=my_columns)

        for i in df_call_1["CE.strikePrice"]:
            l = []
            l.append(i)
            l.append(self.CE_Openinterest(i,df))
            for j in df_put_1["PE.strikePrice"]:
                l.append(j)
                l.append(self.PE_Openinterest(j,df))

                l.append(l[0] + PointDiff)
                l.append(self.CE_Openinterest(l[0] + PointDiff,df))

                l.append(l[2] - PointDiff)
                l.append(self.PE_Openinterest(l[2] - PointDiff,df))

                CE_Sell = self.Callprice( l[0],df)
                PE_Sell = self.Putprice(l[2],df)
                CE_Buy = self.Callprice(l[4],df)
                PE_Buy = self.Putprice(l[6],df)
                l = l + self.OverView(symbol ,CE_Sell, PE_Sell, CE_Buy, PE_Buy)
                final_dataframe = final_dataframe.append(
                    pd.Series(l, index=my_columns),
                    ignore_index=True)
                l = [i, self.CE_OpenInterest(symbol,Expiry,i)]

        final_dataframe['Risk/Reward'] = pd.to_numeric(final_dataframe['Risk/Reward'], errors="coerce")
        final_dataframe.dropna(how="any", inplace=True)

        final_dataframe = final_dataframe[final_dataframe["Risk/Reward"] <= 10][final_dataframe["Risk/Reward"] > 0]
        final_dataframe.sort_values(by=["Risk/Reward"])

        final_dataframe["%diff"] = (final_dataframe["CE StrikePrice"] / final_dataframe["PE StrikePrice"] - 1) * 100
        final_dataframe=final_dataframe.sort_values(by=["%diff"], ascending=False)

        return final_dataframe












