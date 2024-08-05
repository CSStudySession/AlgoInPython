'''
给定node和edge的NN定义 实现几个NN的接口. 可以按需添加node和edge的字段.
'''
from typing import List
import math
import random # 给bias node用

class Edge:
    def __init__(self, src:'Node', tar:'Node', w:float):
        self.src = src
        self.tar = tar
        self.w = w
        self.src.outEdges.append(self)
        self.tar.inEdges.append(self)

class Node:
    def __init__(self, index):
        self.index = index
        self.inEdges = []   # incoming edges
        self.outEdges = []  # outgoing edges

        self.fwdVal = None   # 记录到当前点的 前向传播的值
        self.loss = None    # 记录该点反向传播时的损失

        # 在入边集合中 插入一个bias node. 这里权重为uniform分布的随机数
        # For simplicity, all bias nodes are with the same index -1
        self.inEdges.append(Edge(Bias(-1), self, random.uniform(0,1)))

    def activation(self, x): # 激活函数都是sigmoid
        return 1.0 / (1.0 + math.exp(-x))
    
    def get_value(self, inputValues: dict[int, float]) -> float:
        if self.fwdVal:
            return self.fwdVal
        
        if self.index in inputValues:
            self.fwdVal = inputValues[self.index]
        else: # 之前没有计算过该点的前向传播值 取出该点的所有入边 一个个算再累加起来
            val = 0.0
            for edge in self.inEdges: # val=sum(w_i*x_i)
                val += edge.w * edge.src.get_value(inputValues)
            val = self.activation(val) # 过一次激活函数
            self.fwdVal = val
        
        return self.fwdVal
    
    # node0(loss0) w1-> node1(loss1)
    #              w2-> node2(loss2) 
    # loss0 = w1*loss1 + w2*loss2 反向算loss时
    def get_loss(self, targetValues: dict[int, float]) -> float:
        if self.loss:
            return self.loss
        
        if self.index in targetValues:
            self.loss = targetValues[self.index] - self.fwdVal
        else:
            loss = 0.0
            for edge in self.outEdges: 
                loss += edge.w * edge.tar.get_loss(targetValues)
            self.loss = loss # 反向算loss不用过激活函数
        return self.loss            

    
    def update_weight(self, lr): # lr is learning rate
        for edge in self.inEdges:
            # w(t) = w(t-1) +(或者- 取决于怎么定义的loss) lr* dL/dw(t-1)
            # wx + b = p1 --> sigmoid(p1) --> p2 --> loss(p2, label)
            # 由链式法则: dL/dw = dL/dp2 * dp2/dp1 * dp1/dw  
            # dL/dp2: self.loss, dp2/dp1(sigmoid求导): self.fwdVal * (1 - self.fwdVal)
            # dp1/dw = x of input edge = edge.src.fwdVal. 最后乘一个学习率lr
            edge.w += lr * self.loss * edge.src.fwdVal * self.fwdVal * (1 - self.fwdVal)
        
        for edge in self.outEdges:    # 也要更新出边 
            edge.tar.update_weight(lr)

    def clear_NN(self):
        self.fwdVal, self.loss = None, None
        for edge in self.outEdges: # 把当前点的出边对应点清空
            edge.tar.chear_NN()

class NeuralNetwork:
    def __init__(self, layers: List[int]): # layers[i]:第i层有多少个节点
        # 第一层比较特殊 单独拿出来定义
        self.inputLayer = []
        for i in range(layers[0]):
            self.inputLayer.append(Node(i))
        
        offset = layers[0]
        cur = self.inputLayer
        for cnt in range(layers[1:]):
            nxt = [Node(offset + i) for i in range(cnt)]
            offset += cnt
            for cur_node in cur:  # fully connected layers
                for nxt_node in nxt:
                    Edge(cur_node, nxt_node)
            cur = nxt #当前层和下一层连接完 cur指针跳到下一层进行下一次连接
        self.outputLayer = cur # 最后cur停在最后一层上
    
    def clear(self):
        for node in self.inputLayer:
            node.clear_NN()
    
    def forward_calc(self, inputValues) -> dict[int, float]:
        self.clear()
        ret = dict()
        for node in self.outputLayer:
            ret[node.index] = node.get_value(inputValues)
        return ret
        
    def backward_propagation(self, inputValues, targetValues, lr):
        self.forward_calc(inputValues) # 正向跑一次graph

        for node in self.inputLayer: #先收集所有点的loss
            node.get_loss(targetValues)
        
        for node in self.inputLayer:
            node.update_weight(lr)
    
    # followup: support training this NN
    def train(self, samples):
        lr = 0.3
        epoch = 10000
        decay_coeff = 0.99

        for i in range(epoch):
            for input, label in samples:
                self.backward_propagation(input, label, lr)
            lr = lr * decay_coeff # 学习率每个epcho降低一次

# follwup: adding bias to NN nodes
class Bias(Node):
    def __init__(self, idx):
        self.idx = idx
        self.inEdges = []
        self.outEdges = []

        self.fwdVal = 1
        self.get_loss = None

    def get_value(self, intputValues):
        return self.fwdVal
    
    def get_loss(self, label):
        for edge in self.outEdges:
            edge.tar.get_loss(label)
    
    def update_weight(self, lr):
        for edge in self.outEdges:
            edge.tar.update_weight(lr)
    
    def clear_NN(self):
        self.loss = None
        for edge in self.outEdges: # 把当前点的出边对应点清空
            edge.tar.chear_NN()