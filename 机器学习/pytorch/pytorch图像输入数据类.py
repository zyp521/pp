# @Time : 2021/4/415:25
# @Author : 周云鹏
# @File : pytorch入门.PY

import torch
import os
from PIL import Image
from torch.utils.data import Dataset, DataLoader, TensorDataset


class RMB(Dataset):

    def __init__(self, base_path, label_path):
        self.base_path = base_path
        self.label_path = label_path
        self.items_path = os.path.join(self.base_path, label_path)
        self.items = os.listdir(self.items_path)

    def __getitem__(self, index):
        im = Image.open(os.path.join(self.items_path, self.items[index]))
        label = self.label_path
        return im, label

    def __len__(self):
        return len(self.items)


if __name__ == '__main__':
    rmb = RMB('RMB_data', '1')
    im, label = rmb[0]
    im.show()
