"""
python_charts
"""

from pyecharts.charts import Line
from pyecharts.options import *

line = Line()
line.add_xaxis(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
line.add_yaxis("商家A", [120, 132, 101, 134, 90, 230, 210])

# 全局对象
line.set_global_opts(
    title_opts=TitleOpts(title="test", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render()
