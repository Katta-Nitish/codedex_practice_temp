import pandas as pd
import plotly.express as px
df=pd.read_csv('most_subscribed_youtube_channels.csv')
df['subscribers']=df['subscribers'].str.replace(',','')
#fig=px.histogram(df,x='subscribers',title='subscribers count')
#fig=px.pie(df,values='subscribers',names='category',title='Youtube Categories')
fig=px.box(df,y='started',title='Youtube channel begining')
fig.show()
