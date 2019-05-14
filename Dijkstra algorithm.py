# -*- coding: utf-8 -*-#
# Author:       Liangliang
# Date:         2019\5\14 0014 17:10:10
# File:         ESCG.py
# Software:     PyCharm
#------------------------------------
import numpy as np

def Dijkstra(data,v1,v2):#实现的是Dijkstra算法
    '''
    data: 图的邻接矩阵n*n, data[i,j]=1表示两个节点之间存在边的连接,若data[i,j]=0表示两个节点之间不存在边的连接
    v1: 边的起始顶点
    v2: 边的起始终止顶点
    return: 返回的v1到v2之间的最短路径长度
    '''
    graph = np.zeros((data.shape[0],data.shape[0]))#生成图矩阵
    final = np.zeros((1,data.shape[0]))
    D = np.zeros((1, data.shape[0]))
    P = np.zeros((data.shape[0],data.shape[0]))
    for i in range(data.shape[0]):#将无边连接的顶点对之间的权值置为无穷大
        for j in range(data.shape[0]):
            if data[i,j] == 0:
                graph[i,j] = np.inf
            else:
                graph[i, j] = data[i,j]
    for v in range(graph.shape[0]):
        final[0,v] = False
        D[0,v] = graph[v1,v]
        for w in range(graph.shape[0]):
            P[v,w] = False
            if D[0,v] < np.inf:
                P[v,v1] = True
                P[v,v] = True
    D[0,v1] = 0
    final[0,v1] = True
    for i in range(graph.shape[0]):
        minvalue = np.inf
        for w in range(graph.shape[0]):
            if final[0,w] == 0:
                if D[0,w] < minvalue:
                    v = w
                    minvalue = D[0,w]
        final[0,v] = True
        for w in range(graph.shape[0]):
            if final[0,w] == 0 and minvalue + graph[v,w] < D[0,w]:
                D[0,w] = minvalue + graph[v,w]
                P[w,0] = True
                P[w,v] = True
                P[w,w] = True
    #D[0,i]表示从v1到顶点i之间的路径长度,P矩阵中的第i行表示从v1到顶点i的最短路径,P[i,j]=1表示顶点j位于从顶点v1到顶点i的最短路径上
    return D[0,v2]