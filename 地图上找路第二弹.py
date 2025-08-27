# _*_ coding : utf-8 _*_
# @Time : 2025/7/26 13:33
# @Author : 田园
# @File : 地图上找路第二弹
# @Project : 地图上找路.py

# 引入turtle
import turtle

# 1.
turtle.speed(1)
# 该步骤是为了防止移动时出现走过的那条线，有需要这条线的时候，有不需要的时候，此时暂时不需要
turtle.up()
screen=turtle.Screen()
screen.setup(600,400)
# 向该坐标移动
turtle.goto(-200,0)
# 移动时划线
turtle.down()
turtle.color('aqua')
# 线的粗细
turtle.pensize(20)
turtle.goto(0,0)
turtle.goto(200,100)
# 若下一次需要划线的话，这步骤就不需要，不需要划线，则需调用up()
turtle.up()

# 2.
# 模块样式设置
turtle.turtlesize(2)
turtle.shape('circle')
turtle.color('black','red')
# 在现在的位置留下痕迹
turtle.stamp()
turtle.write('A',align='center',font=('Arial',14))
turtle.goto(0,0)
turtle.stamp()
turtle.write('C',align='center',font=('Arial',14))
turtle.goto(-200,0)
turtle.stamp()
turtle.write('B',align='center',font=('Arial',14))
turtle.hideturtle()
#
# 3.
turtle.turtlesize(0.8)
turtle.shape('arrow')
# 向该坐标移动，并画出向该坐标移动的指针
turtle.towards(0,0)
turtle.pensize(5)
turtle.color('yellow')
turtle.down()
turtle.showturtle()
turtle.goto(0,0)


# 启动 Tkinter 事件循环，保持绘图窗口持续显示，并等待用户交互
turtle.mainloop()

