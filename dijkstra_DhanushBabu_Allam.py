
import numpy as np
from queue import PriorityQueue as pq
import pygame
obstacle_space=[]
table=[]
open_list=pq()
def map():


    for x in range(0,601):
        for y in range(0,6):
            obstacle_space.append((x,y))

    for x in range(0,601):
        for y in range(245,251):
            obstacle_space.append((x,y))

    for x in range(0,6):
        for y in range(0,251):
            obstacle_space.append((x,y))

    for x in range(595,601):
        for y in range(0,251):
            obstacle_space.append((x,y))
    
    for x in range(100,151):
        for y in range(0,101):
            obstacle_space.append((x,y))
            
    for x in range(95,100):
        for y in range(0,101):
            obstacle_space.append((x,y))

    for x in range(95,100):
        for y in range(145,151):
            obstacle_space.append((x,y))

    
    for x in range(100,151):
        for y in range(101,106):
            obstacle_space.append((x,y))
        for y in range(145,151):
            obstacle_space.append((x,y))
            

    for x in range(151,156):
        for y in range(0,106):
            obstacle_space.append((x,y))
        for y in range(145,250):
            obstacle_space.append((x,y))
        
    
    for x in range(100,151):
        for y in range(150,251):
            obstacle_space.append((x,y))
    
    for x in range(95,100):
        for y in range(150,251):
            obstacle_space.append((x,y))

    for x in range(95,100):
        for y in range(100,105):
            obstacle_space.append((x,y))
    
    for x in range(100,151):
        for y in range(101,105):
            obstacle_space.append((x,y))
    
    for x in range(455,460):
        for y in range(20,230):
            obstacle_space.append((x,y))
    
    for x in range(450,601):
        for y in range(20,230):
            if (2*x - y <= 895) and (2*x+y <= 1145):
                obstacle_space.append((x,y))
    
    for x in range(450,601):
        for y in range(20,230):
            if (2*x+y <= 1156.18) and (2*x - y <= 906.18):
                obstacle_space.append((x,y))
    
    for x in range(220,380):
        for y in range(40,230):
            if  (y - (0.577)*x - (32.692)) < 0 and (y + (0.577)*x - (378.846)) < 0 and (y - (0.577)*x + (128.846)) > 0 and (y + (0.577)*x - (217.307)) > 0 and (230 <= x <= 370):
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

    rect_down_space=convert_rect_coord([95,0],250,105)
    rect_up_space=convert_rect_coord([95,145],250,105)
    tri_space_1=convert_coord([455,20],250)
    tri_space_2=convert_coord([463,20],250)
    tri_space_3=convert_coord([515.5,125],250)
    tri_space_4=convert_coord([463,230],250)
    tri_space_5=convert_coord([455,230],250)
    hex_space_1 = convert_coord([300, 205.76], 250)
    hex_space_2 = convert_coord([230, 165.38], 250)
    hex_space_3 = convert_coord([230, 84.61], 250)
    hex_space_4 = convert_coord([300, 44.23], 250)
    hex_space_5 = convert_coord([370, 84.61], 250)
    hex_space_6 = convert_coord([370, 165.38], 250)
    while check:
        for loop in pygame.event.get():
            if loop.type==pygame.QUIT:
                check=False
        pygame.draw.rect(canvas,"yellow",pygame.Rect(rect_down_space[0],rect_down_space[1],60,105))
        pygame.draw.rect(canvas,"yellow",pygame.Rect(rect_up_space[0],rect_up_space[1],60,105))
        pygame.draw.polygon(canvas,"yellow",((tri_space_1),(tri_space_2),(tri_space_3),(tri_space_4),(tri_space_5)))
        pygame.draw.polygon(canvas,"yellow",((hex_space_1),(hex_space_2),(hex_space_3),(hex_space_4),(hex_space_5),(hex_space_6)))
        pygame.draw.rect(canvas,"orange",pygame.Rect(100,0,50,100))
        pygame.draw.rect(canvas,"orange",pygame.Rect(100,150,50,100))
        pygame.draw.polygon(canvas,"orange",((460,25),(460,225),(510,125)))
        pygame.draw.polygon(canvas,"orange",((235,87.5),(300,50),(365,87.5),(365,162.5),(300,200),(235,162.5)))
        pygame.draw.rect(canvas,"yellow",pygame.Rect(0,0,5,250))
        pygame.draw.rect(canvas,"yellow",pygame.Rect(595,0,5,250))
        pygame.draw.rect(canvas,"yellow",pygame.Rect(0,0,600,5))
        pygame.draw.rect(canvas,"yellow",pygame.Rect(0,245,600,5))

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
    start_x=int(input("enter the x coordinate of start node "))
    start_y=int(input("enter the y coordinate of start node "))
    start=(start_x,start_y)
    if start in obstacle_space:
        print("start node is in obstacle space")
        continue
    else:
        check_correct_input=True
    goal_x=int(input("enter the x coordinate of goal node "))
    goal_y=int(input("enter the y coordinate of goal node "))
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