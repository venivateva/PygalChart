import pygal
from pygal.style import LightStyle
#import pyexcel
import pandas
# pygal


title='my first chart'
#
# sheet = pyexcel.get_sheet(file_name='data.csv')
#
# svg = sheet.plot(chart_type='pie',title=title,width=600,height=400, explicit_size='True')
#
# #pyexcel.save_as(adict=sheet, dest_title=title,dest_chart_type='pie', dest_file_name='pie.svg', dest_no_prefix=True)
#
# svg.save_as('test.sortable.html',display_lenght=10)

data=pandas.read_csv('data.csv',index_col=0,squeeze=True).to_dict()
print(data)

bar_chart=pygal.Bar(style=LightStyle, width=500, height=700, legend_at_bottom=True, human_readable=True, title=title)
value=data.values()
for key in data:
    bar_chart.add(title=key[0],values=value)
bar_chart.render_to_file('bar_chart.svg')