import pygal
from pygal.style import LightStyle
#import pyexcel
import pandas
# pygal


title='my first chart'


data=pandas.read_csv('data.csv',index_col=0,squeeze=True).to_dict()
print(data)

bar_chart=pygal.Bar(style=LightStyle, width=500, height=700, legend_at_bottom=True, human_readable=True, title=title)

my_values1=[]
my_keys1=[]

my_values=data.values()
my_keys=data.keys()
print(my_keys)

for value in my_values:
    my_values1.append(value)
for key in my_keys:
    my_keys1.append(key)

for key in my_keys1:
    bar_chart.add(str(my_keys1),values=my_values1)
bar_chart.render_to_file('bar_chart.svg')