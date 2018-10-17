from pyecharts import Bar
from pyecharts import Geo
from pyecharts import Style
from pyecharts import GeoLines
from pyecharts import Graph
from pyecharts import Radar

'''
    利用pyecharts我们可以作图的类型分别为：Bar（柱状图/条形图），Bar3D（3D 柱状图），Boxplot（箱形图），EffectScatter（带有涟漪特效动画的散点图），Funnel（漏斗图），
    Gauge（仪表盘），Geo（地理坐标系），Graph（关系图），HeatMap（热力图），Kline（K线图），Line（折线/面积图），Line3D（3D 折线图），Liquid（水球图），
    Map（地图），Parallel（平行坐标系）Pie（饼图），Polar（极坐标系），Radar（雷达图），Sankey（桑基图），Scatter（散点图），Scatter3D（3D 散点图），
    ThemeRiver（主题河流图），WordCloud（词云图）。
'''

# 柱状图
def test1():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
    bar.render(path="render.html")

'''
    散点地图
'''
def test2():
    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15),
        ("赤峰", 16), ("青岛", 18), ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21),
        ("日照", 21), ("胶南", 22), ("南通", 23), ("拉萨", 24), ("云浮", 24), ("梅州", 25),
        ("文登", 25), ("上海", 25), ("攀枝花", 25), ("威海", 25), ("承德", 25), ("厦门", 26),
        ("汕尾", 26), ("潮州", 26), ("丹东", 27), ("太仓", 27), ("曲靖", 27), ("烟台", 28),
        ("福州", 29), ("瓦房店", 30), ("即墨", 30), ("抚顺", 31), ("玉溪", 31), ("张家口", 31),
        ("阳泉", 31), ("莱州", 32), ("湖州", 32), ("汕头", 32), ("昆山", 33), ("宁波", 33),
        ("湛江", 33), ("揭阳", 34), ("荣成", 34), ("连云港", 35), ("葫芦岛", 35), ("常熟", 36),
        ("东莞", 36), ("河源", 36), ("淮安", 36), ("泰州", 36), ("南宁", 37), ("营口", 37),
        ("惠州", 37), ("江阴", 37), ("蓬莱", 37), ("韶关", 38), ("嘉峪关", 38), ("广州", 38),
        ("延安", 38), ("太原", 39), ("清远", 39), ("中山", 39), ("昆明", 39), ("寿光", 40),
        ("盘锦", 40), ("长治", 41), ("深圳", 41), ("珠海", 42), ("宿迁", 43), ("咸阳", 43),
        ("铜川", 44), ("平度", 44), ("佛山", 44), ("海口", 44), ("江门", 45), ("章丘", 45),
        ("肇庆", 46), ("大连", 47), ("临汾", 47), ("吴江", 47), ("石嘴山", 49), ("沈阳", 50),
        ("苏州", 50), ("茂名", 50), ("嘉兴", 51), ("长春", 51), ("胶州", 52), ("银川", 52),
        ("张家港", 52), ("三门峡", 53), ("锦州", 54), ("南昌", 54), ("柳州", 54), ("三亚", 54),
        ("自贡", 56), ("吉林", 56), ("阳江", 57), ("泸州", 57), ("西宁", 57), ("宜宾", 58),
        ("呼和浩特", 58), ("成都", 58), ("大同", 58), ("镇江", 59), ("桂林", 59), ("张家界", 59),
        ("宜兴", 59), ("北海", 60), ("西安", 61), ("金坛", 62), ("东营", 62), ("牡丹江", 63),
        ("遵义", 63), ("绍兴", 63), ("扬州", 64), ("常州", 64), ("潍坊", 65), ("重庆", 66),
        ("台州", 67), ("南京", 67), ("滨州", 70), ("贵阳", 71), ("无锡", 71), ("本溪", 71),
        ("克拉玛依", 72), ("渭南", 72), ("马鞍山", 72), ("宝鸡", 72), ("焦作", 75), ("句容", 75),
        ("北京", 79), ("徐州", 79), ("衡水", 80), ("包头", 80), ("绵阳", 80), ("乌鲁木齐", 84),
        ("枣庄", 84), ("杭州", 84), ("淄博", 85), ("鞍山", 86), ("溧阳", 86), ("库尔勒", 86),
        ("安阳", 90), ("开封", 90), ("济南", 92), ("德阳", 93), ("温州", 95), ("九江", 96),
        ("邯郸", 98), ("临安", 99), ("兰州", 99), ("沧州", 100), ("临沂", 103), ("南充", 104),
        ("天津", 105), ("富阳", 106), ("泰安", 112), ("诸暨", 112), ("郑州", 113), ("哈尔滨", 114),
        ("聊城", 116), ("芜湖", 117), ("唐山", 119), ("平顶山", 119), ("邢台", 119), ("德州", 120),
        ("济宁", 120), ("荆州", 127), ("宜昌", 130), ("义乌", 132), ("丽水", 133), ("洛阳", 134),
        ("秦皇岛", 136), ("株洲", 143), ("石家庄", 147), ("莱芜", 148), ("常德", 152), ("保定", 153),
        ("湘潭", 154), ("金华", 157), ("岳阳", 169), ("长沙", 175), ("衢州", 177), ("廊坊", 193),
        ("菏泽", 194), ("合肥", 229), ("武汉", 273), ("大庆", 279)]

    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",
              title_pos="center", width=1200,
              height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    # 散点
    geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff",
            symbol_size=15, is_visualmap=True)
    geo.render(path="scatter.html")

    # 动态散点
    geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
    geo.render("effect.html")
    '''
        attr：标签名称（在例子里面就是地点）
        value：数值（在例子里就是流动人员）
        visual_range：可视化的数值范围
        symbol_size：散点的大小
        visual_text_color：标签颜色
        is_piecewise ：颜色是否分段显示（False为渐变，True为分段）
        is_visualmap：是否映射（数量与颜色深浅是否挂钩）
        maptype ：地图类型，可以是中国地图，省地图，市地图等等
        visual_split_number ：可视化数值分组
        geo_cities_coords：自定义的经纬度
    '''
    # headmap
    geo.add("", attr, value, type="heatmap", is_visualmap=True, is_piecewise=True,visual_range=[0, 300],
            visual_text_color='#fff')
    geo.render("headmap.html")

# 地理坐标系线图（适合做出行）
def test3():
    style = Style(title_top="#fff", title_pos="center", width=1200, height=600, background_color="404a59")
    style_geo = style.add(is_label_show=True, line_curve=0.2, line_opacity=0.6, legend_text_color="#eee",
                          legend_pos="right", geo_effect_symbol="plane", geo_effect_symbolsize=15,
                          label_color=['#a6c84c', '#ffa022',
                                       '#46bee9'],
                          label_pos="right", label_formatter="{b}", label_text_color="#eee", )
    data_guangzhou = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]
    ]
    geolines = GeoLines("GeoLines 示例", **style.init_style)
    geolines.add("从广州出发", data_guangzhou, **style_geo)
    geolines.render("coordinate.html")

# 关系图
def test4():
    nodes = [{"name": "结点1", "symbolSize": 10},
             {"name": "结点2", "symbolSize": 20},
             {"name": "结点3", "symbolSize": 30},
             {"name": "结点4", "symbolSize": 40},
             {"name": "结点5", "symbolSize": 50},
             {"name": "结点6", "symbolSize": 40},
             {"name": "结点7", "symbolSize": 30},
             {"name": "结点8", "symbolSize": 20}]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    graph = Graph("关系图-环形布局示例")
    graph.add("", nodes, links, is_label_show=True,
              graph_repulsion=8000, graph_layout='circular',
              label_text_color=None)
    graph.render("graph.html")

# 雷达图
def test5():
    schema = [
        ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
        ("客服", 38000), ("研发", 52000), ("市场", 25000)
    ]
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radar = Radar()
    radar.config(schema)
    radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
    radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,
              legend_selectedmode='single')
    radar.render("radar.html")

from pyecharts import WordCloud
import sys

'''
    词云图
'''
def test6():
    name = [
            'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
            'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
            'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
            'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break1']
    value = [
        10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
        965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.render("wordcloud.html")


if __name__ == "__main__":
    test6()
