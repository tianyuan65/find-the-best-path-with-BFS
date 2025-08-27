# _*_ coding : utf-8 _*_
# @Time : 2025/7/26 14:02
# @Author : 田园
# @File : 地图找路结合地图和turtle版
# @Project : 地图上找路.py

import turtle
from os import write

#### functions ####
# 初始化数据的函数，如turtle的大小，颜色等等
def initialize():
    turtle.speed(0)
    turtle.up()
    # 窗口样式
    screen = turtle.Screen()
    screen.setup(600, 400)
    # 修改窗口名
    screen.title('Path Finder')

def drawMap():
    # 连接每个点
    turtle.pensize(5)
    turtle.color('gray')
    for start in graph:
        for finish in graph[start]:
            # 向start位置前进
            turtle.goto(position[start])
            # 放下笔，准备画图
            turtle.down()
            # 两个节点之间的中点坐标
            cx=position[start][0]+(position[finish][0]-position[start][0])/2
            cy = position[start][1] + (position[finish][1] - position[start][1]) / 2
            # 向中点坐标前进
            turtle.goto(cx,cy)
            turtle.color('black')
            # 坐标的名，就是A，B
            turtle.write('  '+str(graph[start][finish]))
            # 用灰色线连接每个节点
            turtle.color('gray')
            # 向终点前进
            turtle.goto(position[finish])
            # 抬起笔
            turtle.up()

    # 画出每个点
    turtle.shape('circle')
    turtle.turtlesize(2)
    # 遍历position字典
    for node in position:
        # print('position-node:',node) # A B C D E F G H
        turtle.color('black')
        # 向每个点前进
        turtle.goto(position[node])
        # 在目前的位置留下痕迹
        turtle.stamp()
        # 白色字体
        turtle.color('white')
        # 将node值写在圆形的中间
        turtle.write(node,align='center')
    turtle.hideturtle()

# 找出最适宜路线的函数
def findPath(start,end): # 用上BFS
    # 队列初始化，用空列表来表示
    queue = []
    # 向队列中添加起点，移动的距离，堵车指数，目前经过的路线
    queue.append((start,0, 0,[start]))
    paths=[]
    while queue:
        current,distance,traffic,path=queue.pop(0)
        # print('current:',current)
        if current==end:
            # 将移动的距离，堵车指数以及所有可能的路径加入到paths中
            paths.append((distance,traffic,path))
            continue
        # 遍历目前所在点的堵车指数
        for to in graph[current]:
            # 若是没去过的地点
            if to not in path:
                # 此处运用了勾股定理，计算两点之间的直线距离
                dist=(position[to][0]-position[current][0])**2+ \
                     (position[to][1]-position[current][1])**2
                dist=dist**0.5
                # 则向queue中添加to，也就是要去的位置，从目前为止移动到目标位置移动的距离，堵车指数，以及从该节点能去的所有节点
                queue.append((to,distance+dist,traffic+graph[current][to],path+[to]))
                # print(to,distance+dist,traffic+graph[current][to],path+[to])
    # 起点到终点的直线距离，用勾股定理
    directDistance=(position[end][0]-position[start][0])**2+ \
                     (position[end][1]-position[start][1])**2
    directDistance = directDistance ** 0.5
    scores=[]
    mini=float('inf')
    # 遍历所有路径
    for result in paths:
        # result中包含距离，堵车指数和可能的所有节点
        # print(result)
        # 距离除以起点到终点的直线距离
        d=result[0]/directDistance
        # 寻找最佳路径公式，需要注意比重，20:50
        # score=d*20+(result[1]/d)*50
        # 这样的公式是15:85为最佳路径比例公式
        score=d*15+(result[1]/result[0])*85
        score=int(score)
        scores.append(score)
        # 若设置的mini大于score，则将score的值赋值给mini
        if mini>score:
            mini=score
    print(scores)
    print(paths[scores.index(mini)])
    print('移动的距离：',paths[scores.index(mini)][0])
    print('每条路线平均堵车指数：', paths[scores.index(mini)][1]/result[0])
    return paths[scores.index(mini)][2]

# 用turtle画出路线的函数
def drawPath(path):
    # 连接每个点
    # turtle.speed(1)
    turtle.pensize(5)
    turtle.color('lime')
    # 遍历所有路径的长度-1
    for index in range(len(path)-1):
        # 让海龟移动到 path 路径中第 index 个点所对应的坐标位置。
        turtle.goto(position[path[index]])
        turtle.speed(1)
        turtle.down()
        # 让海龟移动到 path 列表中下一个点（index + 1）
        turtle.goto(position[path[index+1]])
        turtle.up()
    turtle.shape('arrow')
    turtle.showturtle()
    turtle.turtlesize(1)

#### variables ####
# 坐标
position=dict()
position['A']=(-150,150)
position['B']=(100,150)
position['C']=(-200,0)
position['D']=(-125,0)
position['E']=(25,0)
position['F']=(150,0)
position['G']=(25,-100)
position['H']=(150,-100)

# 每个节点间的堵车指数
graph=dict()
# graph['A']={'B':90,'D':20}
# graph['B']={'A':90,'E':50}
# graph['C']={'D':60}
# graph['D']={'A':90,'C':60,'E':30,'G':50}
# graph['E']={'B':50,'D':30,'F':50,'G':15}
# graph['F']={'E':50,'H':15}
# graph['G']={'D':50,'E':15,'H':25}
# graph['H']={'F':15,'G':25}

graph['A']={'B':90,'C':5,'D':20}
graph['B']={'A':90,'E':50,'C':15,'F':20}
graph['C']={'D':60,'A':5,'B':15}
graph['D']={'A':90,'C':60,'E':30,'G':50}
graph['E']={'B':50,'D':30,'F':50,'G':15}
graph['F']={'E':50,'H':15,'B':20}
graph['G']={'D':50,'E':15,'H':25}
graph['H']={'F':15,'G':25}

start='A'
end='H'

#### run ####
initialize()
drawMap()
path=findPath(start,end)
drawPath(path)

turtle.mainloop()
