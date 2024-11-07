import plotly.express as px
df = px.data.gapminder()
fig = px.line(df[df['country'] == 'India'], x='year', y='gdpPercap', title='GDP per Capita Over Time')
fig.show()
