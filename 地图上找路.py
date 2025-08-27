# _*_ coding : utf-8 _*_
# @Time : 2025/7/19 13:10
# @Author : 田园
# @File : 地图上找路
# @Project : bankaccount.py

# weight graph，需要抽象化先决条件
# that is no direction graph
# 寻找最短路径
def bfs_shortestPath(start,end,graph):
    queue=[]
    # 存储会经过的路线的列表
    # paths=[]
    # 将会经过的地方存储到res的第一个元素中，并在第二个元素的位置存储堵车指数
    res=[[],float('inf')]
    # 向队列中添加起点和从起点到目前位置经过的路线
    # queue.append((start,[start]))
    # 向队列中添加起点和从起点到目前位置经过的路线，以及堵车程度指数
    queue.append((start,[start],0))
    visited=[]
    while queue:
        # current,path=queue.pop(0)
        # 目前所在地，路径和堵车指数
        current, path,weight = queue.pop(0)
        # 向visited中添加刚刚所经路线
        visited.append(current)
        # 若到达目的地
        # if current==end:
        #     # 则向存储路径的列表中添加刚刚所经路线
        #     paths.append(path)
        #     continue
        # 若目前目前所在地等于目的地，且堵车指数大于路线中的堵车值
        if current==end and res[1]>weight:
            # 则，res中加入所经路线和堵车值
            res=[path,weight]
            # print('path-',path)
            continue
        # 遍历graph中车辆经过的路线，将经过的每个点称为节点
        for node in graph[current]:
            # print('node-',node)
            # 若该节点被经过过，或节点在路径中
            if node in visited or node in path:
                # 则继续走
                continue
            else:
                # 否则，就是没走过的路，向目的地移动时，向队列中添加这些会经过的所有可能的节点和路径
                # queue.append((node,path+[node]))
                print('path+[node]:',path+[node])
                # 向目前位置移动时，加上目前为止的堵车程度指数
                queue.append((node,path+[node],weight+graph[current][node]))
    # return paths
    return res

mapGraph={
    'A':{'C':10},
    'B':{'C':10},
    'C':{'A':10,'B':10,'D':50,'G':30},
    'D':{'C':50,'E':10,'H':90},
    'E':{'D':10,'H':40,'I':50},
    'F':{'G':10},
    'G':{'C':30,'F':10,'H':40},
    'H':{'D':90,'E':40,'G':40,'I':10},
    'I':{'E':50,'H':10}
}

result=bfs_shortestPath('A','I',mapGraph)
print(result)
# print(mapGraph['A'])
# 用于查询最适宜路线的公式，score值越大，则表示这条路越通畅，堵车指数越低，
score=len(result[0])*20+(len(result[0]*50))/result[1]
print(score)

# 灵活运用BFS和加重值来寻找最适合的路径
# 项目大纲，profile要写得全面，最后用pdf出示
# 动机：找到地图中最短并且能最短时间内(不堵车)到达目的地
# 项目目标：可视化(把简单画的抽象化的图挂上)
# 表格理论：将每个点连起来的数据表示，就是把上面的mapGraph用点线连起来
    # 加重值表格：将每条路的堵车程度指数加上
    # 有方向的表格：加上指向方向
# 已知背景与BFS演示：在无方向，有费用的加重值表格当中，从起点出发到终点，找到最便捷的路线，在此费用越低并路线最短最好。
# 在此为了方便，用dic类型来抽象化表格
# 项目环境：如Windows，python313
# 目标设计：结果预示，功能介绍
# 地图可视化：
#   利用turtle
#   运用turtle导航
# 运行经过，仔仔细细的写


