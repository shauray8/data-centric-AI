## -------------------- AUTO AUGMENT -------------------- ##

import albumentation 
import torch
import torch.nn as nn

import torchvision

class RomanPolicy(object):
    ## -------------------- the probability of applying the operation -------------------- ##
    ## -------------------- the magnitude of the operation -------------------- ##

    def __init__(self, fillcolor=(128,128,128)):
        self.policies[
        SubPolicy(.4, "posterize", 8, .6, "rotate", 9, fillcolor),
        ]


if __name__ == "__main__":
    print("some augmentations to improve the dataset !")
