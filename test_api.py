# 5jvylhNzT7WMGOTQ55Pt8GaGIX2zsT16rlDSgA3f


import json
import pandas as pd
import requests

av_k = "W2J61LUSTTXBV64M"

av_symbol = "GOOGL"

av_link = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}".format(
  av_symbol, av_k)

av_request = requests.get(av_link)

av_json = av_request.json()

series_data = av_json['Weekly Time Series']

meta_data = av_json['Meta Data']

av_data = pd.DataFrame.from_dict(series_data, orient='index')

av_data['symbol'] = meta_data['2. Symbol']

av_data.reset_index(inplace = True)

av_data = av_data.rename(columns = {'index':'date'})

print(av_data.head())


#https://api.data.gov/ed/collegescorecard/v1/schools?api_key=5jvylhNzT7WMGOTQ55Pt8GaGIX2zsT16rlDSgA3f&school.name=University of Notre Dame&fields=id,Notre.Dame,latest.student.size
