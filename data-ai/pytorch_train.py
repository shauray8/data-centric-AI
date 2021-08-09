import torch.nn as nn
import torch
from torch import torchvision

import ROMANPolicy from augmentaion

## ----------------- Cloning the model into pytorch cause that is easier for me to work with ----------------- ##

transforms = transforms.Compose([
    transforms.resize(32,32),
    ROMANPolicy(),
    transforms.ToTensor()])


class clone(nn.Module()):
    def __init__(self):
        super(self, clone).__init__()

        resnet_50 = torchvision.models.resnet50(pretrained = False)

