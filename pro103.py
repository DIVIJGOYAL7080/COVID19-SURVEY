import pandas as pd
import plotly.express as px
df=pd.read_csv('Copy+of+data+-+data.csv')
fig=px.scatter(df,x='date',y='cases',color='country',title='covid-19')
fig.show()