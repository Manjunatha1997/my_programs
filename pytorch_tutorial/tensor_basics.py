from itertools import tee
from re import S
from cv2 import cubeRoot, mean
from numpy import float32
import torch

## tensor initilization

## setting device
device = 'cuda' if torch.cuda.is_available() else 'cpu' 

my_tensor = torch.tensor([[1,2,3],[4,5,6]], dtype=torch.float32, device=device, requires_grad=True)



## Other commom initialization methods
x = torch.rand([3,4])
x = torch.zeros(size=(2,3))
x = torch.ones(size=(3,4))
x = torch.eye(3)
x = torch.empty(size=(2,3))
x = torch.empty(size=(2,3)).normal_(mean=0, std=1)
x = torch.empty(size=(1,2)).uniform_(20,90)


