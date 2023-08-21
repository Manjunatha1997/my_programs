
from statistics import mode
from turtle import color
from h11 import Data
from spacy import load
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torchvision.transforms as transformers
import torchvision.datasets as datasets
from tqdm import tqdm
from colorama import Fore


class NN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_size,50)
        self.fc2 = nn.Linear(50,num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

## Create simple CNN 
class CNN(nn.Module):
    def __init__(self,in_channels=1,num_classes=10):
        super(CNN,self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1,out_channels=8,kernel_size=(3,3),stride=(1,1),padding=(1,1))
        self.pool = nn.MaxPool2d(kernel_size=(2,2),stride=(2,2))
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3,3),stride=(1,1),padding=(1,1))
        self.fc1 = nn.Linear(16*7*7,num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = x.reshape(x.shape[0],-1)
        x = self.fc1(x)
        return x


model = CNN()
x = torch.randn(64,1,28,28)
print(model(x).shape)

## Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu' ) 
print(device)


## Hyper parameters
input_size = 784
in_channels = 1
num_classes = 10
learlning_rate = 0.001
batch_size = 64
epochs = 5


## Load data
train_dataset = datasets.MNIST(root='dataset/', train=True,transform=transformers.ToTensor(),download=True)
test_dataset = datasets.MNIST(root='dataset/', train=False,transform=transformers.ToTensor(),download=True)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle= True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)



## Initialise Network
model = CNN().to(device)
print(model)

exit()
## Loss and optimizer
criterian = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learlning_rate)

## Check accuracy
def check_accuracy(loader, model):
    if loader.dataset.train:
        print('training dataset')
    else:
        print('testing dataset')
    num_correct = 0
    num_samples = 0
    model.eval()

    # loader = tqdm(loader)

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            y = y.to(device)
            # x = x.reshape(x.shape[0], -1)
            
            scores = model(x)
            _,predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
    print(f'accuracy : {float(num_correct)/float(num_samples)*100}')
    model.train()



## Train network
for epoch in range(epochs):
    for batch_idx, (data, targets) in enumerate(train_loader):
        data = data.to(device)
        targets = targets.to(device)

        # forward
        scores = model(data)
        loss = criterian(scores, targets)
        

        # backward
        optimizer.zero_grad()
        loss.backward()

        optimizer.step()
    
    print(f'epoch: {epoch} / {epochs} loss: {loss} ')


    check_accuracy(train_loader, model)
    check_accuracy(test_loader, model)

















