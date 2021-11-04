import plotly.graph_objects as go
import pandas

df = pandas.read_csv('CandlestickChartsPython/yahooBTC.csv')

candlestick = go.Candlestick(x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'])

figure = go.Figure(data=[candlestick])


figure.layout.xaxis.type = 'category' # only shows days where there is data? (when market open)
#
shapes = [
    dict(x0='2019-01-02', x1='2019-01-02', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2019-05-06', x1='2019-05-06', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2019-07-30', x1='2019-07-30', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2019-10-30', x1='2019-10-30', y0=0, y1=1, xref='x', yref='paper'),
]

annotations=[
    dict(x='2019-01-03', y=0.01, xref='x', yref='paper', showarrow=False, xanchor='left', text='Apple Cuts Guidance'),
    dict(x='2019-05-06', y=0.5, xref='x', yref='paper', showarrow=False, xanchor='left', text='Trump Tariff Tweet'),
    dict(x='2019-07-30', y=0.3, xref='x', yref='paper', showarrow=False, xanchor='left', text='Trump Tweets "China is doing very badly"'),
    dict(x='2019-10-30', y=0.3, xref='x', yref='paper', showarrow=False, xanchor='left', text='Apple Q4 Earnings'),
]

figure.update_layout(title='BTC', annotations=annotations, shapes=shapes)
figure.show()
#figure.write_html('btc.html', auto_open=True)