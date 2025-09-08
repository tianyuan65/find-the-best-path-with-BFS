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
# def findPath(start,end): # 用上BFS
#     # 队列初始化，用空列表来表示
#     queue = []
#     # 向队列中添加起点，移动的距离，堵车指数，目前经过的路线
#     queue.append((start,0, 0,[start]))
#     paths=[]
#     while queue:
#         current,distance,traffic,path=queue.pop(0)
#         # print('current:',current)
#         if current==end:
#             # 将移动的距离，堵车指数以及所有可能的路径加入到paths中
#             paths.append((distance,traffic,path))
#             continue
#         # 遍历目前所在点的堵车指数
#         for to in graph[current]:
#             # 若是没去过的地点
#             if to not in path:
#                 # 此处运用了勾股定理，计算两点之间的直线距离
#                 dist=(position[to][0]-position[current][0])**2+ \
#                      (position[to][1]-position[current][1])**2
#                 dist=dist**0.5
#                 # 则向queue中添加to，也就是要去的位置，从目前为止移动到目标位置移动的距离，堵车指数，以及从该节点能去的所有节点
#                 queue.append((to,distance+dist,traffic+graph[current][to],path+[to]))
#                 # print(to,distance+dist,traffic+graph[current][to],path+[to])
#     # 起点到终点的直线距离，用勾股定理
#     directDistance=(position[end][0]-position[start][0])**2+ \
#                      (position[end][1]-position[start][1])**2
#     directDistance = directDistance ** 0.5
#     scores=[]
#     mini=float('inf')
#     # 遍历所有路径
#     for result in paths:
#         # result中包含距离，堵车指数和可能的所有节点
#         print(result)
#         # 距离除以起点到终点的直线距离
#         d=result[0]/directDistance
#         # 寻找最佳路径公式，需要注意比重，20:50
#         # score=d*20+(result[1]/d)*50
#         # 这样的公式是15:85为最佳路径比例公式
#         score=d*15+(result[1]/result[0])*85
#         score=int(score)
#         scores.append(score)
#         # # 若设置的mini大于score，则将score的值赋值给mini
#         if mini>score:
#             mini=score
#
#     print(scores)
#     print(paths[scores.index(mini)])
#     print('移动的距离：',paths[scores.index(mini)][0])
#     print('每条路线平均堵车指数：', paths[scores.index(mini)][1]/result[0])
#     return paths[scores.index(mini)][2]

# 找出所有路线的函数
def findAllPaths(start,end):
    # 队列初始化
    queue = [(start, [start], 0, 0)]  # (当前节点, 路径, 总距离, 总堵车指数)
    all_paths = []

    while queue:
        current, path, total_distance, total_traffic = queue.pop(0)

        if current == end:
            # 计算平均堵车指数
            avg_traffic = total_traffic / total_distance if total_distance > 0 else 0
            all_paths.append((path, total_distance, total_traffic, avg_traffic))
            continue

        # 遍历邻居节点
        for neighbor in graph[current]:
            if neighbor not in path:
                # 计算到这个邻居节点的距离
                dx = position[neighbor][0] - position[current][0]
                dy = position[neighbor][1] - position[current][1]
                segment_distance = (dx ** 2 + dy ** 2) ** 0.5

                # 获取堵车指数
                traffic = graph[current][neighbor]

                # 添加到队列
                queue.append((
                    neighbor,
                    path + [neighbor],
                    total_distance + segment_distance,
                    total_traffic + traffic
                ))

    return all_paths

# 找出最适宜路线的函数
def findBestPaths(start,end):
    allPaths=findAllPaths(start,end)

    if not allPaths:
        return None,None,None

    # 最短路线
    shortestPath=min(allPaths,key=lambda x:x[1])
    # print('最短路线',shortestPath)  #最短路线 (['A', 'D', 'G', 'H'], 457.346627030655, 95, 0.20771990955042585)
    # 最不堵车路线
    leastTrafficPath=min(allPaths,key=lambda x:x[3])
    # print('堵车指数最低路线',leastTrafficPath)

    # 找出平衡路径（距离和堵车的加权平均）
    # 计算最短距离和最小堵车值作为基准
    min_distance = min(path[1] for path in allPaths)
    min_traffic = min(path[3] for path in allPaths)

    for path in allPaths:
        # 标准化距离和堵车指数 (0-1范围)
        norm_distance = path[1] / min_distance
        norm_traffic = path[3] / min_traffic if min_traffic > 0 else 1

        # 计算加权得分（可以根据需要调整权重）
        score = norm_distance * 0.6 + norm_traffic * 0.4

    return shortestPath, leastTrafficPath

# 用turtle画出路线的函数
# def drawPath(path):
def drawPath(path,color):
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

def displayPathInfo(shortestPath, leastTrafficPath):
    # 创建信息显示区域
    turtle.goto(-350, 150)
    turtle.color('black')
    turtle.write(f"从 {start} 到 {end} 的路径分析", font=("Arial", 16, "bold"))

    # 显示最短路径信息
    turtle.goto(-350, 120)
    turtle.color('green')
    if shortestPath:
        path_str = " -> ".join(shortestPath[0])
        turtle.write(f"最短路径: {path_str}", font=("Arial", 12, "normal"))
        turtle.goto(-350, 100)
        turtle.write(
            f"距离: {shortestPath[1]:.2f}, 总堵车指数: {shortestPath[2]}, 平均堵车指数: {shortestPath[3]:.2f}",
            font=("Arial", 10, "normal"))

    # 显示最少堵车路径信息
    turtle.goto(-350, 70)
    turtle.color('blue')
    if leastTrafficPath:
        path_str = " -> ".join(leastTrafficPath[0])
        turtle.write(f"最少堵车路径: {path_str}", font=("Arial", 12, "normal"))
        turtle.goto(-350, 50)
        turtle.write(
            f"距离: {leastTrafficPath[1]:.2f}, 总堵车指数: {leastTrafficPath[2]}, 平均堵车指数: {leastTrafficPath[3]:.2f}",
            font=("Arial", 10, "normal"))

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
# graph['D']={'A':20,'C':60,'E':30,'G':50}
# graph['E']={'B':50,'D':30,'F':50,'G':15}
# graph['F']={'E':50,'H':15}
# graph['G']={'D':50,'E':15,'H':25}
# graph['H']={'F':15,'G':25}

graph['A']={'B':90,'C':5,'D':20}
graph['B']={'A':90,'E':50,'C':15,'F':20}
graph['C']={'D':60,'A':5,'B':15}
graph['D']={'A':20,'C':60,'E':30,'G':50}
graph['E']={'B':50,'D':30,'F':50,'G':15}
graph['F']={'E':50,'H':15,'B':20}
graph['G']={'D':50,'E':15,'H':25}
graph['H']={'F':15,'G':25}

start='A'
end='H'

#### run ####
initialize()
drawMap()
# path=findPath(start,end)
shortestPath,leastTrafficPath=findBestPaths(start,end)
# drawPath(path)
displayPathInfo(shortestPath,leastTrafficPath)
# 绘制最短路线
if shortestPath:
    drawPath(shortestPath[0],'red')
if leastTrafficPath:
    # 将比移动到起点，避免连线
    turtle.up()
    drawPath(leastTrafficPath[0],'gold')



turtle.mainloop()
