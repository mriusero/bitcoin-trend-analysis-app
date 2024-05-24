import plotly.graph_objects as go

def create_table(data):
    return data

def create_candlestick_chart(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df["Open"],
                                         high=df["High"],
                                         low=df["Low"],
                                         close=df["Close"]
                                         )
                          ]
                    )
    return fig






