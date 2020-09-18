
import os
from PIL import Image
from torch.utils import data
from torchvision import transforms as T

'''
    - transform.ToTensor()
        (0,255) -> (0,1)
    图像预处理transforms与normalize
    - torchvision.transforms 常用的图像预处理方法
        - 数据中心化、数据标准化、缩放、裁剪、旋转、翻转、填充、噪声添加、灰度变换、线性变换、仿射变换、亮度、饱和度及对比度变换等
    - trochvision.datasets 常用数据集的dataset实现,ImageNet,CIFAR-10等
    - transforms.normalize(-1,1)
        - 逐channel的对图像进行标准化（均值变为0，标准差变为1），可以加快模型的收敛
        - output = (input - mean) / std,
        - mean:各通道的均值
        - std：各通道的标准差
    - torchvision.model 常用的模型预训练,AlexNet,VGG,ResNet,Lstm等
'''

class Hand(data.Dataset):
    def __init__(self,root,transforms = None,train=True):
        '''
        get image,divide into train/val set
        '''
        self.train = train
        self.images_root = root
        self._read_txt_file()
        if transforms is None:
            # 数据增强
            normalize = T.Normalize(mean=[0.485,0.456,0.406],
                                    std = [0.229,0.224,0.225])
            if not train:
                # 将多个图像预处理步骤整合一起
                self.transforms = T.Compose([
                    T.Scale(224),
                    T.CenterCrop(224),
                    T.ToTensor(),
                    normalize
                ])
            else:
                self.transforms = T.Compose([
                    T.Scale(256),
                    T.RandomSizedCrop(224),
                    T.RandomHorizontalFlip(),
                    T.ToTensor(),
                    normalize
                ])

    def _read_txt_file(self):
        self.images_path = []
        self.images_labels = []

        if self.train:
            txt_file = self.images_root + './images/train.txt'
        else:
            txt_file = self.images_root + './images/test.txt'

        with open(txt_file,'r') as f:
            lines = f.readlines()
            for line in lines:
                item = line.strip().split(' ')
                self.images_path.append(item[0])
                self.images_labels.append(item[1])

    def __getitem__(self, index):
        '''
        return the data of one image
        '''
        img_path = self.images_root + self.images_path[index]
        label = self.images_labels[index]
        data = Image.open(img_path)
        return data,int(label)

    def __len__(self):
        return len(self.images_path)


