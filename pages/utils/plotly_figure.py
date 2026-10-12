import plotly.graph_objects as go

def plotly_table(dataframe):
    header_color = '#1f77b4' # Professional Blue theme
    row_even_color = '#f8fbf8'
    row_odd_color = 'white'

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(dataframe.columns),
            fill_color=header_color,
            font=dict(color='white', size=12)
        ),
        cells=dict(
            values=[dataframe[col] for col in dataframe.columns],
            fill_color=[[row_odd_color, row_even_color] * (len(dataframe)//2 + 1)]
        )
    )])
    return fig
