import pygal
from pygal.style import LightStyle
import pandas

# read csv data

data = pandas.read_csv('data.csv',index_col=0,squeeze=True).to_dict()
print(data)


# storing the keys and values in lists for indexing

my_values1 = []
my_keys1 = []

my_values = data.values()
my_keys = data.keys()

# add each key and value in a list

for value in my_values:
    my_values1.append(value)
for key in my_keys:
    my_keys1.append(key)
print(my_values1)

# create chart

title = 'my first chart'
bar_chart = pygal.Bar(style=LightStyle, width=500, height=700, legend_at_bottom=True, human_readable=True, title=title)
bar_chart.add(my_keys1[0],values=my_values1[0])
bar_chart.add(my_keys1[1],values=my_values1[1])
bar_chart.add(my_keys1[2],values=my_values1[2])
bar_chart.add(my_keys1[3],values=my_values1[3])
bar_chart.render_to_file('bar_chart.svg')