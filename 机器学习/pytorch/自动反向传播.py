# @Time : 2021/4/614:34
# @Author : 周云鹏
# @File : 手工模型创建.PY


import torch

# 人工构建一元线性回归模型
# 准备数据
x = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
y = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]

x = torch.tensor(x)
y = torch.tensor(y)


# 构建模型
def model(x, w, b):
    return w * x + b


# 构建损失
# 模型预测值y_p与真实值y值的差距即为损失，一般使用绝对差值或平方差值
# loss1 = |y_p - y|
# loss2 = (y_p - y)^2 # 常用此种

def loss_fn(y_p, y):
    squared_diffs = (y_p - y) ** 2
    return squared_diffs.mean()


# 初始化参数
# 求解问题的本质是去求解参数w,b， 使得损失越小，那么先得随机初始化w,b。
# params = torch.tensor(data=[1.0,0.0],requires_grad=True)


# 向前计算得到预测值与损失值
# y_p = model(x, *params)
# loss = loss_fn(y_p, y)


# 自动反向计算
# 反向计算是指梯度下降更新参数的过程：求每个参数的梯度–>根据学习率更新参数值

# 更新w,b梯度
def training_loop(n_epochs, learning_rate, params, x, y):
    for epoch in range(1, n_epochs + 1):
        if params.grad is not None:
            params.grad.zero_()
        y_p = model(x, *params)
        loss = loss_fn(y_p, y)
        loss.backward()  # 自动计算梯度
        params = (params - learning_rate * params.grad).detach().requires_grad_()   # 更新梯度
        print('Epoch %d, Loss %f' % (epoch, float(loss)))


# 学习率设置不合适，过大的学习率会导致损失波动，过小的学习率会超慢收敛或陷入局部最优
# 自变量与应变量的数据规模不一致，应缩小自变量的规模，可以乘以一个小的系数，或进行0均值化等
training_loop(
    n_epochs=1000,
    learning_rate=1e-4,  # le-4 减少学习率
    params=torch.tensor([1.0, 0.0], requires_grad=True),
    x=x,  # 自变量与应变量的数据规模不一致，应缩小自变量的规模，可以乘以一个小的系数，或进行0均值化等
    y=y
)
