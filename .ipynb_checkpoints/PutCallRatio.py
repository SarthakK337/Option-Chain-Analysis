import schedule
import time
from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize


def func():
    #     columns=["Time", 'Call', "Put", "Diff", "PCR", "Price"]
    #     df=pd.DataFrame(columns=columns)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
    json_obj = requests.get(url, headers=headers).json()

    df_data = json_normalize(json_obj["records"]["data"])
    df_strikePrices = json_normalize(json_obj["records"]["strikePrices"])

    for i in df_data.columns:
        if "Date" in i:
            df_data[i] = pd.to_datetime(df_data[i])

    df_data_n = df_data[df_data["expiryDate"] == "2022-12-22"]

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    Call = df_data_n["CE.openInterest"].sum()
    Put = df_data_n["PE.openInterest"].sum()
    Price = df_data_n['PE.underlyingValue'].iloc[0]

    C = [current_time, Call, Put, Put - Call, Put / Call, Price]

    #     df = df.append(pd.Series(C,index = columns),
    #                                 ignore_index = True)

    print(C)


schedule.every(5).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(60 * 5)