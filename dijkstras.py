import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue as pq
obstacle_space=[]
table=[]
open_list=pq()
def map():
    plt.xlim([0,600])
    plt.ylim([0,250])

    for x in range(100,150):
        for y in range(0,100):
            #plt.scatter(x,y,label="bottom rectange")
            obstacle_space.append((x,y))

    for x in range(100,150):
        for y in range(150,250):
            #plt.scatter(x,y,label="top rectange")
            obstacle_space.append((x,y))

    for x in range(235,365):
        for y in range(85,160):
            #plt.scatter(x,y, label='Map rectangle hexagon')
            obstacle_space.append((x,y))

    for x in range(235,300):
        for y in range(160,198):
            if 38*x - 65*y >= -1470:
                #plt.scatter(x,y,label='top left hexagon')
                obstacle_space.append((x,y))

    for x in range(300,365):
        for y in range(160,198):
            if 38*x + 65*y <= 24270:
                #plt.scatter(x,y,label='top right hexagon')
                obstacle_space.append((x,y))

    for x in range(300,365):
        for y in range(58,85):
            if 27*x - 65*y <= 4330:
                #plt.scatter(x,y,label='bottom right hexagon')
                obstacle_space.append((x,y))

    for x in range(235,300):
        for y in range(58,85):
            if 27*x + 65*y >= 11870:
                #plt.scatter(x,y,label='bottom left hexagon')
                obstacle_space.append((x,y))

    for x in range(460,510):
        for y in range(125,225):
            if 2*x+y <= 1145:
                #plt.scatter(x,y,label='top triangle')
                obstacle_space.append((x,y))
    for x in range(460,600):
        for y in range(25,125):
            if 2*x - y <= 895:
                #plt.scatter(x,y, label='bottom triangle')
                obstacle_space.append((x,y))

def up(node,cost,visited):
    new_x=node[0]
    new_y=node[1]+1
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited:
        cost=cost+1
        open_list.put(cost,new_node)


#map()
check_correct_input=False
while (check_correct_input!=True):
    start_x=int(input("enter the x coordinate of start node"))
    start_y=int(input("enter the y coordinate of start node"))
    start=(start_x,start_y)
    if start in obstacle_space:
        print("start node is in obstacle space")
        continue
    else:
        check_correct_input=True
    goal_x=int(input("enter the x coordinate of goal node"))
    goal_y=int(input("enter the y coordinate of goal node"))
    goal=(goal_x,goal_y)
    if goal in obstacle_space:
        check_correct_input=False
        print("end node is in obstacle space")
open_list.put((0,start))
open_list.put((1,(8,10)))
table.append([0,(goal_x,goal_y),(goal_x,goal_y)])
closed_list=[]
while(open_list.empty()==False):
    current_node=open_list.get()
    closed_list.append(current_node[1])
    up(current_node[1],current_node[0],closed_list)
print(closed_list)
print(table)