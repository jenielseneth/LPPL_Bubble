import numpy as np
from pandas import Timestamp
import yfinance as yf



if __name__ == '__main__':
    time = 1016
    start_date = Timestamp('2003-07-01')
    complete_data = yf.download('^GSPC',start_date, Timestamp('2023-07-01'))
    adj_close_data = complete_data['Adj Close']
    i= complete_data.index[int(np.round(time))]
    print(i)