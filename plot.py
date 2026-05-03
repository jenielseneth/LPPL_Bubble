import numpy as np
from pandas import Timestamp
import yfinance as yf
import datetime
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20})

def plot(plot_list, name, stock, start_date, end_date):
    def lppl(x, a, b, t, m, c, w, phi):
        return (a-b*np.power((t-x),m)*(1+c*np.cos(w*np.log(t-x)+phi))) #(a+b*np.power((t-x),m)+c*np.power((t-x),m)*np.cos(w*np.log(t-x)-phi))
    vlppl = np.vectorize(lppl)

    complete_data = yf.download(stock,start_date, end_date)
    adj_close_data = complete_data['Adj Close']
    data = adj_close_data.values
    data_ln = np.log(data)
    plt.plot(adj_close_data, color='black')
    cmap = plt.get_cmap('rainbow') #rainbow
    colors = [cmap(i) for i in np.linspace(0.1, 0.99, len(plot_list))]
    for idx, params in enumerate(plot_list):
        a, b, t, m, c, w, phi = params[0],params[1],params[2],params[3],params[4],params[5],params[6]
        log_func= vlppl(range(data_ln.size), a, b, t, m, c, w, phi)
        print(idx)
        plt.plot(complete_data.index, np.exp(log_func), label=name[idx], color= colors[idx], linewidth=3)
    i_date=Timestamp(datetime.date(2017,6,11))
    j_date=Timestamp(datetime.date(2017,9,1))
    k_date=Timestamp(datetime.date(2017,11,8))
    plt.plot(i_date, adj_close_data.loc[i_date], 'o', color='black')
    plt.plot(j_date, adj_close_data.loc[j_date], 'o', color='black')
    plt.plot(k_date, adj_close_data.loc[k_date], 'o', color='black')
    legend = [stock]
    plt.legend(legend + name)

if __name__ == '__main__':
    downhill_params =   [   9.06203 , 0.01296 , 339.5 , 0.89872  , -0.00329 ,57.07935, -175.17414]
    ga_params =  [ 10.36094,  0.09222, 406.38671 ,  0.61381,  -0.00013  ,12.24443 ,  3.23418]
    pso_params =  [ 13.034   ,  0.95813, 494.48894 ,  0.29645 , -0.00366 , 35.89392 ,  2.71628]
    ga_pso_params =  [ 10.60832 ,  0.09465, 431.55472,   0.61348 , -0.03734 , 16.43289 ,196.32676]
    pso_ga_params= [ 12.82165,   0.43453, 486.99035 ,  0.42786 , -0.00014,  51.56704 ,  6.48219]
    opt_params = [7.47, 0.014, 1105.8, 0.52, -0.04, 9.87, 2.72]


    params = [downhill_params, ga_params, pso_params, ga_pso_params, pso_ga_params]
    names = [ "DS", "GA", "PSO", "GA-PSO", "PSO-GA",]
    start_date = datetime.date(2017, 1, 1)
    end_date = datetime.date(2017, 12, 1)
    plot(params, names, 'BTC-USD' ,start_date, end_date)
    plt.show()