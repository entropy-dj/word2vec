import torch
from torch import nn


class CBOW(nn.Module):
    '传入词数量，词向量长度'

    def __init__(self, voc_num, voc_dim):
        super().__init__()
        # 定义输入词库x，shape=[4,v]
        # self.codebook = nn.Parameter(torch.randn(voc_num,voc_dim))
        self.codebook = nn.Embedding(voc_num, voc_dim)
        # 定义权重w,shape=[v,v]
        # self.w1 = nn.Parameter(torch.randn(voc_dim,voc_dim))
        self.linear_1 = nn.Linear(voc_dim, voc_dim, bias=False)
        self.linear_2 = nn.Linear(voc_dim, voc_dim, bias=False)
        self.linear_4 = nn.Linear(voc_dim, voc_dim, bias=False)
        self.linear_5 = nn.Linear(voc_dim, voc_dim, bias=False)

    def forward(self, x1, x2, x4, x5):  # 传入索引:[0,1,3,4]
        # 对Embedding对象通过取索引，从形状为[4,v]的词库中取出一个词x1,形状为[1,v]
        # 也就是根据词库中的某个词的索引获取词向量，得到单独的输入x
        v1 = self.codebook(x1)  # [1,v]
        v2 = self.codebook(x2)
        v4 = self.codebook(x4)
        v5 = self.codebook(x5)
        # 取出的四个词向量x分别和权重w做计算，得到输出
        y1 = self.linear_1(v1)  # [1,v]*[v,v]=[1,v]
        y2 = self.linear_2(v2)
        y4 = self.linear_4(v4)
        y5 = self.linear_5(v5)
        y3 = y1 + y2 + y4 + y5
        return y3  # [1,v]

    def getLoss(self, x3, y3):
        # v3就是标签，y3是输出
        v3 = self.codebook(x3)
        return torch.mean((y3 - v3) ** 2)


"""
能做五言绝句的填空
"""
