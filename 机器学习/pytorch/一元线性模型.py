# @Time : 2021/4/617:27
# @Author : 周云鹏
# @File : 一元线性模型.PY

import torch
import torch.nn as nn
import torch.optim as optim


# 1. 准备数据
x = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
y = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]
x = torch.tensor(x).unsqueeze(1)
y = torch.tensor(y).unsqueeze(1)

n_sample = x.shape[0]
n_val = int(0.2 * n_sample)

shuffled_indices = torch.randperm(n_sample)  # 获取随机正整数
train_indices = shuffled_indices[:-n_val]
val_indices = shuffled_indices[-n_val:]
print(train_indices)
print(val_indices)
train_x = 0.1*x[train_indices]
train_y = y[train_indices]

val_x = 0.1*x[val_indices]
val_y = y[val_indices]

# 2. 创建模型
linear_model = nn.Linear(1, 1)

# 3. 构建优化器()
optimizer = optim.SGD(linear_model.parameters(), lr=1e-2)


# 4. 训练
def train_loop(n_epochs, optimizer, model, loss_fn, train_x, val_x, train_y, val_y):
    for epoch in range(1, n_epochs + 1):
        # 训练集向前
        train_y_p = model(train_x)
        train_loss = loss_fn(train_y_p, train_y)

        # 验证集向前
        val_y_p = model(val_x)
        val_loss = loss_fn(val_y_p, val_y)

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        if epoch % 100 == 0:
            print('Epoch {}, Train Loss {}, Val Loss {}'.format(epoch, float(train_loss), float(val_loss)))


train_loop(n_epochs=1000, optimizer=optimizer, model=linear_model, loss_fn=nn.MSELoss(), train_x=train_x, val_x=val_x,
           train_y=train_y,
           val_y=val_y)
