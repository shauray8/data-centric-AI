import torch.nn as nn
import torch

import PIL
import numpy as np
from augmentation import RomanPolicy

path = "./docs/1.png"
image = PIL.Image.open(path)
policy = RomanPolicy()
transformed = policy(image)


plt.imshow(transformed)
plt.show()
