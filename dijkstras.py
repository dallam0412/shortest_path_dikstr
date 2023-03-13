import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue as pq
import pygame
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
    if new_node not in obstacle_space and new_node not in visited and new_y<=250:
        cost=cost+1
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))


def down(node,cost,visited):
    new_x=node[0]
    new_y=node[1]-1
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited and new_y>=0:
        cost=cost+1
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))

def left(node,cost,visited):
    new_x=node[0]-1
    new_y=node[1]
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited and new_x>=0:
        cost=cost+1
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))

def right(node,cost,visited):
    new_x=node[0]+1
    new_y=node[1]
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited and new_x<=600:
        cost=cost+1
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))

def up_right(node,cost,visited):
    new_x=node[0]+1
    new_y=node[1]+1
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited and new_x<=600 and new_y<=250 :
        cost=cost+1.4
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))

def up_left(node,cost,visited):
    new_x=node[0]-1
    new_y=node[1]+1
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited and new_x>=0 and new_y<=250:
        cost=cost+1.4
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))

def down_left(node,cost,visited):
    new_x=node[0]-1
    new_y=node[1]-1
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited and new_x>=0 and new_y>=0:
        cost=cost+1.4
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))

def down_right(node,cost,visited):
    new_x=node[0]+1
    new_y=node[1]-1
    new_node=(new_x,new_y)
    if new_node not in obstacle_space and new_node not in visited and new_x<=250 and new_y>=0:
        cost=cost+1.4
        for i in range(len(table)):
            if table[i][2]==new_node:
                if cost<table[i][0]:
                    table[i][0]=cost
                    table[i][1]=node
                    table[i][2]=new_node
                    return
                else:
                    return
        table.append([cost,node,new_node])
        open_list.put((cost,(new_node)))
def convert_coord(coordinate,frame_height):
    return(coordinate[0],frame_height-coordinate[1])
def convert_rect_coord(coordinate,frame_height,rect_height):
    return(coordinate[0],frame_height-coordinate[1]-rect_height)

def disp(bfs,path):
    pygame.init()
    canvas=pygame.display.set_mode((600,250))
    clock=pygame.time.Clock()
    check=True
    while check:
        for loop in pygame.event.get():
            if loop.type==pygame.QUIT:
                check=False
        pygame.draw.rect(canvas,"orange",pygame.Rect(100,0,50,100))
        pygame.draw.rect(canvas,"orange",pygame.Rect(100,150,50,100))
        pygame.draw.polygon(canvas,"orange",((460,25),(460,225),(510,125)))
        pygame.draw.polygon(canvas,"orange",((235,87.5),(300,50),(365,87.5),(365,162.5),(300,200),(235,162.5)))
        for i in bfs:
            pygame.draw.circle(canvas,"white",convert_coord(i,250),1)
            pygame.display.flip()
            clock.tick(1000)
        for i in path:
            pygame.draw.circle(canvas,"black",convert_coord(i,250),1)
            pygame.display.flip()
            clock.tick(20)
        pygame.display.flip()
        pygame.time.wait(5000)
        check=False
        pygame.quit()



map()
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
table.append([0,(start_x,start_y),(start_x,start_y)])
closed_list=[]
print("processing")
while(open_list.empty()==False):
    current_node=open_list.get()
    if current_node[1]==goal:
        break
    closed_list.append(current_node[1])
    up(current_node[1],current_node[0],closed_list)
    down(current_node[1],current_node[0],closed_list)
    left(current_node[1],current_node[0],closed_list)
    right(current_node[1],current_node[0],closed_list)
    up_right(current_node[1],current_node[0],closed_list)
    up_left(current_node[1],current_node[0],closed_list)
    down_right(current_node[1],current_node[0],closed_list)
    down_left(current_node[1],current_node[0],closed_list)
closed_list.append(goal)
back_node=goal
back_track=[back_node]
while(True):
    for i in range(len(table)):
        if table[i][2]==back_node:
            back_node=table[i][1]
            back_track.append(back_node)
            break
    if back_node==start:
        break
print("done")
back_track.reverse()
print(back_track)
disp(closed_list,back_track)