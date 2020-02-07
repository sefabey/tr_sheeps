import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



df=pd.read_csv("data/sheeps.csv")
df.columns= ['yas', 'yil', 'sayi']

df['missing']= "seren"

print(df.head(3))


# plot using pyplot
data_to_plot= df.groupby('yil').sum()
data_to_plot.columns
data_to_plot.plot()
plt.show()

# plot using plotly
fig = px.line(data_to_plot, x=data_to_plot.index,y="sayi", title="Sheep Counts in Turkey" ,range_y=[0,40000000])
fig.show()
