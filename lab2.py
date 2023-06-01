import pandas as pd
import matplotlib.pyplot as plt


def plot():
    df_full = pd.read_json('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&sort=exchangedate&order=asc&json')
    df = pd.DataFrame({"date": df_full[df_full['cc'] == "USD"]['exchangedate'].values,
                       'USD': df_full[df_full['cc'] == "USD"]['rate'].values,
                       'EUR': df_full[df_full['cc'] == "EUR"]['rate'].values})
    df.to_csv("data.csv", index=False)
    df.plot(x='date', y=['USD', 'EUR'], figsize=(20, 10), title="UAH exchange rate")
    plt.savefig('plot.png')


plot()
