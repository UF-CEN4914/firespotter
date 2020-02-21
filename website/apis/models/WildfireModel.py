import torch.nn as nn
import torch.nn.functional as F

class WildfireModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.kernel_size = 5

        self.conv1 = nn.Conv2d(in_channels=3,  out_channels=16,  kernel_size=self.kernel_size)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32,  kernel_size=self.kernel_size)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=self.kernel_size)

        self.fc1 = nn.Linear(5184, 512)
        self.fc2 = nn.Linear(512, 128)
        self.fc3 = nn.Linear(128, 32)
        self.fc4 = nn.Linear(32, 8)
        self.fc5 = nn.Linear(8, 1)

    def forward(self, x):
        x = F.max_pool2d(F.leaky_relu(self.conv1(x)), (2,2))
        x = F.max_pool2d(F.leaky_relu(self.conv2(x)), (2,2))
        x = F.max_pool2d(F.leaky_relu(self.conv3(x)), (2,2))
        
        x = x.view(-1, 5184) # flatten to input to the linear layer
        
        x = F.leaky_relu(self.fc1(x))
        x = F.leaky_relu(self.fc2(x))
        x = F.leaky_relu(self.fc3(x))
        x = F.leaky_relu(self.fc4(x))
        x = F.leaky_relu(self.fc5(x))
                    
        x = F.sigmoid(x)
        return x