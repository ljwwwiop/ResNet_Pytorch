from torch import nn
from utils import Tester
from network import resnet34,resnet101

params = Tester.TestParams()
# params.gpus = [] -> cpu  if len(params.gpus)>1, default to use params.gpus[0] to test
params.gpus = []
params.ckpt = './models/ckpt_epoch_800_res101.pth' #'./models/ckpt_epoch_400_res34.pth'
# params.ckpt = './models/ckpt_epoch_400_res34.pth'
params.testdata_dir = './testimg/'

# models
# model = resnet34(pretrained=False, num_classes=1000)  # batch_size=120, 1GPU Memory < 7000M
# model.fc = nn.Linear(512, 6)
model = resnet101(pretrained=False,num_classes=1000)  # batch_size=60, 1GPU Memory > 9000M
model.fc = nn.Linear(512*4, 6)

# Test
tester = Tester(model,params)
tester.test()



