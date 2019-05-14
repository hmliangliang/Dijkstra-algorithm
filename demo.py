import numpy as np


if __name__  == '__main__':
    data = np.array([[0,0,10,0,30,100],[0,0,5,0,0,0],[0,0,0,50,0,0],[0,0,0,0,0,10],[0,0,0,20,0,60],[0,0,0,0,0,0]])
    dist = Dijkstra(data, 0, 2)
    print('0-->5之间的距离长度为:',dist)